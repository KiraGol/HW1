import os
import pickle
import random
b = [(random.randint(1, 100), random.randint(1, 100), random.randint(1, 3))
     for i in range(100)]
print(b)

os.makedirs("test/data")

print(os.getcwd())
os.chdir("test/data")
print(os.getcwd())


my_file = open("text.txt", "w")
my_file.close()

with open("text.txt", "wb") as file:
    text = pickle.dumps(b)
    file.write(text)
# well since I am using Ubuntu it will not work on my end.
# So you have to rewrite it with relative path.
# Good but it make not sence to open file for writting and close
# it in next line)

# Resolve this issues in this module
# 5.1.py:4:23: E231 missing whitespace after ','
# 5.1.py:4:46: E231 missing whitespace after ','
# 5.1.py:4:69: E231 missing whitespace after ','
# 5.1.py:11:80: E501 line too long (80 > 79 characters)
# 5.1.py:18:10: E211 whitespace before '('
