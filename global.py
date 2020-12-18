x=101

def myFunc():
    global x
    print(x)

    x="Hello World"
    print(x)

myFunc()
print(x)