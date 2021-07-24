from typing import Union, Callable, List, Dict, Tuple


def my_reduce(callback: Callable, sequence: Union[List, Tuple, Dict]) \
        -> Union[List, Tuple, Dict]:
    iterable_data = iter(sequence)
    result = next(iterable_data)
    for element in sequence:
        result = callback(result, element)
    return result
