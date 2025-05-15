from framework_core.api.base_test_case_api import BaseTestCaseApi
from services.plans.plans_api import PlanApi
from tests.test_plans.data import ErrorMessage
import allure


class TestPlans(BaseTestCaseApi):
    """Тест-кейс Тарифы"""

    error_msg = ErrorMessage

    with allure.step("Проверка данных о тарифах"):
        def test_get_data_on_room_categories(self):
            """Получение данных о тарифах"""
            plan_api = PlanApi(self.client)
            plan_api.get_plan_data(self.config.get("account_id"))
            plan_api.check_status_code(200)
            plan_api.validate_response_schema()

    with allure.step("Отправка get запроса без uid"):
        def test_get_request_without_uid(self):
            """Отправка get запроса без uid"""
            self.hotel_api = PlanApi(self.client)
            self.hotel_api.get_plan_data('')
            self.hotel_api.check_status_code(406)
            self.hotel_api.check_body(self.error_msg.get_without_uid)