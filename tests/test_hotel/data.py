class ErrorMessage:
    """Класс для хранения сообщений об ошибках."""
    get_without_uid = {
                "errors": [
                    {
                        "field": "uid",
                        "type": "PresenceOf",
                        "message": "Не передан обязательный параметр uid"
                    }
                ],
                "request": {
                    "url": "/v1/api/accounts?uid=",
                    "method": "GET",
                    "params": {
                        "_url": "/v1/api/accounts",
                        'uid': ''
                    }
                }
            }