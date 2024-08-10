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

    def create_issue(self, project_key, summary, description, issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }

        # Get all issue types for the project
        project = self._auth_jira.project(project_key)
        issue_types = [it.name for it in self._auth_jira.issue_types_for_project(project.id)]

        # If 'Bug' is not in the list of issue types, use the first available type
        if issue_type not in issue_types:
            issue_dict['issuetype']['name'] = issue_types[0]

        return self._auth_jira.create_issue(fields=issue_dict)