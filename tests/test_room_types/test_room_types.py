from framework_core.api.base_test_case_api import BaseTestCaseApi
from services.room_types.room_types_api import RoomTypeApi
import allure


class TestRoomTypes(BaseTestCaseApi):
    """Тест-кейс Категория номеров"""

    with allure.step("Проверка данных о категориях номеров"):
        def test_get_data_on_room_categories(self):
            """Получение данных о категориях номеров"""
            room_types_api = RoomTypeApi(self.client)
            room_types_api.get_room_type_data(self.config.get("account_id"))
            room_types_api.check_status_code(200)
            room_types_api.validate_response_schema()