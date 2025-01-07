def calculate_discount(price, discount_percentage):
    """Calculates the discount amount."""
    return price * (discount_percentage / 100)

def final_price(price, discount_percentage):
    """Calculates the final price after applying the discount."""
    discount = calculate_discount(price, discount_percentage)  # Get discount amount
    return price - discount  # Subtract the discount from the original price to get the final price

def test_final_price():
    """Tests the final_price function for different cases."""

    # Test Case 1: Normal Scenario
    price = 200
    discount_percentage = 20
    expected = 160  # 200 - (20% of 200) = 160
    result = final_price(price, discount_percentage)
    if result == expected:
        print("Test 1 Passed: Final price correctly calculated.")
    else:
        print(f"Test 1 Failed: Expected {expected}, Got {result}")

    # Test Case 2: No Discount (0% discount)
    price = 100
    discount_percentage = 0
    expected = 100  # No discount, so price remains the same
    result = final_price(price, discount_percentage)
    if result == expected:
        print("Test 2 Passed: No discount, price remains unchanged.")
    else:
        print(f"Test 2 Failed: Expected {expected}, Got {result}")

    # Test Case 3: Full Discount (100% discount)
    price = 50
    discount_percentage = 100
    expected = 0  # 100% discount means the price becomes 0
    result = final_price(price, discount_percentage)
    if result == expected:
        print("Test 3 Passed: Final price is zero with a 100% discount.")
    else:
        print(f"Test 3 Failed: Expected {expected}, Got {result}")

    # Test Case 4: Fractional Price Calculation
    price = 99.99
    discount_percentage = 15
    expected = 84.9915  # 15% discount on 99.99 results in 14.9985, so the final price should be 84.9915
    result = final_price(price, discount_percentage)
    if abs(result - expected) < 0.0001:  # Allowing a small margin of error due to floating-point calculations
        print("Test 4 Passed: Final price correctly calculated for fractional price.")
    else:
        print(f"Test 4 Failed: Expected {expected}, Got {result}")

    # Test Case 5: Overly High Discount (Greater than price)
    price = 50
    discount_percentage = 150  # Overly high discount percentage
    try:
        result = final_price(price, discount_percentage)
        print(f"Test 5 Failed: Expected an exception but got {result}")
    except ValueError as e:
        # We expect the system to raise an error for this case
        print(f"Test 5 Passed: Exception correctly raised for discount greater than price. Error: {e}")

    # Test Case 6: Negative Price (Invalid case)
    price = -100  # Negative price is invalid
    discount_percentage = 20
    try:
        result = final_price(price, discount_percentage)
        print(f"Test 6 Failed: Expected an exception for negative price but got {result}")
    except ValueError as e:
        # We expect a ValueError for negative prices
        print(f"Test 6 Passed: Exception correctly raised for negative price. Error: {e}")

    # Test Case 7: Discount Percentage Greater Than 100 (Invalid case)
    price = 80
    discount_percentage = 200  # Invalid discount greater than 100%
    try:
        result = final_price(price, discount_percentage)
        print(f"Test 7 Failed: Expected an exception for invalid discount but got {result}")
    except ValueError as e:
        # We expect a ValueError for a discount percentage greater than 100
        print(f"Test 7 Passed: Exception correctly raised for invalid discount. Error: {e}")
test_final_price()

