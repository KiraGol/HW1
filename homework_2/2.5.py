non_unique = ["Tom Smith", "Robert Lane", "John Doyle",
              "John Doyle", "Sharon French", "Tom Smith"]
unique = []

for item in non_unique:
    if item not in unique:
        unique.append(item)

print(unique)

# Good. But it can be solved in one line in python with dicts.
# Since dict contains only unique keys.
# print(list({}.fromkeys(gruppa).keys()))
