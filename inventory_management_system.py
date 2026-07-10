import json

class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ₹{self.price}")
        print(f"Quantity: {self.quantity}")
        print("-" * 30)


class InventoryManagementSystem:
    def __init__(self):
        self.products = []
        self.load_products()

    def save_products(self):
        data = []

        for product in self.products:
            data.append({
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "quantity": product.quantity
            })

        try:
            with open("inventory.json", "w") as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            print("Error saving inventory:", e)


    def load_products(self):
        try:
            with open("inventory.json", "r") as file:
                data = json.load(file)

                for item in data:
                    self.products.append(
                        Product(
                            item["name"],
                            item["category"],
                            item["price"],
                            item["quantity"]
                        )
                    )

        except FileNotFoundError:
            pass

        except json.JSONDecodeError:
            print("Invalid inventory file.")
            self.products = []


    def search_product(self):
        if not self.products:
            print("No products available.")
            return

        while True:
            name = input("Enter product name: ").strip()

            if name:
                break

            print("Product name cannot be empty.")

        for product in self.products:
            if product.name.lower() == name.lower():
                print("\nProduct Found\n")
                product.display()
                return

        print("Product not found.")


    def add_product(self):
        while True:
            name = input("Enter product name: ").strip()

            if name:
                break

            print("Product name cannot be empty.")
        
        for product in self.products:
            if product.name.lower() == name.lower():
                print("Product already exists.")
                return

        
        while True:
            category = input("Enter category: ").strip()

            if category:
                break

            print("Category cannot be empty.")

        while True:
            try:
                    price = float(input("Enter price: "))

                    if price <= 0:
                        print("Price must be greater than 0.")
                        continue

                    break

            except ValueError:
                print("Invalid price.")
        
        while True:
            try:
                    quantity = int(input("Enter quantity: "))

                    if quantity < 0:
                        print("Quantity cannot be negative.")
                        continue

                    break

            except ValueError:
                print("Invalid Quantity.")

        product = Product(name, category, price, quantity)
        self.products.append(product)
        self.save_products()

        print("Product added successfully.")


    def view_products(self):
        if not self.products:
            print("No products available.")
            return
        
        print(f"\nTotal Products: {len(self.products)}\n")
        print("\nProducts\n")

        for product in self.products:
            product.display()

    def update_product(self):
        if not self.products:
            print("No products available.")
            return
        
        while True:
            name = input("Enter product name to update: ").strip()

            if name:
                break

            print("Product name cannot be empty.")

        for product in self.products:
            if product.name.lower() == name.lower():

                print("\n1. Update Price")
                print("2. Update Quantity")

                choice = input("Enter choice: ")

                if choice == "1":
                    while True:
                        try:
                            product.price = float(input("Enter new price: "))

                            if product.price <= 0:
                                print("Price must be greater than 0.")
                                continue

                            break

                        except ValueError:
                            print("Invalid price.")

                    self.save_products()
                    print("Price updated successfully.")

                elif choice == "2":
                    while True:
                        try:
                            product.quantity = int(input("Enter new quantity: "))

                            if product.quantity < 0:
                                print("Quantity can not be negative.")
                                continue

                            break

                        except ValueError:
                            print("Invalid Quantity.")

                    self.save_products()
                    print("Quantity updated successfully.")

                else:
                    print("Invalid choice.")

                

                return

        print("Product not found.")


    def sell_product(self):
        if not self.products:
            print("No products available.")
            return

        while True:
            name = input("Enter product name to sell: ").strip()

            if name:
                break

            print("Product name cannot be empty.")

        for product in self.products:
            if product.name.lower() == name.lower():

                print(f"Current Stock: {product.quantity}")

                try:
                    quantity = int(input("Enter quantity to sell: "))
                except ValueError:
                    print("Please enter a valid quantity.")
                    return

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    return

                if quantity > product.quantity:
                    print("Insufficient stock.")
                    return

                product.quantity -= quantity

                self.save_products()

                print(f"{quantity} unit(s) sold successfully.")
                print(f"Current Stock: {product.quantity}")

                return

        print("Product not found.")        


system = InventoryManagementSystem()

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Sell Product")
    print("5. Search Product")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.add_product()

    elif choice == "2":
        system.view_products()

    elif choice == "3":
        system.update_product()

    elif choice == "4":
        system.sell_product()

    elif choice == "5":
        system.search_product()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")