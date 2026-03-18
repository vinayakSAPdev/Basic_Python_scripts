def greet(name):
    """A simple greeting function"""
    return f"Hello, {name}! Welcome to Python."

def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

# Main program
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = add_numbers(num1, num2)
    print(f"The sum is: {result}")