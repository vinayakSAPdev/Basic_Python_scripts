#Lambda Functions
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# The syntax of a lambda function is:
# lambda arguments: expression
# Example of a lambda function that adds two numbers:
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
# Example of a lambda function that squares a number:
square = lambda x: x ** 2  
print(square(4))  # Output: 16
# Example of a lambda function that checks if a number is even:
is_even = lambda x: x % 2 == 0
print(is_even(5))  # Output: False
print(is_even(4))  # Output: True


# few more examples of lambda functions
# Example of a lambda function that finds the maximum of two numbers:
maximum = lambda x, y: x if x > y else y
print(maximum(5, 3))  # Output: 5
# Example of a lambda function that sorts a list of tuples based on the second element:
sort_by_second = lambda lst: sorted(lst, key=lambda x: x[1])
print(sort_by_second([(1, 3), (4, 1), (2, 2)]))  # Output: [(4, 1), (2, 2), (1, 3)] 
# Example of a lambda function that filters out even numbers from a list:
filter_even = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
print(filter_even([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6] 
