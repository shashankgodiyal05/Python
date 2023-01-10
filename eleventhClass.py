
## Date - 03/01/2023

    ## String:
        # sequence of characters

a = 'python'
print(a)

b = "python"
print(b)

c = """mera naam 'Sinchan' hai me shararat se bhara,
    badi mushkil me padi meri family nohara,
    come on baby, come on baby aao kare danc suru, 
    joor se ghoome ham tum jhume naacho naccho, 
    dekho sabko hasa de, oooooooooohhhhhhhh! Shinchan"""

print(c)

d = "python programming"
print(d)

# length function ( len() )
print(len(d))
# output will be the number of characters present in 'd' string

# iterating string
for x in d:
    print(x)

# extracting data through index no.
print(d[5])

# through -ve indexing 
print(d[-4])

# string slicing
print(d[0:6:1])
# print keyword, d - name of the string, [ 0 - starting index no. of string : 6 - till print : 1 - step size ]


#                                 Positive Indexing
#                                        |
#                                        |
# +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
# |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11 |  12 |  13 |  14 |  15 |  16 |  17 |
# +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
# |  p  |  y  |  t  |  h  |  o  |  n  | ' ' |  p  |  r  |  o  |  g  |  r  |  a  |  m  |  m  |  i  |  n  |  g  |
# +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
# | -18 | -17 | -16 | -15 | -14 | -13 | -12 | -11 | -10 |  -9 |  -8 |  -7 |  -6 |  -5 |  -4 |  -3 |  -2 |  -1 |
# +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
#                                        T
#                                        |
#                                 Negetive Indexing


# negetive string slicing
print(d[-18: -12 : 1])

print(d[-11: ])

print(d[: 6: -1])
#     ^
#     |
# string reversal
#     |
#     v
print(d[: :-1])

print(d[-1:])

print(d[:-1])

print(d[3:-3])


    ## Operation on string data:

# 1. Concatination of two or more string

e = "python " + "Programming"
print(e)

# 2. Multiplication of string with integers

f = "echo " * 4
print(f)

# 3. Comparision between two string

g = 'a'
h = 'z'

print(g > h)
