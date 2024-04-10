def sample():
  print('Hello Sample')

sample()


def sample1(x,y):
  print(x+y)

sample1(10,20)
sample1(30,20)

def namePrint(firstname, lastname):
  f = firstname.title()
  l = lastname.title()
  return "Hello " + f + "," + l

namePrint("john", "wesley")
namePrint(lastname="wesley", firstname="john")

name = namePrint(lastname="wesley", firstname="john")
print(name)


def sample3():
  y=20
  print(x)

x = 10
sample3()
print(y)
