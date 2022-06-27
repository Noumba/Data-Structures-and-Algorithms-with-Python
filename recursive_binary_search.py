from logging.config import listen
from re import L


def recursive_binary_search(list, searched_val):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == searched_val:
            return True
        elif list[midpoint] < searched_val:
            return recursive_binary_search(list[midpoint+1:], searched_val)
        elif list[midpoint] > searched_val:
            return recursive_binary_search(list[:midpoint], searched_val)
        else:
            return False
    return None


def verify_searched(index):
    print("Searched value is in the list: ", index)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

value = recursive_binary_search(numbers, 7)
value2 = recursive_binary_search(numbers, 15)
verify_searched(value)
verify_searched(value2)
