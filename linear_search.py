
def linear_search(list, searched_val):
    """Returns the position of the searched value in the list if found"""

    for i in range(0, len(list)):
        if list[i] == searched_val:
            return i
    return None


def verify_searched(index):
    if index is not None:
        print("The index of the searched value in the list is: ", index)
    else:
        print("The index of the searched value in the list is None.")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

value = linear_search(numbers, 2)
verify_searched(value)
