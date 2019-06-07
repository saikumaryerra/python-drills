def sum_items_in_list(x):
    return sum(x)


def list_length(x):
    return len(x)


def last_three_items(x):
    return x[-3:] 


def first_three_items(x):
    return x[:3]


def sort_list(x):
    x.sort()
    return x


def append_item(x, item):
    x.append(item)
    return x


def remove_last_item(x):
    x.pop()
    return x


def count_occurrences(x, item):
    return x.count(item)


def is_item_present_in_list(x, item):
    return item in x


def append_all_items_of_y_to_x(x, y):
    """
    x and y are lists
    """
    #return x+y
    x.extend(y)
    return x


def list_copy(x):
    """
    Create a shallow copy of x
    """
    y=[]
    for i in x:
        y.append(i)
    return y

