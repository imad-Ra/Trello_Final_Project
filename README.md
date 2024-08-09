
## Overview
This project provides an automated testing suite for Trello, covering both UI and API functionalities. Trello is a web-based, Kanban-style list-making application used for project management and task organization.

## Features
- UI automation using Selenium WebDriver
- API testing with Requests library
- Integration with Allure for detailed reporting
- Jira integration for test case management

## Test Scope

### UI Testing
- Core functionalities: board creation, task management, collaboration features, synchronization, notifications
- Example tests:
  - Verify task creation, editing, and deletion
  - Ensure real-time synchronization across different browsers

### API Testing
- Core API endpoints: Actions, Boards, Cards, Lists, Members
- Example tests:
  - Verify CRUD operations for boards via API
  - Ensure API responses adhere to specified schema and performance benchmarks

## Setup
1. Clone the repository:
git clone https://github.com/imad-Ra/Trello_Final_Project.git
cd Trello_Final_Project

2. Install dependencies:
pip install -r requirements.txt
Copy
3. Configure environment variables:
cp .env.example .env
Edit .env with your Trello API key and token

## Running Tests

### UI Tests
pytest ui/tests

### API Tests
pytest api/tests

### All Tests with Allure Report
pytest --alluredir=./reports
allure serve reports

## Tools and Technologies
- IDE: PyCharm version 2024.1.1
- Automation Framework: Selenium version 4.22.0
- Programming Language: Python 3.8+
- Browser: Google Chrome version 126.0.6478.127
- WebDriver: Chrome WebDriver
- API Testing: Requests library
- Test Framework: Pytest
- Reporting: Allure Framework
- Version Control: Git
- Bug Tracking: Jira

## Allure Reporting
Allure provides detailed test results including test case steps, screenshots, and API logs.

To set up and use Allure:
1. Install Allure:
npm install -g allure-commandline
Copy2. Run tests with Allure:
pytest --alluredir=./reports
allure serve reports
Copy

## Jira Integration
Our test suite integrates with Jira for bug tracking and test case management.


## Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request

## Contact
For questions or suggestions, please contact:
- **Name**: Imad Rabah
- **Email**: imadrabah123@gmail.com
- **GitHub**: [ImadRabah](https://github.com/imad-Ra)
