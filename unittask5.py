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
        print(f"Test 1 Failed!")

    # Test Case 2: 0% Discount
    price = 100
    discount_percentage = 0
    expected = 0
    result = calculate_discount(price, discount_percentage)
    if result == expected:
        print("Test 2 Passed")
    else:
        print(f"Test 2 Failed!")

    # Test Case 3: 100% Discount
    price = 50
    discount_percentage = 100
    expected = 50
    result = calculate_discount(price, discount_percentage)
    if result == expected:
        print("Test 3 Passed")
    else:
        print(f"Test 3 Failed!")

    # Test Case 4: Discount on a fractional price
    price = 99.99
    discount_percentage = 15
    expected = 14.9985
    result = calculate_discount(price, discount_percentage)
    if abs(result - expected) < 0.0001:
        print("Test 4 Passed")
    else:
        print(f"Test 4 Failed!")

    # Test Case 5: Discount greater than the price
    price = 50
    discount_percentage = 150
    result = calculate_discount(price, discount_percentage)
    if result == expected:
        print("Test 5 Passed")
    else:
        print(f"Test 5 Failed!)

    # Test Case 6: Negative Price
    price = -100
    discount_percentage = 20
    result = calculate_discount(price, discount_percentage)
    if result == expected:
        print("Test 6 Passed")
    else:
        print(f"Test 6 Failed!")

    # Test Case 7: Discount Percentage Greater Than 100 (Invalid Case)
    price = 80
    discount_percentage = 200
    result = calculate_discount(price, discount_percentage)
    if result == expected:
        print("Test 7 Passed")
    else:
        print(f"Test 7 Failed!")

test_calculate_discount()
