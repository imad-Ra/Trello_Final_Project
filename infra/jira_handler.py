import logging
from jira import JIRA
from infra.config_provider import ConfigProvider

class JiraHandler:
    def __init__(self):
        self.config = ConfigProvider().load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self._jira_url = self.secret["jira_url"]
        self._auth_jira = JIRA(
            basic_auth=(self.secret["jira_email"], self.secret["jira_api_token"]),
            options={'server': self._jira_url}
        )
        self.logger = logging.getLogger(__name__)

    def create_issue(self, project_key, summary, description, issue_type="Bug"):
        # Get all issue types for the project
        project = self._auth_jira.project(project_key)
        issue_types = self._auth_jira.issue_types_for_project(project.id)

        # Find the Bug issue type
        bug_issue_type = next((it for it in issue_types if it.name.lower() == "bug"), None)

        if bug_issue_type:
            issue_type_id = bug_issue_type.id
            self.logger.info(f"Using Bug issue type with ID: {issue_type_id}")
        else:
            # If Bug type is not found, log a warning and use the default issue type
            default_issue_type = issue_types[0]
            issue_type_id = default_issue_type.id
            self.logger.warning(f"Bug issue type not found. Using default issue type: {default_issue_type.name}")

        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'id': issue_type_id}
        }

        # Print the issue dictionary for debugging
        self.logger.debug(f"Creating issue with fields: {issue_dict}")

        new_issue = self._auth_jira.create_issue(fields=issue_dict)
        self.logger.info(f"Created issue: {new_issue.key} with type: {new_issue.fields.issuetype.name}")
        return new_issue