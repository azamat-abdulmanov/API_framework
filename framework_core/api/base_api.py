from framework_core.api.api_client import ApiClient
from requests import Response
import allure


class BaseApi:
    """Базовый класс API"""

    response: Response

    def __init__(self, client: ApiClient):
        self.client = client

    @allure.step("Проверка статус кода")
    def check_status_code(self, status: int):
        """Проверка статус кода
        :param status: статус код"""

        assert self.response.status_code == status, f"Неверный статус код {status}"

    @allure.step("Проверка тела ответа")
    def check_body(self, body: dict):
        """Проверка тела ответа
        :param body: тело ответа"""

        response_dict = self.response.json()

        assert response_dict == body, f"Неверное тело ответа {response_dict}"

