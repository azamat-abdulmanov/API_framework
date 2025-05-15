class APIClientException(Exception):
    """Базовое исключение для API клиента."""


class APIRequestException(APIClientException):
    """Исключение при ошибке запроса."""