import pytest
from conftest import BaseUrl, Username,Password
from hrmpages.LoginPage import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_login:

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page = LoginPage(self.driver)

    def test_value_login(self):
        self.login_page.login(Username,Password)


    def tearDown_class(self):
        self.driver.quit()

