global_logic = ["Tom Smith", "Jacob Carr", "Sharon French", "Charles Short"]
toshiba = ["Gilbert Ramsey", "Robert Lane", "John Doyle",
           "Meryl White", "Sharon French", "Tom Smith"]
toshiba.extend(global_logic)
list.clear(global_logic)
print(toshiba)
print(global_logic)
