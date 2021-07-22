from typing import Union, Callable, List, Dict, Tuple


def my_filter(callback: Callable, sequence: Union[List, Tuple, Dict]) \
        -> Union[List, Tuple, Dict]:
    new = []
    for element in sequence:
        if callback(element) is True:
            new.append(element)
    return new



