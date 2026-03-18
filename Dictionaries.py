# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

from typing import ItemsView, ValuesView


thisdict = [{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  },
  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}]
print(thisdict[0])

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


# Accssing the Items

x = thisdict.get("model")
x = thisdict["model"]

# keys will return all the keys
x = thisdict.keys() 

# same for getting the ValuesView
x = thisdict.values()

# The items() method will return each item in a dictionary, as tuples in a list.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)


# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#deleting item in dictionary
d = {"a": 1, "b": 2}

del d["a"]

print(d)   # {'b': 2}

# Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

d = {"name": "Vinayak", "age": 25}
for k, v in d.items():
    print(k, v)

nums = [1, 2, 2, 3, 3, 3]
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1
print(freq)


text = "ai is future ai is powerful"

words = text.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1
print(count)

# Group Anagrams (Interview 🔥)
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = {}
for word in words:
    key = "".join(sorted(word))   
    if key not in anagrams:
        anagrams[key] = []   
    anagrams[key].append(word)

print(anagrams.values())

# Find most frequent word
sentence = "machine learning is fun and learning is powerful"

words = sentence.split()
freq = {}

# Step 1: Count frequency
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Step 2: Find max frequency word
max_word = None
max_count = 0

for word, count in freq.items():
    if count > max_count:
        max_count = count
        max_word = word

print("Most frequent word:", max_word)
print("Count:", max_count)

# Problem 2: First Unique Character
s = "leetcode"
uniquech = {}

for ch in s:
    uniquech[ch] = uniquech.get(ch,0) + 1
for i, ch in enumerate(s):
    if uniquech[ch] == 1:
        print("Index:", i)
        break

#square numbers in list
# nums = [1, 2, 3, 4, 5]
squared = {num: num**2 for num in range(1, 6)}
print(squared)

