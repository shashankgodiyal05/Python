
## Date = 14/12/2022


## Non Primitive Data types-

# 1. List 

    # It can store all type af data- primitive and non primitive
    # It is a mutable collection means the data in it can be changed
    # Its assigns every data member a Index no. which starts from 0, its called indexing

var1 = [34, 44.53, 24 + 5j, 'r', b"python"]

print(var1)
print(type(var1))
print(var1[0])

    # It also supports -ve indexing

# 2. Tuple

    # Tuple is an immutable collection of data means we can not perform any operation on the data stored in it

var2 = (34, 44.53, 24 + 5j, 'r', b"python")

print(var2)
print(type(var2))
print(var2[3])

# 3. Range 

    # Range stores numeric integer values in a sequence 
    # It is immutable

var3 = range(1, 1001, 1)
#           /     |    \
#          /      |     \
#         /       |      \
# Starting From   |   Step Size
#                 |
#             Ending + 1

# len() is used to check the length of the variable
print(len(var3))
print(var3[3])

# 4. Set

    # It store the collection of non sequential, unique data which is immutable

set1 = {2, 34.778, "python", 45 + 7j}

    # It is a mutable and it can not store itself means a set can not store another set init
    # It does not have index no.

print(set1)

# 5. Frozenset

    # It is immutable
    # To create a frozenset we have to first make a set then convert it into the frozenset

fs = frozenset(set1)
print(fs)

# 6. Dictionary 

    # It is immutable 
    # It is a combination of key and value

dictionary1 = {'a' : "apple", 'b' : "ball"}
#              /       T       T       \
#             /        |       |        \
#           Key      Value    Key      Value

print(dictionary1)

    # we can also access the data through indexing but we use key instead of index no.

print(dictionary1["a"])
# We can put same values inside the multiple key but keys can not be repeated.

# 7. Bytearray 

    #Immutable

ba = bytearray([43,65,98,59])
print(ba)
