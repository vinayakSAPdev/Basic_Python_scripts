# New users

# Common users

# Total unique users

# users_app1 = {"user1", "user2", "user3"}
# users_app2 = {"user2", "user3", "user4"}

# # New users
# user_app3 = users_app2.difference(users_app1)
# print(f"new users are {user_app3}")

# # Common users
# user_app4 = users_app2.intersection(users_app1)
# print(f"common users {user_app4}")

# Common users
# user_app5 = users_app2.symmetric_difference(users_app1)
# print(f"total unique users {user_app5}")

# Total unique users
# user_app6 = users_app2.union(users_app1)
# print(f"total unique users {user_app6}")


# Problem 2: Find Common Skills (Hiring Use Case)
candidate1 = {"python", "sql", "ml"}
candidate2 = {"python", "java", "ml"}
print(f"common skills are {candidate1.intersection(candidate2)} ")

# 🟡 Problem 3: Find Missing Items (Inventory)
expected_items = {"laptop", "mouse", "keyboard", "charger"}
received_items = {"laptop", "mouse"}

print(f"missing items are {expected_items.difference(received_items)} ")

# Problem 5: Detect Fraud (Duplicate Transactions)
transactions = ["tx1", "tx2", "tx3", "tx2", "tx4", "tx1"]
seen = set()
duplicates = set()

for tx in transactions:
    if tx in seen:
        duplicates.add(tx)
    else:
        seen.add(tx)

print(duplicates)

# Problem 6: Mutual Friends (Social Network)

user1_friends = {"A", "B", "C"}
user2_friends = {"B", "C", "D"}

print(f"Mutual friends {user1_friends.intersection(user2_friends)}")

# Problem 7: Unique Words in Text (AI/NLP Use Case)
text = "python is easy and python is powerful"  
words = text.split()
unique_words = set(words)

print(unique_words)
print("Count:", len(unique_words))

# Problem 8: Check Subset (Permissions System)
required_permissions = {"read", "write"}
user_permissions = {"read", "write", "delete"}
print(required_permissions.issubset(user_permissions))

# Remove duplicates + count unique emails
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]
removeduplicate = set(emails)
print(f"removed duplicate email {removeduplicate}")
print(f"count of unique {len(removeduplicate)}")

# Check if any two numbers sum to target (hint: use set)
nums = [1, 2, 3, 4, 5]
target = 8

seen = set()

for num in nums:
    if (target - num) in seen:
        print("Pair found:", num, "and", target - num)
        break
    seen.add(num)
else:
    print("No pair found")



newset = {"apple", "banana", "cherry"}
newset1 = ["apple", "banana", "cherry"]
print(newset)
newset.add("orange")
print(newset)
print("extracted itmes are",newset.pop()    )
print(newset)
print("extracted itmes are",newset1[1:2]  )
if 'banana' in newset:
    print("banana is present in the set")
numbers = {1, 2, 3, 4, 5}
squared_numbers = {x**2 for x in numbers}
print(squared_numbers)

#tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
a,b,c = my_tuple[0:3]
print(a,b,c)

#dictionaries is like json
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)
#crete some example dictionary
person = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "traveling", "coding"],
    "education": {
        "degree": "Bachelor's",
        "major": "Computer Science",
        "university": "XYZ University"
    },
    "name": "albert",
    "age": 28,
    "city": "India",
    "hobbies": ["workout", "traveling", "swimming"],
    "education": {
        "degree": "Master's",
        "major": "AI/ML",
        "university": "XYZ555 University"
    }
}
print(person)
print(person["name"])
print(person["hobbies"])

print(person.get("education")["degree"])
person.update({"age": 26})
print(person)

for key, value in person.items():
    print(f"{key}: {value}")    


#dictionary comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict)

#explain the json model with example
import json
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "coding"],
    "education": {
        "degree": "Bachelor's",
        "major": "Computer Science",
        "university": "XYZ University"
    }
}
json_data = json.dumps(data)
print(json_data)    

#reading json data
json_string = '{"name": "Alice", "age": 30, "city": "New York", "hobbies": ["reading", "traveling", "coding"], "education": {"degree": "Bachelor\'s", "major": "Computer Science", "university": "XYZ University"}}'
data = json.loads(json_string)
print(data)

#crud operations on json data
# Create
new_data = {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles",
    "hobbies": ["music", "sports"],
    "education": {
        "degree": "Master's",
        "major": "Data Science",
        "university": "ABC University"
    }
}
json_data = json.dumps(new_data)
print(json_data)
# Read
json_string = '{"name": "Bob", "age": 25, "city": "Los Angeles", "hobbies": ["music", "sports"], "education": {"degree": "Master\'s", "major": "Data Science", "university": "ABC University"}}'
data = json.loads(json_string)
print(data)
# Update
data["age"] = 26
print(data)
# Delete
del data["city"]
print(data) 

