def binary_search(list, searched_val):
    first_index = 0
    last_index = len(list) - 1

    while first_index <= last_index:
        midpoint = (first_index + last_index) // 2
        if list[midpoint] == searched_val:
            return midpoint
        elif list[midpoint] < searched_val:
            first_index = midpoint + 1
        else:
            last_index = midpoint - 1

    return None


def verify_searched(index):
    if index is not None:
        print("The index of the searched value in the list is: ", index)
    else:
        print("The index of the searched value in the list is None.")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

value = binary_search(numbers, 7)
verify_searched(value)
