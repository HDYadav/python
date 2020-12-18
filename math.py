from math import sqrt
import calendar as cal

print(sqrt(25))


print(cal.month_name[5])  

# process of declear the empty class or functions 
class my_class:
    pass 

 
def sum(a,b):
    c= a + b
    return c

print("sum of A + B is: ", sum(5,10))


def outside_function():  
    a = 20   
    def inside_function():  
        nonlocal a  
        a = 30  
        print("Inner function: ",a)  
    inside_function()  
    print("Outer function: ",a)  
outside_function() 



