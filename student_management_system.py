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

    def add_product(self):
        name = input("Enter product name: ").strip()

        # Duplicate product name check
        for product in self.products:
            if product.name.lower() == name.lower():
                print("Product already exists.")
                return

        category = input("Enter category: ").strip()
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        product = Product(name, category, price, quantity)
        self.products.append(product)

        print("Product added successfully.")

    def view_products(self):
        if not self.products:
            print("No products available.")
            return

        print("\nProducts\n")

        for product in self.products:
            product.display()

    def update_product(self):
        if not self.products:
            print("No products available.")
            return
        name = input("Enter product name to update: ").strip()

        for product in self.products:
            if product.name.lower() == name.lower():

                print("\n1. Update Price")
                print("2. Update Quantity")

                choice = input("Enter choice: ")

                if choice == "1":
                    product.price = float(input("Enter new price: "))
                    print("Price updated successfully.")

                elif choice == "2":
                    product.quantity = int(input("Enter new quantity: "))
                    print("Quantity updated successfully.")

                else:
                    print("Invalid choice.")

                return

        print("Product not found.")


    def sell_product(self):
        if not self.products:
            print("No products available.")
            return

        name = input("Enter product name to sell: ").strip()

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
    print("5. Exit")

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
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")