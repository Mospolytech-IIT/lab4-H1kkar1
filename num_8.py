"""Задание 8"""


class InvalidAgeError(Exception):
    """Пользовательское исключение"""
    def __init__(self, age):
        """Генерируем исключение"""
        self.age = age
        self.message = f"Некорректный возраст: {age}. Он должен быть в пределах от 0 до 120."
        super().__init__(self.message)


def check_age(age):
    """
    Проверка возраста

    :param age: Возраст

    :return: Валидный возраст
    """
    try:
        if age < 0 or age > 120:
            raise InvalidAgeError(age)
        print(f"Валидный возраст: {age}")
    except InvalidAgeError as e:
        print(e)
        age = 18
        print(f"Возраст обновлён до: {age}")


class StringTooLongError(Exception):
    """Пользовательское исключение"""
    def __init__(self, string, max_length):
        """Генерируем исключение"""
        self.string = string
        self.max_length = max_length
        self.message = f"Строка слишком длинная: '{string}'. Максимум {max_length} символов."
        super().__init__(self.message)


def check_string_length(string, max_length):
    """
    Проверка длинны строки

    :param string: Начальная строка

    :param max_length: Максимальная длинна

    :return: Валидная строка
    """
    try:
        if len(string) > max_length:
            raise StringTooLongError(string, max_length)
        print(f"Valid string: '{string}'")
    except StringTooLongError as e:
        print(e)
        string = string[:max_length]
        print(f"Усеченная строка: '{string}'")


class NegativeValueError(Exception):
    """Пользовательское исключение"""
    def __init__(self, value):
        """Генерируем исключение"""
        self.value = value
        self.message = f"Найдено отрицательное значение: {value}. Все значения должны быть положительными."
        super().__init__(self.message)


class NonNumericValueError(Exception):
    """Пользовательское исключение"""
    def __init__(self, value):
        """Генерируем исключение"""
        self.value = value
        self.message = f"Найдено нечисловое значение: {value}. Все значения должны быть числами."
        super().__init__(self.message)


def check_positive_numbers(numbers):
    """
    Проверям числа
    :param numbers: входные числа
    :return: Проверка на num > 0
    """
    try:
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise NonNumericValueError(num)
            if num < 0:
                raise NegativeValueError(num)
        print("Все значения являются положительными числами.")
    except NegativeValueError as e:
        print(e)
        print("Обработка ошибки отрицательного значения путем удаления отрицательного значения")
        numbers.remove(e.value)
        print(f"Обновленный список: {numbers}")
    except NonNumericValueError as e:
        print(e)
        print("Обработка ошибки, связанной с нечисловым значением, путем удаления нечислового значения")
        numbers.remove(e.value)
        print(f"Обновленный список: {numbers}")
    except Exception as e:
        print(f"Обнаружено неожиданное исключение: {e}")
