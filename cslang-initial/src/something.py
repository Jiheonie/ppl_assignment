print(""" " """)
print("\\\\n hello\t")

print(""" \\\\\" """)

class Animal:
  def __init__(self) -> None:
    # TODO document why this method is empty
    pass

  @classmethod
  def something(cls):
    # TODO document why this method is empty
    pass

  def make_sound(self):
    print("")

x,y,z = 3,3,4

print(id(x))
print(id(y))
print(id(z))

x,y = [1,2,3], [1,2,3]
print(id(x))
print(id(y))

def double(lst):
	if len(lst) == 0:
		return []
	i = lst[0]
	return [2*i] + double(lst[1:])

print(double([]))

def double1(lst):
	return list(map(lambda x: 2*x, lst))

print(double1([5,2,3]))