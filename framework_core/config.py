import toml
import os

class Config:
    def __init__(self, path_to_toml):
        """
        Загрузка конфигурации из TOML-файла.
        """
        self.path_to_toml = path_to_toml
        self.reload()

    def reload(self):
        """
        Перегрузить конфигурацию из TOML-файла.
        """
        if os.path.exists(self.path_to_toml):
            with open(self.path_to_toml, "r", encoding="utf-8") as file:
                self._data = toml.load(file)
        else:
            raise FileNotFoundError(f"Файл конфигурации '{self.path_to_toml}' не найден.")

    def get(self, key=None, section="general"):
        """
        Получить значение из конкретной секции.
        :param section: Имя секции
        :param key: Ключ в секции (опционально)
        :return: Значение или секция целиком
 """
        if key not in self._data[section]:
            raise KeyError(f" В секции {section} нет ключа {key}")
        return self._data[section][key]