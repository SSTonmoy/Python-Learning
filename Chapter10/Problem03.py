# Create a class with a class attribute a; create an object from it and
# set ‘aʼ directly using‘object.a = 0ʼ. Does this change the class attribute?
class apple:
    a = 69


Tiger = apple()
Tiger.a = 0
print(Tiger.a)
# yes