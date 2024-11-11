from num_1 import func_1, func_2
from num_2 import func_3
from num_3 import process_parameters
from num_4 import count_lines, count_words, count_characters
from num_5 import get_BPI_graph
from num_6 import (get_api_data, read_file, check_parameter,
                   InvalidParameterError, APIRequestError, FileReadError)
from num_7 import get_api_data
from num_8 import (InvalidAgeError, StringTooLongError, NegativeValueError,
                   check_age, check_string_length, check_positive_numbers)

def main():
    """Задание 1"""
    # print(func_1("a"))
    #
    # print(func_2(0))
    """Задание 2"""
    # print(func_3("asda", 321))
    """Задание 3"""
    # process_parameters(10, "test", -5)
    # process_parameters(10, "test", 5)
    # process_parameters(10, "thisisalongstring", 5)
    """Задание 4"""
    # count_words("text.txt")
    # count_lines("text.txt")
    # count_characters("text.txt")
    """Задание 5"""
    # get_BPI_graph(5, 10)
    """Задание 6"""
    # try:
    #     content = read_file("nonexistent_file.txt")
    # except FileReadError as e:
    #     print(e)
    #
    # try:
    #     result = check_parameter(-5)
    # except InvalidParameterError as e:
    #     print(e)
    #
    # try:
    #     data = get_api_data("https://api.coindesk.com/v1/bpi/asd")
    # except APIRequestError as e:
    #     print(e)
    """Задание 7"""
    get_api_data("https://randomuser.me/api/ssss")
    """Задание 8"""
    # check_age(150)
    # check_string_length("This is a very long string that exceeds the maximum length", 20)
    # check_positive_numbers([1, 2, -3, 4, "five", 6])


if __name__ == '__main__':
   main()

