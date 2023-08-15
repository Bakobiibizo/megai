def does_not_contain(item, item_list):
    return all(element not in item for element in item_list)
