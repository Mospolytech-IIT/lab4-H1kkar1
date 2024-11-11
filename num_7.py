"""Задание 7"""
import json
import requests
from num_6 import APIRequestError


def get_api_data(url):
    """
    Рандомная API дата
    :param url: Url для сайта который мы выбрали
    :return: Результат запроса в виде Json
    """
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            raise APIRequestError(response.status_code, response.text)
        response_json = json.loads(response.text)
        result = json.dumps(response_json, indent=4)
        return result
    except APIRequestError as e:
        print(e)
        print("Обработка ошибки запроса API с использованием URL-адреса API по умолчанию")
        url = "https://api.ipify.org?format=json"
        return get_api_data(url)
    except requests.RequestException as e:
        print(f"Произошло исключение по запросу: {e}")
        return get_api_data(url)
    except Exception as e:
        print(f"Произошло неожиданное исключение: {e}")
        return get_api_data(url)
    finally:
        print("Функция завершила свою работу и отчистила ресурсы")
