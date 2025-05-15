import os
import pytest
from framework_core.config import Config
import allure

with allure.step("Получение конфигурации из test_config.toml"):
    @pytest.fixture(scope="class", autouse=True)
    def config(request):
        """
        Фикстура для автоматического подбора конфигурационного файла.
        По умолчанию ищет файл test_config.toml в той же папке, где находится сам тест.
        """
        test_dir = os.path.dirname(request.fspath)
        config_path = os.path.join(test_dir, "test_config.toml")
        return Config(config_path)
