#for loop

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
  print(f"Fruit name - {fruit}")


# while loop
i = 5
while i >0:
  print(f'Iteration - {i}')
  i = i -1

fruits = ["apple", "banana", "orange"]
print(enumerate(fruits))
for index, fruit in enumerate(fruits):
  print(f"Index - {index} Fruit name - {fruit}")


fruits = ["apple", "banana", "orange"]
quantity = [ 10, 20 , 10]

for fruit, quan in zip(fruits, quantity):
  print(f"Fruit - {fruit} Quantity - {quan}")



