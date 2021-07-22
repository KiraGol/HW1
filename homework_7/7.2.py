from typing import Union, Callable, List, Dict, Tuple


def my_map(callback: Callable, sequence: Union[List, Tuple, Dict]) \
        -> Union[List, Tuple, Dict]:
    result = []
    for element in sequence:
        result.append(callback(element))
    return result