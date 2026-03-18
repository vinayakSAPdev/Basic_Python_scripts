def greet(name):
    """A simple greeting function"""
    return f"Hello, {name}! Welcome to Python."

def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

def subtract_numbers(a, b):
    """Subtract two numbers and return the result"""
    return a - b

def multiply_numbers(a, b):
    """Multiply two numbers and return the result"""
    return a * b

def divide_numbers(a, b):
    """Divide two numbers and return the result"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator():
    """A simple calculator menu"""
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter your choice (1-4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {add_numbers(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract_numbers(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply_numbers(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide_numbers(num1, num2)}")
    else:
        print("Invalid choice! Please select 1-4.")

def get_favorite_numbers():
    """Get and display favorite numbers from user"""
    numbers = []
    print("\n--- Favorite Numbers ---")
    while True:
        num = input("Enter a number (or 'done' to finish): ")
        if num.lower() == 'done':
            break
        try:
            numbers.append(float(num))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    if numbers:
        print(f"Your numbers: {numbers}")
        print(f"Sum: {sum(numbers)}")
        print(f"Average: {sum(numbers) / len(numbers):.2f}")
        print(f"Max: {max(numbers)}, Min: {min(numbers)}")
    else:
        print("No numbers entered.")

# Main program
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Basic Calculator")
        print("2. Enter Favorite Numbers")
        print("3. Exit")
        option = input("Choose an option (1-3): ")
        
        if option == '1':
            calculator()
        elif option == '2':
            get_favorite_numbers()
        elif option == '3':
            print("Thank you for using this program. Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")