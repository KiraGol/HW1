list_1 = [1, 2, 3, 4, 5, 6, 7, 8]

chet = []
nechet = []
for index in range(len(list_1)):
    if index % 2 == 0:
        chet.append(index)
    else:
        nechet.append(index)
print(chet)
print(nechet)