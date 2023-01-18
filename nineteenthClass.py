# Date - 18/01/2023

'''
        Predifined Functions:

    1. map(func, *iterables) --> map object
        
        Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.

'''

tuple1 = (1, 2, 3, 4, 5)

'''
def square(n):
    return n ** 2

t = tuple(map(square, tuple1))
print(tuple1)
print(t)

'''

'''
t1 = tuple(map(lambda n : n**2, tuple1))
print(t1)

'''

tuple2 = ('a', 'b', 'c', 'd')

'''
t2 = tuple(map(str.upper, tuple2))
print(t2)

'''

'''
    2. filter(function or None, iterable) --> filter object

        Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.  

'''

'''
tuple3 = (1, 2, 3, 4, 5, 'a', 4.7, 5+7j)

def get(n):
    return isinstance(n, int) or isinstance(n, float)

t3 = tuple(filter(get, tuple3))
print(t3)

# t4 = tuple(map(lambda n : n**2, t3))
# print(t4)

'''

'''
    3. reduce(function, iterable[, initial]) -> value

        Apply a function of two arguments cumulatively to the items of a sequence or iterable, from left to right, so as to reduce the iterable to a single value. 
        For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). If initial is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty.


'''

'''
from functools import reduce

def add(a, b):
    return a + a

res = reduce(add, tuple1)
print(res)

'''