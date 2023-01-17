## Date - 17/01/2023


    ## Keyword argument:

'''
def display(a, b, c):
    print(a, b, c)

display(12, 13, 15)

'''

'''
def display1(a, b, c):
    print("a =", a, "b =", b, "c =", c)

display1(a=15, c=12, b=11)

'''


    ## Default parameters:

'''
def display2(a, b = 0):
    print("a =", a, "b =", b)

display2(4)
display2(4, 8)

'''

    ## Arbitrary arguments:

'''
def func(*param):
    print(param)

func(2, 3, 4, 5)
func(5, 6, 8)
func()

'''

    ## Arbitrary keyword arguments:

'''
def func1(**param):
    print(param)

func1(a = 5, b = 6, c = "Cat")
func1(d = "dog", e = 8)
func1()

'''
'''
    lambda function:
        -unnamed function
        -anonymous function
        -one liner statement
        -need not to return the value manually, it automaticaly returns the value 
        
'''

'''
x = lambda : print("This is a lambda function.")
x()

y = lambda a, b : a + b
print(y(4,6))

'''

    ## Properties of funtion:

        # 1. Functions can be copied

'''
def factorial(n):

    f = 1
    for x in range(n, 0, -1):
        f *= x
    
    return f

print(factorial(6))

a = factorial
print(a(5))

'''

        # 2. Nested functions

'''
def outer():

    def inner():
        print("Inner function ran")

    print("Outer function ran")
    inner()

outer()



def outer1():

    def inner1():
        print("Inner funcrion ran")

    print("Outer function ran")
    return inner1

outer1()

x = outer1()
x()

'''

    ## Recursion
        # -function call itself

'''
def func(n):

    if n >= 1:

        print(n, "function")
        func(n - 1)

func(10)

'''