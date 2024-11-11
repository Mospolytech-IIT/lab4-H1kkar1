"""Задание 5"""
from datetime import datetime
import time
import json
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from requests.exceptions import HTTPError


def get_bpi_graph(iteration: int, s: int):
    """
    Функция для отображения графика индекса цен на биткоин (BPI) в форматах USD GBP EUR,
    USD - Доллар
    GBP - Фунт
    EUR - Евро

    :param iteration: Количество запросов

    :param s: Время ожидания между запросами

    :return: График зависимости цены от времени
    """
    try:
        if (iteration and s) < 0:
            raise ValueError("Входящие параметны не должны быть < 0")
        usd = []
        gpb = []
        eur = []
        events = []
        while iteration:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json", timeout=3)
            response.encoding = "utf-8"
            response_json = json.loads(response.text)

            t = response_json["time"]["updated"].split(" ")[3]
            events.append(datetime.strptime(t, '%H:%M:%S'))
            usd.append(float(response_json['bpi']['USD']['rate_float']))
            gpb.append(float(response_json['bpi']['GBP']['rate_float']))
            eur.append(float(response_json['bpi']['EUR']['rate_float']))

            time.sleep(s)

        fig, ax = plt.subplots(3, 1, sharex=True)

        plt.subplot(311)
        plt.plot(events, usd, 'r--')
        plt.subplot(312)
        plt.plot(events, gpb, 'g--')
        plt.subplot(313)
        plt.plot(events, eur, 'b--')

        ax[2].xaxis.set_major_locator(mdates.SecondLocator(interval=5))
        ax[2].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        fig.autofmt_xdate()

        plt.show()

        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    else:
        print("Success!")
