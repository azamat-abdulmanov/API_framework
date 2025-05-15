from services.room_types.models import Rooms
from framework_core.api.base_api import BaseApi
from requests import Response
from typing import Optional
import allure


class RoomTypeApi(BaseApi):
    """Класс для работы с объектом Тарифы"""

    endpoint = 'roomtypes'
    rooms_model = Rooms


    @allure.step("Получение данных отеля")
    def get_room_type_data(self,  account_id: int,  address_included: Optional[str] = None) -> Response:
        """Получить данные по данных о тарифах
        :param account_id: id аккаунта
        :param address_included: включенные адреса
        :return response: """

        params = {'account_id': account_id}
        if address_included:
            params.setdefault(address_included, None)

        self.response = self.client.get(endpoint=self.endpoint, params=params)
        return self.response

    @allure.step("Проверка данных ответа")
    def validate_response_schema(self):
        """Проверить модель ответа"""

        self.rooms_model(**self.response.json())