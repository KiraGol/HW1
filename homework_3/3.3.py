friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]

for friend in friends:
    if friend in enemies:
        print(friend + ', we are not the friends anymore')
    elif friend in friends and friend != 'James':
        print(friend + ', we are the best friends')
# This pring is excess. Try to look on logical operators to cobine several conditions in one line.