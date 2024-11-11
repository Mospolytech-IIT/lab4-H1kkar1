"""Задание 3"""


def process_parameters(*args):
    """

    :param args: любые параметры
    :return: сумма из args
    """
    try:
        for arg in args:
            if arg is None or arg == "":
                raise ValueError("Параметры не должны быть None или пустой строкой")
            if isinstance(arg, int) and arg < 0:
                raise ValueError("число не должно быть отрицательным")
            if isinstance(arg, str) and len(arg) > 10:
                raise ValueError("")

        result = sum(arg for arg in args if isinstance(arg, int))
        print(f"сумма чисел равна {result}")

    except TypeError as e:
        print(f"Вы ввели не корректный тип данных: {e}")

    finally:
        print("Очистка ресурсов и обеспечение нормального завершения работы")


process_parameters(10, "test", -5)
process_parameters(10, "test", 5, 23)
process_parameters(10, "thisisalongstring", 5)
