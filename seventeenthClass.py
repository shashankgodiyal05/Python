## Date - 16/01/2023

'''
    Functions
        -are used to define the process(sub program)
        -makes your code reusable
        -arranges code
        -is created by using the 'def' keyword.

        to use the function
            -define the function block
            -call the function block



    Syntax of function:-

    def functoin_name(parameters):
        process statements

        'pass' keyword is used to create an empty function

        'return' keyword is used to return the values after executing the whole function block


    Types of Functions:-
        -in built functions
        -user define functions

'''

# make a function to find out the factorial of a number
'''
def factorial():

    n = 5
    f = 1

    for x in range(n, 0, -1):
        f *= x

    print(f)

factorial()

'''

# with passing arguments
'''
def factorial1(n):

    f = 1
    for x in range(n, 0, -1):
        f *= x

    print(f)

factorial1(4)
factorial1(5)

n = int(input("Enter a number for its factorial: "))
factorial1(n)

'''

# storing the returned value in a variable or printing the result out of the funcion-
'''
def factorial2(n):

    f = 1
    for x in range(n, 0, -1):
        f *= x
    
    return f

a = factorial2(6)
print(a)

'''

# check a number is prime or not-
'''
def check_prime(num):

    for x in range(2, num):
        if num %x == 0:
            return False

    else:
        return True

print(check_prime(5))
print(check_prime(6))

'''

# find out the list of prime numbers using function and print it outside of a function-
'''
def get_prime(start, stop):

    li = []

    for x in range(start, stop + 1):

        for y in range(2, x):

            if x%y==0:
                break

        else:
            li.append(x)

    return li

print(get_prime(2, 54))

li2 = get_prime(2, 54).copy()
print(li2)

'''