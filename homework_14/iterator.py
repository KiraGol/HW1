class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index < len(self.__sequence) and self.__start_index <= self.__end_index:
            item = self.__sequence[self.__start_index]
            self.__start_index += 1
            return item
        else:
            raise StopIteration


if __name__ == '__main__':
    custom_iterator = CustomIterator([1, 2, 3, 4, 5, 6, 7, 8], 1, 4)
    iterator = iter(custom_iterator)
    for item in custom_iterator:
        print(item)
    # Well done but take a look on condition in next
    # I have add some modification and it is works now but -2 points
