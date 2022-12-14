## Date = 12/12/2022

## Rules to define the variable name:-
    # Variable name should contain alphabets, numbers, underscore(_)
    # Variable name's first letter must not be a number
    # Variable name must be reasonable

    # abc132, _abs, asf, cag_45 are all valid variable names
    # 123abc, 1_las are all invalid variable names

## input() - this function is used to take input from the user
# we put required instruction in between (" ")
# by default it treat input as string
# int(input()) is used to take integer type of data

var1 = int(input("Enter the first number: "))
print("You entered ", var1)

var2 = int(input("\nEnter the first number: "))
print("You entered ", var2)

print("\nAddition of var1 and var2 is ", var1 + var2)
print("\nSubstraction of var1 and var2 is ", var1 - var2)

## Data Types:-

    ## Primitive Data Types-
        # 1. int (Integer)
        # 2. float
        # 3. complex (2 + 7j type)
        # 4. bool (Boolean)
        # 5. str (String)
        # 6. bytes 
    # (We can not define a data into bytes but we can convert the other types of data into bytes)

    ## Non Primitive Data Types-
        # 1. list
        # 2. tuple
        # 3. set
        # 4. frozenset
        # 5. range
        # 6. dict (Dictionary)
        # 7. bytearray

    
var3 = 58	# Integer(int)
print("\nThe type of var3 is", type(var3))

var4 = 51.65	# Float(float)
print("\nThe type of var4 is", type(var4))

var5 = 2 + 7j	# Complex no.(complex)
print("\nThe type of var5 is", type(var5))

var6 = True    # Boolean(bool)
print("\nThe type of var6 is", type(var6))

var7 = "Hello frands chai pi lo"	# String(str)
print("\nThe type of var7 is", type(var7))

var8 = b"python"	#Bytes(byte)
print("\nThe type of var8 is", type(var8))

# to check the type of data stored in the variable we use:-
# print(type(variable_name))
