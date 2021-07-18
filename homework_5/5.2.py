import pickle

with open("text.txt", "rb") as file:
    byte_text = file.read()
    b_2 = pickle.loads(byte_text)
print(b_2)

for (a, d, c) in b_2:
    if c == 1:
        print(a+d)
    elif c == 2:
        print(a-d)
    else:
        print(a*d)

# Good but resolve small issues in this module
# 5.2.py:3:10: E211 whitespace before '('
# 5.2.py:8:7: E231 missing whitespace after ','
# 5.2.py:8:9: E231 missing whitespace after ','
# 5.2.py:17:1: W391 blank line at end of file

