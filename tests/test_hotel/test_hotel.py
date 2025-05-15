from framework_core.api.base_test_case_api import BaseTestCaseApi
from services.hotel.hotel_api import HotelApi
from tests.test_hotel.data import ErrorMessage
import allure


class TestHotel(BaseTestCaseApi):
    """Тест-кейс Отель"""

    error_msg = ErrorMessage()

    with allure.step("Проверка мета-информации об отеле"):
        def test_get_hotel_data(self):
            """Получение мета-информация об отеле"""
            hotel_api = HotelApi(self.client)
            hotel_api.get_hotel_data(self.config.get("uid"))
            hotel_api.check_status_code(200)
            hotel_api.validate_response_schema()

    with allure.step("Отправка get запроса без uid"):
        def test_get_request_without_uid(self):
            """Отправка get запроса без uid"""
            self.hotel_api = HotelApi(self.client)
            self.hotel_api.get_hotel_data('')
            self.hotel_api.check_status_code(406)
            self.hotel_api.check_body(self.error_msg.get_without_uid)
