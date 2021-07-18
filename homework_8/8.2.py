def square_of_an_even_number():
    """returns the squares of even elements for the range 0
    through 1,000,000,000, inclusive"""
    number = 0
    while number <= 1000000000:
        if number % 2 == 0:
            yield number ** 2
        number += 1


generator = square_of_an_even_number()
print(next(generator))
print(next(generator))
print(next(generator))
new_gen = (item for item in generator)
print(new_gen)
