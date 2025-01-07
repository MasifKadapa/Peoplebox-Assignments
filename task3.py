def multiply_and_add(x, y):
    result = x * y
    total = result + y
    return total

def add_and_calculate(x, y):
    sum_value = x + y
    product_plus_sum = multiply_and_add(x, y)
    return sum_value, product_plus_sum
