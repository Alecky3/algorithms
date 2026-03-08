# Binary search algorithm using the iterative approach
def binary_search_iterative(items_list: list, target_item: any) -> int:
    """
    Searches for the target element using interative binary search algorith.

    Args:
    target_item(any): The item to search.

    Returns:
    (int): the index of the target element if found, else -1.
    """
    start, end = 0, len(items_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if(item_list[mid] == target_item):
            return target_item
        
        if(items_list[mid] > target_item):
            end = mid - 1
        else:
            start = mid + 1

    return -1

# Binary seach using recursive method
def binary_search_rec(items_list: list, target_item: any) -> int | bool:
    """
    Searches the target item using recursive binary search.

    Args:
    items_list(list): The list to search.
    target_item(int): The target to search.

    Returns:
    (int | bool): Returns the index if search successfull else returns False
    """

    mid = len(items_list) // 2
    if(len(items_list) == 1):
        return mid if items_list[mid] == target_item else False
    
    if(items_list[mid] == target_item):
        return mid
    else:
        if(items_list[mid] < target_item):
            callback_result = binary_search_rec(items_list[mid:],target_item)
            return mid + callback_result if callback_result is not False else False
        else:
            return binary_search_rec(items_list[:mid], target_item)


if __name__ == "__main__":
    item_list = [1, 2, 3, 4, 5, 6, 7, 8]
    target_item = 8
    print(binary_search_rec(item_list,target_item)) 