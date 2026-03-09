# Bubble sort algorithm
def bubble_sort(items_list: list) -> list:
    """
    Sort items_list using bubble sort algorithm.

    Args:
    target_list: List of items to sort.
    """

    for i in range(len(items_list)):
        for j in range((len(items_list) - 1 - i)):
            if (items_list[j] > items_list[j + 1]):
                items_list[j], items_list[j + 1] = items_list[j + 1], items_list[j]
    return items_list
