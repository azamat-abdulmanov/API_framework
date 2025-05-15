import pytest
from framework_core.api.api_client import ApiClient
from framework_core.config import Config


class BaseTestCaseApi:
    """Базовый класс для тестов"""

    client: ApiClient
    config: Config

    @pytest.fixture(autouse=True)
    def setup(self, request, config):
        request.cls.config = config
        request.cls.client = ApiClient(base_url=self.config.get("base_url"))
