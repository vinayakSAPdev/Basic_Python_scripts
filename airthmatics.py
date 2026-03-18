# import math

# nums = [1, 2, 3, 4, 5]

# min_num = math.ceil(max(nums))
# print(min_num)

# # math.sqrt(nums)
# print(math.sqrt(nums[3]))

#and or operators
# a = 5
# if a > 0 and a < 10:
#     print("a is between 0 and 10")   

#is not operator
# a = 5
# if a is not None:
#     print("a is not None")

#is operator
a = [1, 2, 3]
b = a
c = b
print(c)
if a is b and a is c:
    print("a,b,c are the same object")

