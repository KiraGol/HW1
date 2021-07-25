from typing import Union, Callable, List, Dict, Tuple


def my_reduce(callback: Callable, sequence: Union[List, Tuple, Dict]) \
        -> Union[List, Tuple, Dict]:
    iterable_data = iter(sequence)
    result = next(iterable_data)
    for element in sequence:
        result = callback(result, element)
    return result


if __name__ == '__main__':
    print(my_reduce(lambda a, b: a + b, [1, 2]))
    print(my_reduce(lambda a, b: a + b, ["one", "two", "three"]))

    # Almost works. Take a look on results. First item duplicated
    # but should not
# -5 points
