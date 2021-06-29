list_1 = [1, 2, 3, 4, 5, 6, 7, 8]  # I suppose will be better to name it like numbers

chet = []  # I suppose will be better to name it like even
nechet = []  # I suppose will be better to name if like odd

for index in range(len(list_1)):  # you should use foreach loop instead of for loop
    if index % 2 == 0:
        chet.append(index)
    else:
        nechet.append(index)
print(chet)
print(nechet)

# I sugest to look on list method index of build in function enumerate
# Try something like this:
# enumerate(some_list)  # will return object which could be iterated and you able to unpack it to some pair with index and value
# for some_integer_generated_by_enumerate_func, list_element in enumerate(list_1):
#     print(some_integer_generated_by_enumerate_func, list_element)
# Or
# some_list.index(some_value_which_need_to_find)
# Method append is able to add any object into the list. So it could be something like this:
# some_list.append([key, value])
# and as you understand same possible with tuple and you able to add tuple as element.
