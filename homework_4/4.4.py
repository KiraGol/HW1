import re

names = ["FirstItem", "FriendsList", "MyTuple"]
string_names = ','.join(names)
print(string_names)
string_names = re.sub(r'(?<!^)(?=[A-Z])', '_', string_names).lower()
print(string_names)
list_names = string_names.split(' ')
print(list_names)
