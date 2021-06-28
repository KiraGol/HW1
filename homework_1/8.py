john = {
    "full_name": "John",
    "age": 35,
    "salary": 456.7,
    "gender": True,
    "friends": ["Mark", "Jack", "Jessica", "John", "James", "Jessica", "Jack"],
    "coordinates": (46.4873195, 30.7392776)
}

marta = {
    "full_name": "Marta",
    "age": 37,
    "salary": 534.89,
    "gender": True,
    "friends": ["Mark", "Jack", "Jessica", "John", "James", "Jessica", "Jack"],
    "coordinates": (46.4873195, 30.7392776)
}

for key, value in john.items():
    print(key, value, sep=" => ")

for key, value in marta.items():
    print(key, value, sep=" => ")
