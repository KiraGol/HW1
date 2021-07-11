import re

names = ["FirstItem", "FriendsList", "MyTuple"]
string_names = ','.join(names)
print(string_names)
string_names = re.sub(r'(?<!^)(?=[A-Z])', '_', string_names).lower()
print(string_names)
list_names = string_names.split(' ')
print(list_names)

# Almost works so take a look on alternative solution:
# some_list = ["FirstItem", "FriendsList", "MyTuple"]
# new_list = []
# for str_ in some_list:
#     new_list.append(re.sub('(?!^)([A-Z]+)', r'_\1', str_).lower())
# -2 point