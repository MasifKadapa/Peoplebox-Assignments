def calculate_discount(price, discount_percentage):
    """Calculates the discount amount."""
    return price * (discount_percentage / 100)

def test_calculate_discount():
    # Test Case 1: Normal Case
    price = 200
    discount_percentage = 20
    expected = 40
    result = calculate_discount(price, discount_percentage)
    if result == expected:
        print("Test 1 Passed")
    else:
        print(f"Test 1 Failed: Expected {expected}, Got {result}")

    # Test Case 2: 0% Discount
    price = 100
    discount_percentage = 0
    expected = 0
    result = calculate_discount(price, discount_percentage)
    if result == expected:
        print("Test 2 Passed")
    else:
        print(f"Test 2 Failed: Expected {expected}, Got {result}")

    # Test Case 3: 100% Discount
    price = 50
    discount_percentage = 100
    expected = 50
    result = calculate_discount(price, discount_percentage)
    if result == expected:
        print("Test 3 Passed")
    else:
        print(f"Test 3 Failed: Expected {expected}, Got {result}")

    # Test Case 4: Discount on a fractional price
    price = 99.99
    discount_percentage = 15
    expected = 14.9985
    result = calculate_discount(price, discount_percentage)
    if abs(result - expected) < 0.0001:
        print("Test 4 Passed")
    else:
        print(f"Test 4 Failed: Expected {expected}, Got {result}")

    # Test Case 5: Discount greater than the price (Invalid case)
    price = 50
    discount_percentage = 150  # Invalid case
    result = calculate_discount(price, discount_percentage)
    # We check if the result makes sense in the context (if discount is overly high)
    if result >= price:
        print(f"Test 5 Passed: The calculated discount {result} is higher than the price, which is expected in case of an overly high discount percentage.")
    else:
        print(f"Test 5 Failed: Expected a discount greater than price, but got {result}")

    # Test Case 6: Negative Price (Invalid case)
    price = -100  # Invalid price
    discount_percentage = 20
    try:
        result = calculate_discount(price, discount_percentage)
        print(f"Test 6 Failed: Expected an error but got {result}")
    except ValueError:
        print("Test 6 Passed: ValueError raised for negative price.")

    # Test Case 7: Discount Percentage Greater Than 100 (Invalid case)
    price = 80
    discount_percentage = 200  # Invalid discount
    try:
        result = calculate_discount(price, discount_percentage)
        print(f"Test 7 Failed: Expected an error but got {result}")
    except ValueError:
        print("Test 7 Passed: ValueError raised for discount greater than 100.")
test_calculate_discount()
