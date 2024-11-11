"""Задание 2"""


class User:
    """
    Класс пользователя
    """
    def __init__(self):
        self.__name = ''
        self.__age = 0

    @property
    def name(self):
        """
        getter (name)
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        setter (name)
        """
        if isinstance(name, str):
            raise TypeError("Тип значения name не строка")
        self.__name = name

    @property
    def age(self):
        """
        getter (age)
        """
        return self.__age

    @age.setter
    def age(self, age):
        """
        setter (age)
        """
        if age > 100:
            raise ValueError("Значение переменной age > 100")
        self.__age = age

    def __str__(self):
        """
        :return:
        Информация об объекте
        """
        return f"Имя пользователя: {self.__name}\nВозраст пользователя: {self.__age}"


def func_3(name: str, age: int) -> User:
    """

    :param name: Имя пользователя
    :param age: Его возраст
    :return: Информация о зарегистрированном пользователе
    """
    person = User()
    try:
        person.name = name
        person.age = age
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

    return person
