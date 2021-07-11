import os
import pickle
import random
b = [(random.randint(1,100), random.randint(1,100), random.randint(1,3))
     for i in range(100)]
print(b)

os.makedirs("test/data")

print(os.getcwd())
os.chdir('C:\\Users\\denys\\PycharmProjects\\homework1\\homework_5\\test\\data')
print(os.getcwd())

my_file = open("text.txt", "w")
my_file.close()

with open ("text.txt", "wb") as file:
    text = pickle.dumps(b)
    file.write(text)

with open ("text.txt", "rb") as file:
    byte_text = file.read()
    b_2 = pickle.loads(byte_text)
print(b_2)

for (a,d,c) in b_2:
    if c == 1:
        print(a+d)
    elif c == 2:
        print(a-d)
    else:
        print(a*d)