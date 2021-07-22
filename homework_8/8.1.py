def name_of_func(func):
    """shows the name of the function and the result of the operation"""

    def inner(*args, **kwargs):
        func_name = str(func.__name__)
        return f"{func_name} : {func(*args, **kwargs)}"

    return inner


@name_of_func
def my_sum(left_operand: int, right_operand: int):
    return left_operand + right_operand


print(my_sum(2, 2))


@name_of_func
def my_multiplication(left_operand: int, right_operand: int):
    return left_operand * right_operand


print(type(my_multiplication(3, 3)))

# Well good code but your decorator brake logic. I am expecting that function
# will return result looking on my sum or my multiplication. But I am
# getting string instead

# -3 points
