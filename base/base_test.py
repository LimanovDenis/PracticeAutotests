import pytest

from pages.login_page import LoginPage
from pages.personal_page import PersonalPage
from pages.dashboard_page import DashBoardPage
from config.data import Data


class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard_page: DashBoardPage
    personal_page: PersonalPage

    @pytest.fixture(autouse=True)
    def setup(self, driver, request):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashBoardPage(driver)
        request.cls.personal_page = PersonalPage(driver)

