## Date = 19-12-2022

#### Operators-
    # Symbols used to perform operations on data.



    ## 1. Arithmatic operators:-

var1 = 45
var2 = 5

# +
print(var1+var2)

# -
print(var1-var2)

# *
print(var1*var2)

# /
print(var1/var2)

# %
print(var1%var2)

# ** (** = ^)
print(var1**var2)

# // (floor division)
print(var1//var2)


    ## 2. Assignment operators:-

# = 
var3 = 26
var4 = 58

# +=
var4 += var3 
# it means var4 = var4 + var3
print(var4)

# -=
var4 -= var3
# it means var4 = var4 - var3
print(var4)

# *=
var4 *= var3
# it means var4 = var4 * var3
print(var4)

# /=
var4 /= var3
# it means var4 = var4 / var3
print(var4)

# %=
var4 %= var3
# it means var4 = var4 % var3
print(var4)

# **= 
var4 **= var3
# it means var4 = var4 ** var3
print(var4)

# //=
var4 //= var3
# it means var4 = var4 // var3
print(var4)


    ## 3. Comparision operators:-
        # It gives boolean value (true or false) as an output of the operation

var5 = 24
var6 = 40

# < (less then)
print(var5<var6)

# > (grater then)
print(var5>var6)

# <= (less then or equals to)
print(var5<=var6)

# >= (grater then or equals to)
print(var5>=var6)

# == (equality check, if the value of both the variables are same then it will print true otherwise false)
print(var5==var6)

# != (inequality check, if the value of both the variables are not same then it will print true otherwise false)
print(var5!=var6)



    ## 4. Logical operations:-
        # It works over the boolean values

# and

    # truth table of and 
    # true and true = true
    # true and false = false
    # false and false = false
    # false and true = false

var7 = 47
var8 = 62
var9 = 31

print(var7 > var8 and var9 < var8)
#    (___________)   (___________)
#         |                      \
#         |                       \
#1. First this will get solved     \
#(this portion will result false)   \
#                                    \
#                       2. Then this will get solved
#                       (this portion will result true)
#
# now 'and' operator will perform operation on the results of point (1) and (2)
# it will result false since we know from the truth table of and that false and true is false

# or

    # truth table of or 
    # true or true = true
    # true or false = true
    # false or false = false
    # false or true = true

print(var7 > var8 or var9 < var8)
#    (___________)  (___________)
#         |                     \
#         |                      \
#1. First this will get solved    \
#(this portion will result false)  \
#                                   \
#                       2. Then this will get solved
#                       (this portion will result true)
#
# now 'or' operator will perform operation on the results of point (1) and (2)
# it will result true since we know from the truth table of or that false or true is true

# not
    # It reverse the boolean value of any comparision operations

print(not(var7 > var8))
# (var7 > var8) will result false but the 'not' operator will the reverse the output to true
