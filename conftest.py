import time
from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
Username = "Admin"
Password = "admin123"


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chrome_option = Options()
    chrome_option.add_experimental_option("detach", True)
    request.cls.driver = webdriver.Chrome()
    time.sleep(5)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()

    # Define the absolute path to the report directory
    report_dir = Path(r"C:\Users\Vozon\PycharmProjects\OrangeHRM\hrmreports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)

    # Set the full path to the report file with the correct date formatting
    report_file = report_dir / f"Report_{today.strftime('%Y%m%d')}.html"

    # Set the full path in pytest options
    config.option.htmlpath = str(report_file)
    config.option.contained_html = True



def pytest_html_report_title(report):
    report.title = "HRM Test Report"
