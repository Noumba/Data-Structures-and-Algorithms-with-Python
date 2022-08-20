def merge_sort(list_to_sort):
    """
    Sorts a list in ascending order
    Return a new sorted list

    Divide: Find the midpoint of the list and divide into sublist
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in previous step
    """

    if len(list_to_sort) <= 1:
        return list_to_sort

    left_half, right_half = split(list_to_sort)

    """Recursive portion of the function that continuouly split the list"""
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """Divide the unsorted list at midpoint into sublists
    Returns two lists: left and right"""

    midpoint = len(list)//2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right


def merge(left, right):
    """
    Merges two lists and sorted them in the process
    Returns a new list
    """

    l = []
    # keep track of the index of the left list
    i = 0
    # keep track of the index of the right list
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


list = [3, 1, 33, 21, 8, 6, 11]
l = merge_sort(list)
print(l)
