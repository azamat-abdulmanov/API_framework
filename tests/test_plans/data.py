class ErrorMessage:
    """Класс для хранения сообщений об ошибках."""
    get_without_uid = {
                "errors": [
                    {
                        "field": "account_id",
                        "type": "PresenceOf",
                        "message": "Не передан обязательный параметр account_id"
                    }
                ],
                "request": {
                    "url": "/v1/api/plans?account_id=",
                    "method": "GET",
                    "params": {
                        "_url": "/v1/api/plans",
                        'account_id': ''
                    }
                }
            }