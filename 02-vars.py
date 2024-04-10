x = 10 # integer
y = 10.5 # float
s = "DevOps" # string
# single or double quote can be used

# booleans
b = True
c = False

# List
l = [ 1, 2, "hello", True]
# list can have different values with different data types.

# Map
m = {"course" : "DevOps", "timings": "6am"}

# All the above variables are mutable

# Immutables are Tuple
t = (1,2,3)

# Sets
s = {1,2,3,3}

print(s)
print(x)
print(l[0])
print(m["course"])
print(t[2])

#print("Value in Tuple - " + t[2] )
print("Value in Tuple - " + str(t[2]) )
print(f"Value in Tuple - {t[2]}" )
print(f"course name - {m['course']}")

fruits = ["apple", "banana"]
print(fruits)
fruits.append("orange")
print(fruits)

print(m)
m["fee"] = 100
print(m)

#t[3] = 110

print(l[1:3])
print(l[:3])

multiline = """Line1
Line2
"""
print(multiline)