# 🚀 Trello Automation Suite

![Trello Test Management](https://github.com/imad-Ra/Trello_Final_Project/raw/master/image.png)

## 📌 Overview
This project delivers a robust automated testing suite for Trello, encompassing both UI and API functionalities. Our goal is to ensure the reliability and performance of Trello's core features through comprehensive automated testing.

## 🔑 Key Features
- 🖥️ UI automation using Selenium WebDriver
- 🔌 API testing with Requests library
- 📊 Integrated reporting with Allure
- 🔗 Jira integration for seamless test management

## 🎯 Test Scope
- UI Tests: Core Trello functionalities
- API Tests: Key Trello API endpoints
- Combined UI-API Tests: Two integrated tests demonstrating UI and API interaction

## 🛠️ Setup
1. Clone the repository:

   git clone https://github.com/imad-Ra/Trello_Final_Project.git
   cd Trello_Final_Project

Install dependencies:
   pip install -r requirements.txt

Configure environment variables:
   cp .env.example .env
# Edit .env with your Trello API key and token


▶️ Running Tests
UI Tests:
    test/web
API Tests:
    tests/api
All Tests with Allure Report:
    test --alluredir=./reports
    allure serve reports
🛠️ Tools and Technologies

IDE: PyCharm 2024.1.1
Automation Framework: Selenium 4.22.0
Programming Language: Python 3.8+
Browser: Google Chrome 126.0.6478.127
API Testing: Requests library
Test Framework: Pytest
Reporting: Allure Framework
Version Control: Git
Bug Tracking: Jira

📊 Allure Reporting
To set up and use Allure:

Install Allure:
    npm install -g allure-commandline

Run tests with Allure:
    test --alluredir=./reports
allure serve reports


🤝 Contributing
We welcome contributions! Here's how you can help:

Fork the repository
Create a feature branch: git checkout -b feature/NewFeature
Commit changes: git commit -am 'Add NewFeature'
Push to the branch: git push origin feature/NewFeature
Submit a pull request

📞 Contact
For inquiries or suggestions, please reach out:

👤 Name: Imad Rabah
📧 Email: imadrabah123@gmail.com
🐙 GitHub: ImadRabah [https://github.com/imad-Ra?tab=repositories]