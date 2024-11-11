"""Задание 4"""


def count_words(file_path):
    """
    Функция для подсчёта слов
    :param file_path: Путь до файла
    :return: количество строк
    """
    try:
        with open(file_path, 'r', encoding='utf-16') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"Общее количество слов: {word_count}")
            return word_count
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}'не был найден.")
        return 0
    except IOError:
        print(f"Ошибка: При чтении файла произошла ошибка ввода-вывода '{file_path}'.")
        return 0
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return 0
    finally:
        print("Очистка ресурсов и обеспечение нормального завершения работы")


def count_lines(file_path):
    """
    Функция для подсчёта строк
    :param file_path: Путь до файла
    :return: Количество строк
    """
    try:
        with open(file_path, 'r', encoding='utf-16') as file:
            lines = file.readlines()
            line_count = len(lines)
            print(f"Общее количество строк{line_count}")
            return line_count
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}'не был найден.")
        return 0
    except IOError:
        print(f"Ошибка: При чтении файла произошла ошибка ввода-вывода '{file_path}'.")
        return 0
    except UnicodeDecodeError:
        print(f"Ошибка: При чтении файла произошла ошибка декодирования'{file_path}'.")
        return 0
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return 0
    finally:
        print("Очистка ресурсов и обеспечение нормального завершения работы")


def count_characters(file_path):
    """
    Функция для подсчёта символов
    :param file_path: путь до файла
    :return: Количество символов
    """
    try:
        with open(file_path, 'r', encoding='utf-16') as file:
            content = file.read()
            char_count = len(content)
            print(f"Общее количество символов: {char_count}")
            return char_count
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не был найден.")
        return 0
    except IOError:
        print(f"Ошибка: При чтении файла произошла ошибка ввода-вывода '{file_path}'.")
        return 0
    except UnicodeDecodeError:
        print(f"Ошибка: При чтении файла произошла ошибка декодирования '{file_path}'.")
        return 0
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return 0
    finally:
        print("Очистка ресурсов и обеспечение нормального завершения работы")
