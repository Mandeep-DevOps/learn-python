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
  print(f"Hello {f},{l}")

namePrint("john", "wesley")
namePrint(lastname="wesley", firstname="john")
