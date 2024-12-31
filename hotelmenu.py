# Define the menu of the restaurant
menu = {
    "Pizza": 440,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80
}

# Greet the customer
print("Welcome to PythonAnywhere.com Restaurant")

# Display the menu
print("\nHere is the menu:")
print("Pizza: ₹440")
print("Pasta: ₹50")
print("Burger: ₹60")
print("Salad: ₹70")
print("Coffee: ₹80")

# Initialize the total order amount
order_total = 0

# Get the first item the customer wants to order
item1 = input("Enter the name of the item you want to order: ")

# Check if the first item is in the menu
if item1 in menu:
    # Add the price of the first item to the total order amount
    order_total += menu[item1]
    print(f"Your order of {item1} has been added.")
else:
    print(f"Sorry, {item1} is not available.")

# Ask the customer if they want to add another item
another_order = input("Do you want to add another item? (yes/no): ")

# If the customer wants to add another item
if another_order.lower() == "yes":
    # Get the second item the customer wants to order
    item2 = input("Enter the name of the second item you want to order: ")

    # Check if the second item is in the menu
    if item2 in menu:
        # Add the price of the second item to the total order amount
        order_total += menu[item2]
        print(f"Your order of {item2} has been added.")
    else:
        print(f"Sorry, {item2} is not available.")

# Display the total order amount
print(f"\nThe total amount of your order is: ₹{order_total}")