print("welocme to python basics")
numberArray = [10, 20, 30, -9, 1,7,5,8,5,8]
print(numberArray)

numberArray.append(40)

# Insert element at position
numberArray.insert(1, 15)

# # Remove element
# numberArray.remove(20)

print(numberArray)

for num in numberArray:
    if num < 0:
        print(" in valid numbers",num)

# numberArray = [num * 2 for num in numberArray]

print(numberArray)

nummax = 0
for num in numberArray:
    if num > nummax:
        nummax = num

print("maximum number is",nummax)
evennum = 0
oddnum = 0
evenArray =[]
oddArray = []

for num in numberArray:
    if num % 2 == 0:
        evenArray.append(num)
    else:
        oddArray.append(num)

print(f"ther are total {len(evenArray)} even numbers and they are {evenArray}")
print(f"ther are total {len(oddArray)} odd numbers and they are {oddArray}")


#duplicate numbers 
duplicates = []

for num in numberArray:
    if numberArray.count(num) > 1 and num not in duplicates:
        print(numberArray.count(num))
        # duplicates.append(num)
        numberArray.remove(num)

print(duplicates)
print(numberArray)

# Finding the largest number in array

numberArray.sort()
numberArray = numberArray[-2]

print("Second largest number is:", numberArray)


#missing number in array
newArray = [2,3,5,6,8]
missingNum = []
print(max(newArray))
for i in range(1, max(newArray)+1):
     if i not in newArray:
        missingNum.append(i)

print(missingNum)

#Find the largest difference between two numbers in an array.
numInput =  [7,1,5,3,6,4]
numInput.sort()
print(numInput)
difnum = 0
# for i in range(len(numInput)-1):
#     diff = numInput[i+1] - numInput[i]
#     if diff > difnum:
#         difnum = diff

# numInput = [7,1,5,3,6,4]

largest_diff = max(numInput) - min(numInput)

print("Largest difference:", largest_diff)

# Remove all duplicates but keep order
Input  = [1,2,2,3,1,4]
duplicate =[]
for num in Input:
    if num not in duplicate:
        duplicate.append(num)
print(duplicate)

#Find two numbers whose sum equals the target.
numbers = [2,7,11,15]
target = 9
sumoftwonumber = []

for i in range(len(numbers)-1):
    if numbers[i] + numbers[i+1] == target:
        sumoftwonumber = [numbers[i],numbers[i+1]]
print(f"the sum of two numbers equals to target are {sumoftwonumber}")

#Return a new array where each element is the product of all other elements.
numbers2 = [1,2,3,4]
productarray = []
for i in range(len(numbers2)):
    product = 1
    for j in range(len(numbers2)):
        if i != j:
            product *= numbers2[j]
    productarray.append(product)

print(f"new array is {productarray}")

#Rotate the array k steps to the right.
numbers3 = [1,2,3,4,5,6,7]
k = 3
rotatearray = []
for i in range (len(numbers3)):
    rotatearray.append(numbers3[i-k])

print(rotatearray)

#Find common elements.
arr1 = [1,2,2,1]
arr2 = [2,2,1]
commonarray = []

for i in range(len(arr1)):
   if arr1[i] in arr2 and arr1[i] not in commonarray:
        commonarray.append(arr1[i])
print(commonarray)

#Find element appearing more than n/2 times.
numbers5 = [3,2,3]

morethanvalue = []
maxappear = len(numbers5) // 2

for num in numbers5:
    if numbers5.count(num) > maxappear and num not in morethanvalue:
        morethanvalue.append(num)

print("Majority element:", morethanvalue)
