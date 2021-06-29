bigno_blacklist = {"Tom Smith", "Jacob Carr", "Sharon French", "Charles Short"}
poker_blacklist = {"Gilbert Ramsey", "Robert Lane", "John Doyle",
                   "Meryl White", "Sharon French", "Tom Smith"}
majong_blacklist = {"Sharon French", "Tom Smith", "Frank Berry"}
print(bigno_blacklist.intersection(poker_blacklist, majong_blacklist))