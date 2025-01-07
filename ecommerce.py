class OrderService:
    def __init__(self):
        # Initializarion of product categories with their respective items, prices, and available stock
        self.categories = {
            "Electronics": [
                {"name": "Phone", "price": 15000, "quantity": 10},
                {"name": "Laptop", "price": 50000, "quantity": 5},
                {"name": "Tablet", "price": 25000, "quantity": 8},
                {"name": "Headphones", "price": 5000, "quantity": 20},
            ],
            "Fashion": [
                {"name": "T-Shirt", "price": 500, "quantity": 30},
                {"name": "Jeans", "price": 1500, "quantity": 15},
                {"name": "Jacket", "price": 2500, "quantity": 10},
                {"name": "Shoes", "price": 3500, "quantity": 12},
            ],
            "Home": [
                {"name": "Sofa", "price": 20000, "quantity": 2},
                {"name": "Table", "price": 5000, "quantity": 5},
                {"name": "Lamp", "price": 800, "quantity": 25},
                {"name": "Curtains", "price": 1000, "quantity": 10},
            ],
            "Sports": [
                {"name": "Football", "price": 1000, "quantity": 50},
                {"name": "Tennis Racket", "price": 3000, "quantity": 8},
                {"name": "Basketball", "price": 1500, "quantity": 20},
                {"name": "Yoga Mat", "price": 700, "quantity": 15},
            ],
            "Beauty": [
                {"name": "Shampoo", "price": 400, "quantity": 50},
                {"name": "Lipstick", "price": 600, "quantity": 30},
                {"name": "Perfume", "price": 1500, "quantity": 10},
                {"name": "Moisturizer", "price": 800, "quantity": 25},
            ],
            "Books": [
                {"name": "Novel", "price": 300, "quantity": 50},
                {"name": "Magazine", "price": 100, "quantity": 100},
                {"name": "Science Book", "price": 1200, "quantity": 10},
                {"name": "Comic", "price": 250, "quantity": 40},
            ]
        }
        self.cart = []  # empty cart

    def show_categories(self):
        print("\nWelcome to our e-commerce platform!")
        print("We have the following product categories:")
        for idx, category in enumerate(self.categories, start=1):
            print(f"{idx}. {category}")

    def show_products(self, category):
        print(f"\nAvailable products in {category}:")
        for idx, product in enumerate(self.categories[category], start=1):
            print(f"{idx}. {product['name']} - ₹{product['price']} (Stock: {product['quantity']})")

    def validate_order(self, product, quantity):
        if product['quantity'] < quantity:
            print(f"Sorry, only {product['quantity']} of {product['name']} are available.")
            return False
        return True

    def update_stock(self, product, quantity):
        product['quantity'] -= quantity

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.cart)
        tax = total * 0.12  # 12% tax rate
        discount = 0
        
        # Apply discount based on the total price of the cart
        if total >= 2000:
            discount = total * 0.10
        elif total >= 1000:
            discount = total * 0.05
        
        final_total = total + tax - discount
        return total, tax, discount, final_total
    
    def preview_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("\nYour cart items:")
        for item in self.cart:
            print(f"{item['name']} (x{item['quantity']}): ₹{item['price'] * item['quantity']}")
    
    def modify_cart(self):
        while True:
            self.preview_cart() 
            try:
                modify_choice = int(input("\nWould you like to modify your cart? (1 for Yes, 0 for No): "))
                if modify_choice == 1:
                    product_name = input("Enter the product name you want to modify: ")
                    quantity = int(input(f"Enter new quantity for {product_name}: "))
                    # update the quantity
                    for item in self.cart:
                        if item['name'] == product_name:
                            item['quantity'] = quantity
                            print(f"Updated quantity of {product_name} to {quantity}.")
                            return
                    print("Product not found in cart.")
                elif modify_choice == 0:
                    return
                else:
                    print("Invalid input. Please enter 1 for Yes or 0 for No.")
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")

    def process_order(self):
        while True:
            self.show_categories()  

            try:
                category_idx = int(input("\nSelect a category by number (or type 0 to finish): ")) - 1
                if category_idx == -1:  
                    break
                category = list(self.categories.keys())[category_idx]
            except (ValueError, IndexError):
                print("Invalid selection. Please choose a valid category.")
                continue

            self.show_products(category) 
            
            while True:
                try:
                    product_idx = int(input(f"\nSelect a product to buy from {category} by number (or type 0 to go back): ")) - 1
                    if product_idx == -1:  # backtract to category
                        break
                    selected_product = self.categories[category][product_idx]
                    
                    quantity = int(input(f"Enter quantity for {selected_product['name']}: "))
                    
                    if self.validate_order(selected_product, quantity):
                        print(f"Added {quantity} of {selected_product['name']} to your cart.")
                        self.cart.append({"name": selected_product['name'], "price": selected_product['price'], "quantity": quantity})
                        self.update_stock(selected_product, quantity)
                    else:
                        print(f"Sorry, we don't have enough stock for {selected_product['name']}.")

                except (ValueError, IndexError):
                    print("Invalid selection. Please try again.")
                    continue

        # Cart preview and modify
        while True:
            self.preview_cart()
            modify_choice = input("\nWould you like to modify your cart or proceed to checkout? (modify/proceed): ").lower()
            if modify_choice == "modify":
                self.modify_cart()  #modify the cart
            elif modify_choice == "proceed":
                break  #Proceed to checkout
            else:
                print("Invalid option. Please type 'modify' or 'proceed'.")

        continue_shopping = input("\nWould you like to continue shopping or finish your order? (continue/finish): ").lower()
        if continue_shopping == "continue":
            self.process_order()  # Recursively call to continue
        else:
            # Calculating the total, taxes, discounts, and print the receipt
            total, tax, discount, final_total = self.calculate_total()
            self.print_receipt(total, tax, discount, final_total)
            print("\nThank you for shopping with us!")

    def print_receipt(self, total, tax, discount, final_total):
        #Generate and print the final receipt
        print("\n---- Order Receipt ----")
        for item in self.cart:
            print(f"{item['name']} (x{item['quantity']}): ₹{item['price'] * item['quantity']}")
        
        print(f"\nTotal price: ₹{total}")
        print(f"Tax (12%): ₹{tax}")
        print(f"Discount: -₹{discount}")
        print(f"\nFinal Total: ₹{final_total}")
        print("\n---- Thank you for your order! ----")
        
order_service = OrderService()
order_service.process_order()
