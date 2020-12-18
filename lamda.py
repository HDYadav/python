""" x= lambda b,c : b * c
print(x(2,20)) """

def myfunc(n):
    return lambda a: a * n
doubler = myfunc(2)
print(doubler(10))