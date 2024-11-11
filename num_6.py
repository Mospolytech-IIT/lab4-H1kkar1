"""Задание 6"""
import json
import requests


class InvalidParameterError(Exception):
    """Пользовательская ошибка"""
    def __init__(self, parameter_name, parameter_value):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.message = f"Недопустимое значение параметра '{parameter_name}': {parameter_value}"
        super().__init__(self.message)


def check_parameter(value: int):
    """
    Тестовая функция

    :param value: int

    :return: Значение переменной value
    """
    if value <= 0:
        raise InvalidParameterError("value", value)
    return value


class FileReadError(Exception):
    """Пользовательская ошибка"""
    def __init__(self, file_path):
        self.file_path = file_path
        self.message = f"Ошибка при чтении файла '{file_path}'"
        super().__init__(self.message)


def read_file(file_path):
    """
    Чтение файла

    :param file_path: Путь до файла в системе

    :return: Возвращает то что в файле
    """
    try:
        with open(file_path, 'r', encoding='utf-16') as file:
            content = file.read()
            return content
    except FileNotFoundError as exc:
        raise FileReadError(file_path) from exc


class APIRequestError(Exception):
    """Пользовательская ошибка"""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = f"Ошибка запроса API с кодом состояния {status_code}: {message}"
        super().__init__(self.message)


def get_api_data(url):
    """
    Проверка на получение статус кода 200

    :param url: Url адрес сайта который мы выбрали

    :return: Результат в виде Json
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise APIRequestError(response.status_code, response.text)
    response_json = json.loads(response.text)
    result = json.dumps(response_json, indent=4)
    return result.json()
