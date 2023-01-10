
## Date = 26/12/2022

    ## 5. Membership operators
        # works on the collection of the data like-
        # list, tuple, set, frozenset, range, dict (Dictionary), bytearray
        # and string.

    
    # in 

        # it checks whether the giver value exist inside the collection of the data

list1 = [3, 45, 21, 78.97]

print(3 in list1)   
# output = True

print(5 in list1)
# output = False


    # not in 

        # it work oposite to 'in', means it checks whether the given value does not
        # exist inside the collection of data.

print(3 not in list1)
# output = False

print(44 not in list1)
# output = True



    ## 6. Identity operators
        # It checks whether the two variables contains same values
        # and same memory address.
        # It works only on premitive data type.


    # is

var1 = 5
var2 = 5

print(var1 is var2)
# output = True

var2 = 6

print(var1 is var2)
# output = False

# id() function is used to check the memory address
print(id(var1), id(var2))


    # is not

print(var1 is not var2)
# output = True

var2 = 5

print(var1 is not var2)
# output = False



    ## 7. Bitwise operator
        # Operates on binary data

        # It first convert decimal to binary 
        # then operates over them
        # To show the result, it converts the data back to decimal number system

var3 = 10
var4 = 46

    # &(and)

# The binary conversion of decimal 10 :-

# +----+----+----+----+----+----+----+
# | 64 | 32 | 16 |  8 |  4 |  2 |  1 |
# +----+----+----+----+----+----+----+
# |  0 |  0 |  0 |  1 |  0 |  1 |  0 |
# +----+----+----+----+----+----+----+

# The binary conversion of decimal 46 :-

# +----+----+----+----+----+----+----+
# | 64 | 32 | 16 |  8 |  4 |  2 |  1 |
# +----+----+----+----+----+----+----+
# |  0 |  1 |  0 |  1 |  1 |  1 |  0 |
# +----+----+----+----+----+----+----+

# 10 = 001010
# 46 = 101110

# +-------+---+-------+---+---------+
# |   10  | & |   46  |   | Results |
# +-------+---+-------+---+---------+
# |   0   |   |   1   |   |    0    |
# |   0   |   |   0   |   |    0    |
# |   1   |   |   1   |   |    1    |
# |   0   |   |   1   |   |    0    |
# |   1   |   |   1   |   |    1    |
# |   0   |   |   0   |   |    0    |
# +-------+---+-------+---+---------+

# it results 001010 witch is 10 in decimal

print(var3 & var4)


    # |(or)

# +-------+-----+-------+---+---------+
# |   10  | '|' |   46  |   | Results |
# +-------+-----+-------+---+---------+
# |   0   |     |   1   |   |    1    |
# |   0   |     |   0   |   |    0    |
# |   1   |     |   1   |   |    1    |
# |   0   |     |   1   |   |    1    |
# |   1   |     |   1   |   |    1    |
# |   0   |     |   0   |   |    0    |
# +-------+-----+-------+---+---------+

# it results 101110 witch is 46 in decimal

print(var3 | var4)


    # ^(xor)

# +-----------+-------+---+---------+
# |   10  | ^ |   46  |   | Results |
# +-------+---+-------+---+---------+
# |   0   |   |   1   |   |    1    |
# |   0   |   |   0   |   |    0    |
# |   1   |   |   1   |   |    0    |
# |   0   |   |   1   |   |    1    |
# |   1   |   |   1   |   |    0    |
# |   0   |   |   0   |   |    0    |
# +-------+---+-------+---+---------+

# it results 100100 witch is 36 in decimal

print(var3 ^ var4)


    # >>(right sift)

var5 = 51

print(var5 >> 1)

# so binary conversion of decimal 51 is -

# +----+----+----+----+----+----+----+
# | 64 | 32 | 16 |  8 |  4 |  2 |  1 |
# +----+----+----+----+----+----+----+
# |  0 |  1 |  1 |  0 |  0 |  1 |  1 |
# +----+----+----+----+----+----+----+

# 51 = 0110011

# in "print(var5 >> 1)" '>>' means the least significant bit of the binary of 51 needs to shift right side
# so (var5 >> 1) means shifting the least significant bit right by 'one' place

# shifting the least significant bit right bye one place of 0110011 :-

# +----+----+----+----+----+----+----+
# | 64 | 32 | 16 |  8 |  4 |  2 |  1 |
# +----+----+----+----+----+----+----+----+
# |  0 |  0 |  1 |  1 |  0 |  0 |  1 |  1 |
# +----+----+----+----+----+----+----+----+

# now we remain with 0011001 witch is 25 in decimal.
# so the output will be 25


    # <<(legt shift)

var6 = 27

print(var6 << 1)

# so binary conversion of decimal 27 is -

# +----+----+----+----+----+----+----+
# | 64 | 32 | 16 |  8 |  4 |  2 |  1 |
# +----+----+----+----+----+----+----+
# |  0 |  0 |  1 |  1 |  0 |  1 |  1 |
# +----+----+----+----+----+----+----+

# 27 = 0011011

# in "print(var6 << 1)" '<<' means the most significant bit of the binary of 27 needs to shift left side
# so (var6 << 1) means shifting the most significant bit left by 'one' place

# shifting the most significant bit left by one place of 0011011 :-

#      +----+----+----+----+----+----+----+
#      | 64 | 32 | 16 |  8 |  4 |  2 |  1 |
# +----+----+----+----+----+----+----+----+
# |  0 |  0 |  1 |  1 |  0 |  1 |  1 |  0 |
# +----+----+----+----+----+----+----+----+

# now we remain with 0011011 witch is 54 in decimal.
# so the output will be 54


    # ~(complement)
        # - (value + 1) 

var7 = 5

print(~var7)

#output = -6
