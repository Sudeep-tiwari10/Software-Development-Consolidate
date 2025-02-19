import csv

# Function to display the inventory
def display_inventory(inventory):
    print("\nCurrent Inventory:")
    print(f"{'Product':<20}{'Quantity':<10}{'Price':<10}")
    print("-" * 40)
    for product, details in inventory.items():
        print(f"{product:<20}{details['quantity']:<10}{details['price']:<10.2f}")
    print()

# Function to add new inventory
def add_inventory(inventory):
    product_name = input("Enter the new product name: ").strip()
    if product_name in inventory:
        print(f"{product_name} already exists in the inventory. Please use the update option to modify it.\n")
    else:
        quantity = int(input(f"Enter the quantity for {product_name}: "))
        price = float(input(f"Enter the price for {product_name}: "))
        inventory[product_name] = {'quantity': quantity, 'price': price}
        print(f"{product_name} has been added successfully!\n")

# Function to update inventory
def update_inventory(inventory):
    product_name = input("Enter the product name to update: ").strip()
    if product_name in inventory:
        quantity = int(input(f"Enter the quantity to add for {product_name}: "))
        price = float(input(f"Enter the new price for {product_name}: "))
        inventory[product_name]['quantity'] += quantity
        inventory[product_name]['price'] = price  # Update the price
        print(f"{product_name} has been updated successfully!\n")
    else:
        print(f"{product_name} does not exist in the inventory. Please use the add option to create it first.\n")

# Function to save inventory to a CSV file
def save_inventory_to_file(inventory, filename="inventory.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "Quantity", "Price"])
        for product, details in inventory.items():
            writer.writerow([product, details['quantity'], details['price']])
    print(f"Inventory saved to {filename}.\n")

# Function to load inventory from a CSV file
def load_inventory_from_file(filename="inventory.csv"):
    inventory = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                product, quantity, price = row
                inventory[product] = {'quantity': int(quantity), 'price': float(price)}
        print(f"Inventory loaded from {filename}.\n")
    except FileNotFoundError:
        print(f"No previous inventory file found. Starting with an empty inventory.\n")
    return inventory

# Main Program
def main():
    inventory = load_inventory_from_file()
    
    while True:
        print("Inventory Management System")
        print("1. Display Inventory")
        print("2. Add Inventory")
        print("3. Update Inventory")
        print("4. Save Inventory to File")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            display_inventory(inventory)
        elif choice == "2":
            add_inventory(inventory)
        elif choice == "3":
            update_inventory(inventory)
        elif choice == "4":
            save_inventory_to_file(inventory)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the main program
if __name__ == "__main__":
    main()
