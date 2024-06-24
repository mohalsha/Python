# Task 1

message = "Python"
Greeting = "Hello " + message + "!"
print(Greeting)

# Task 2

a = 5
b = "10"
addition = a + int(b)
print(addition)
concatenation = str(a) + b
print(concatenation)

# Task 3

email = "python_dev@estarta.com"
domain = email[11:]
print(domain)

# Task 4

cars = ["Toyota", "Mercedes", "BMW", "Jeep"]
cars.append("Honda")
cars[1] = "Ford"
cars.remove("Toyota")
print(cars)

# Task 5

person = {"name": "Ahmad", "age": 25, "occupation": "doctor", "country": "Jordan"}
person["city"] = "Amman"
person["occupation"] = "Sugreon"
del person["country"]
print(person)

# Task 6

numbers = {2, 5, 16, 8, 7, 9, 3, 1}
print( 4 in numbers)
numbers.add(5)
numbers.remove(3)
numbers.add(16)
m = max(numbers)
new_numbers = {m+1, m+2, m+3, m+4, m+5, m+6, m+7, m+8, m+9, m+10}
all_numbers = numbers.union(new_numbers)
print(numbers)
print(new_numbers)
print (all_numbers)