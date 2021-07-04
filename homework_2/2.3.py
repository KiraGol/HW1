vegetarians = ["Tom Smith", "Jacob Carr", "Sharon French", "Charles Short"]
omnivores = ["Gilbert Ramsey", "Robert Lane", "John Doyle", "Tom Smith"]

new = []
new.extend(vegetarians)
new.extend(omnivores)
print (new)

vegetarians.extend(omnivores)
print(vegetarians)

# Good. But you have extend existing group of people. I can think that all
# omnivores start to be vegetarians
