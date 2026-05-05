# def my_function(a,b):
#   print(f"sum of two numbers are {a+b}")

# my_function(4,2)

# # find even numbers in list by function
# def find_even_numbers(num_list):
#     even_numbers = []
#     for num in num_list:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers

# def findSmallestnumber(num_List):
#     if not num_List:
#         return None
#     smallest = num_List[0]
#     for num in num_List:
#         if num < smallest:
#             smallest = num
#     return smallest 
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = find_even_numbers(numbers)
# print(even_numbers)
# smallestnumber = findSmallestnumber(even_numbers)
# print(smallestnumber)


# #Move Zeros
# def move_zeros(nums):
#     non_zero_index = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[non_zero_index] = nums[i]
#             non_zero_index += 1
#     for i in range(non_zero_index, len(nums)):
#         nums[i] = 0
#     return nums
# nums = [0, 1, 0, 3, 12]
# result = move_zeros(nums)
# print(result)  # Output: [1, 3, 12, 0, 0]

# #create a list of dictionaries with products and their name, price and quantity, category
# products = [
#     {"name": "Laptop", "price": 999.99, "quantity": 10, "category": "Electronics"},
#     {"name": "Smartphone", "price": 499.99, "quantity": 20, "category": "Electronics"},
#     {"name": "Book", "price": 19.99, "quantity": 50, "category": "Books"},
#     {"name": "Headphones", "price": 199.99, "quantity": 15, "category": "Electronics"},
#     {"name": "Coffee Mug", "price": 9.99, "quantity": 100, "category": "Home & Kitchen"}
# ]
# butoptions = ["Buy Product","Exit"]

# print("Select Product Category:")
# categories = set(product["category"] for product in products)
# for i, category in enumerate(categories):
#     print(f"{i}. {category}")
# category_choice = int(input("Enter category number: "))
# selected_category = list(categories)[category_choice]
# products_in_category = [product for product in products if product["category"] == selected_category]
# names = set(product["name"] for product in products_in_category)
# print("Select Product Name:")
# for i, name in enumerate(names):
#     print(f"{i}. {name}")

# name_choice = int(input("Enter product number: "))
# selected_name = list(names)[name_choice]
# selected_product = next(product for product in products_in_category if product["name"] == selected_name)
# print(f"Price: {selected_product['price']}, Quantity: {selected_product['quantity']}")

# quantity_choice = int(input("Enter quantity: "))
# if quantity_choice <= selected_product["quantity"]:
#     total_price = quantity_choice * selected_product["price"]
#     print(f"Total Price: {total_price}")
# else:
#     print("Sorry, not enough stock available.")

# for i, butoption in enumerate(butoptions):
#     print(f"{i}. {butoption}")
# button_choice = int(input("Enter button number: "))
# if button_choice == 0:
#     # update inventory
#     selected_product["quantity"] -= quantity_choice
#     print("Product purchased successfully!")
#     print(f"Remaining Quantity of {selected_product['name']}: {selected_product['quantity']}")
# elif button_choice == 1:
#     print("Exiting the program.")

 
