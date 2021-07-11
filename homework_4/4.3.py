string1 = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             "
string2 = string1.rstrip(' ')
print(string2)
string3 = string2.lstrip(' ')
print(string3)
pairs = string3.split('&')
print(pairs)

# Well good but pair is list but should be dict so you should split each string by '=' one more time and take a look on maxsplit argument
# Also I notice that you have use rstrip, lstrip - you can use strip only)
# -2 points
