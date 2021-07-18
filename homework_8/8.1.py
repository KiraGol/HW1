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


print(my_multiplication(3, 3))
