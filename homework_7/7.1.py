from typing import Union, Callable, List, Dict, Tuple


def my_filter(
    callback: Callable, sequence: Union[List, Tuple, Dict]
) -> Union[List, Tuple, Dict]:
    new = []
    for element in sequence:
        if callback(element) is True:
            new.append(element)
    return new



if __name__ == '__main__':
    print(my_filter(lambda item: item > 5, [4, 5, 6, 7]))
# Good but too much empty lines in the of module.
