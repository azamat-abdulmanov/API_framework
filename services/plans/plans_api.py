from services.plans.models import Plans
from framework_core.api.base_api import BaseApi
from requests import Response
import allure


class PlanApi(BaseApi):
    """Класс для работы с объектом Тарифы"""

    endpoint = 'plans'
    plan_model = Plans

    @allure.step("Получение данных о тарифах")
    def get_plan_data(self, account_id: int) -> Response:
        """Получение данных о тарифах
        :param account_id: id аккаунта
        :return response: объект Response"""

        params = {'account_id': account_id}
        self.response = self.client.get(endpoint=self.endpoint, params=params)
        return self.response

    @allure.step("Проверка данных ответа")
    def validate_response_schema(self):
        """Проверить модель ответа"""

        self.plan_model(**self.response.json())