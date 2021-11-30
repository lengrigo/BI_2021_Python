
def sequential_map(*args):
    lst = list(args[-1])
    for arg in args[:-1]:
        lst = list(map(arg, lst))
    return lst


# # Test for sequential_map
# print(sequential_map(np.square, np.sqrt, lambda x: x ** 3, [1, 2, 3, 4, 5]))

def consensus_filter(*args):
    lst = list(args[-1])
    for arg in args[:-1]:
        lst = list(filter(arg, lst))
    return lst


# # Test for consensus_filter
# print(consensus_filter(lambda x: x > 0, lambda x: x > 5, lambda x: x < 10, [-2, 0, 4, 6, 11]))


def conditional_reduce(filter_function, reduce_function, lst):
    filtered_lst = list(filter(filter_function, lst))
    for i in range(len(filtered_lst) - 1):
        filtered_lst[i + 1] = reduce_function(filtered_lst[i], filtered_lst[i + 1])
    return filtered_lst[-1]


# # Test for conditional_reduce
# print(conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10]))

def func_chain(*args):
    def returned_function(value):
        value = [value]
        for func in args:
            value = list(map(func, value))
        return value

    return returned_function


# # Test for func_chain
# my_chain = func_chain(lambda x: x + 2, lambda x: (x/4, x//4))
# print(*my_chain(37))


# ---------------------------------------
# For 2 additional points
def sequential_map_2(*args):
    function = func_chain(*args[:-1])
    return function(args[-1])


# # Test for sequential_map2
# print(sequential_map_2(np.square, np.sqrt, lambda x: x ** 3, [1, 2, 3, 4, 5]))
