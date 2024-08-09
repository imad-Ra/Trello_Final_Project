from jira import JIRA
from infra.config_provider import ConfigProvider

class JiraHandler:
    def __init__(self):
        self.secret = ConfigProvider.load_from_secret()
        self.jira = JIRA(
            server=self.secret['jira_url'],
            basic_auth=(self.secret['jira_email'], self.secret['jira_api_token'])
        )

    def create_issue(self, summary, description):
        issue_dict = {
            'project': {'key': self.secret['jira_project_key']},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Bug'},
        }
        return self.jira.create_issue(fields=issue_dict)