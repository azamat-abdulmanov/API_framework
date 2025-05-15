from services.hotel.models import Hotel
from framework_core.api.base_api import BaseApi
from requests import Response
import allure


class HotelApi(BaseApi):
    """Класс для работы с объектом Отель"""

    endpoint = 'accounts'
    hotel_model = Hotel

    @allure.step("Получение данных отеля")
    def get_hotel_data(self, uid: str) -> Response:
        """Получить данные по конкретному объекту размещения
        :param uid: uid
        :return Response: ответ"""

        params = {"uid": uid}

        self.response = self.client.get(endpoint=self.endpoint, params=params)
        return self.response

    @allure.step("Проверка данных ответа")
    def validate_response_schema(self):
        """Проверить модель ответа"""

        self.hotel_model(**self.response.json())
