class MyClass:
  x = 5
  y = 10

# Now we can use the class named MyClass to create objects:
p1 = MyClass()
print(p1.x)
print(p1.y)

#The __init__() Method
#All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
#The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
#Using __init__() makes it easier to create objects with initial values:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)  
print(p1.age)


class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

#The self Parameter
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# Without self, Python would not know which object's properties you want to access:
# class Person:
#   def __init__(name, age):
#     name.name = name
#     name.age = age
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)

class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()


class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
    self.name = "Vinayak"
    self.contactno = 1234567890
    self.gender = "Male"

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")
  
  def display_customerdetails(self):
    print(f"Customer has bought a {self.name} {self.contactno} {self.gender}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()
car1.display_customerdetails()

# calling the method using class name
 
class demoperson:
  def __init__(self, name, age, city):
    self.name = name
    self.age = age
    self.city = city

  def greet(self):
    return print("Hello, my name is " + self.name) 
  def greetwithcity(self):
    return print("Hello, my name is " + self.name + " and I am from " + self.city)
  
p1 = demoperson("Emil", 36, "Oslo")
demoperson.greet(p1)
demoperson.greetwithcity(p1)

# give me example  with real time example of class and objects
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
# Create an instance of BankAccount
account1 = BankAccount("Alice", 10000)   
account1.deposit(500)  # Deposited 500. New balance is 1500.
account1.withdraw(200) # Withdrew 200. New balance is 1300


#give me example of class and objects with real time example of a class and objects
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book}' to the library.")

    def display_books(self):
        print(f"Books in {self.name} Library:")
        for book in self.books:
            print(f"- {book}")
# Create an instance of Library
my_library = Library("City")
my_library.add_book("To Kill a Mockingbird")  # Added 'To Kill a Mockingbird' to the library.
my_library.add_book("1984")  # Added '1984' to the library.
my_library.display_books()

#give me example with _str_ and without _str_ method
# Without __str__ method
#The __str__() method is a special method that controls what is returned when the object is printed:
class Person:   
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Alice", 30)
print(p1)  # Output: <__main__.Person object at 0x7f8b8c8d0>
# With __str__ method
#Used in:
# Logging
# Debugging
# Printing objects in apps
# Data models in AI systems
class Person:   
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

p1 = Person("Alice", 30)
print(p1)  # Output: Person(name=Alice, age=30)

#inheritance in python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

#inheriting the Animal class to create Dog and Cat classes
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks: Woof! Woof!"
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} meows: Meow! Meow!"
# Create instances of Dog and Cat
dog1 = Dog("Buddy", "Golden Retriever") 
cat1 = Cat("Whiskers", "Tabby")
print(dog1.speak())  # Output: Buddy barks: Woof! Woof!
print(cat1.speak())  # Output: Whiskers meows: Meow!





