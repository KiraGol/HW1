friends = ["John", "Marta", "James", "Amanda", "Marianna"]
print("Names".center(50,'*'))
for name in friends:
    print(name.rjust(50))

print("{:*^50}".format("Names"))
friends2 = f"John\nMarta\nJames\nAmanda\nMarianna"
for f in friends:
    print("{:>50}".format(f))

# Nice job.
