import requests
import allure
import json
from framework_core.api.api_client_exception import APIRequestException


class BaseAPIClient:
    """Базовый класс client"""

    def __init__(self, base_url: str, headers: dict = None, timeout: int = 10):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.timeout = timeout

    @allure.step("Выполнение {method} запроса к {endpoint}")
    def __request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Приватный метод для логирования запросов
        :param method: Метод запроса
        :param endpoint: endpoint запроса
        :param kwargs: Параметры запроса
        :param check_status: выдает ошибку при статусах 400 и 500
        :return: Response ответ"""

        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            with allure.step(f"Запрос: {method} {url}"):
                # Логируем параметры запроса
                if 'json' in kwargs:
                    allure.attach(
                        body=str(kwargs['json']),
                        name="Request JSON",
                        attachment_type=allure.attachment_type.JSON,
                    )
                elif 'data' in kwargs:
                    allure.attach(
                        body=str(kwargs['data']),
                        name="Request Data",
                        attachment_type=allure.attachment_type.TEXT,
                    )
                if 'params' in kwargs:
                    allure.attach(
                        body=str(kwargs['params']),
                        name="Request Params",
                        attachment_type=allure.attachment_type.TEXT,
                    )

                response = self.session.request(method=method.upper(), url=url, timeout=self.timeout, **kwargs)

                # Логируем ответ
                allure.attach(
                    body=json.dumps(response.json()),
                    name=f"Response [{response.status_code}]",
                    attachment_type=allure.attachment_type.JSON if 'application/json' in response.headers.get(
                        'Content-Type', '') else allure.attachment_type.TEXT,
                )

            return response

        except requests.exceptions.RequestException as e:
            # Логируем информацию об ошибке в Allure
            with allure.step(f"Ошибка при выполнении запроса {method} {url}"):
                allure.attach(
                    body=str(e),
                    name="Ошибка",
                    attachment_type=allure.attachment_type.TEXT,
                )
                if 'response' in locals():
                    allure.attach(
                        body=response.text,
                        name=f"Response on Error [{response.status_code}]",
                        attachment_type=allure.attachment_type.JSON if 'application/json' in response.headers.get(
                            'Content-Type', '') else allure.attachment_type.TEXT,
                    )

            raise APIRequestException(f"Ошибка запроса {method} {url}: {e}")

    def get(self, endpoint: str, params: dict = None, **kwargs) -> requests.Response:
        """Get запрос
        :param endpoint: endpoint запроса
        :param params: параметры запроса
        :param kwargs: дополнительные параметры
        :return: объект Response"""

        return self.__request("GET", endpoint, params=params, **kwargs)

    def post(self, endpoint: str, json: dict = None, data=None, **kwargs) -> requests.Response:
        """Post запрос
        :param endpoint: endpoint запроса
        :param json: json body
        :param data: data body
        :param kwargs: дополнительные параметры
        :return: объект Response"""

        return self.__request("POST", endpoint, json=json, data=data, **kwargs)

    def put(self, endpoint: str, json: dict = None, **kwargs) -> requests.Response:
        """Put запрос
        :param endpoint: endpoint запроса
        :param json: json body
        :param kwargs: дополнительные параметры
        :return: объект Response"""

        return self.__request("PUT", endpoint, json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Delete запрос
        :param endpoint: endpoint запроса
        :param kwargs: дополнительные параметры
        :return: объект Response"""

        return self.__request("DELETE", endpoint, **kwargs)

    def set_headers(self, headers: dict):
        """Обновление заголовков
        :param headers: новые заголовки"""

        self.session.headers.update(headers)

class ApiClient(BaseAPIClient):
    """JSON client"""
    pass
