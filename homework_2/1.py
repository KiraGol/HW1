global_logic = ["Tom Smith", "Jacob Carr", "Sharon French", "Charles Short"]
toshiba = ["Gilbert Ramsey", "Robert Lane", "John Doyle",
           "Meryl White", "Sharon French", "Tom Smith"]
toshiba.extend(global_logic)
print(toshiba)

# Good. But global logic employees are employees of toshiba.
# But if I will try to print global_logic I will see that some employees still
# present there.
