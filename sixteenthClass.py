## Date - 12/01/2023




    ### List Comprehension


li1 = [1, 2, 3, 4, 5, 6]

li2 = [ x**2  for x in li1 ]
#       ____  ____________
#        /         \
#       /           \
#   Operation        \
#                   Loop

print(li2)


    # if statement

li3 = [ x**2  for x in li1  if x <= 3 ]
#       ____  ____________  _________
#        |          |           |
#        |          |           |
#    Operation      |           |
#                 Loop          |
#                               |
#                      Flow control statement

print(li3)


    # if else

li4 = [ x**2  if x <= 3  else x**3  for x in li1 ]
print(li4)


    # nested for loop

li5 = [[1, 2, 3], [4, 5, 6]]

li6 = [ y**2  for x in li5  for y in x ]
print(li6)

li7 = [ [ y**2  for y in x ]  for x in li5 ]
print(li7)


# 3 * 4 * 6   '*' 3D list-

li8 = [ [ [ "*"  for x in range(6) ]  for x in range(4) ]  for x in range(3) ]
print(li8)





    ### Dictionary Comprehension

d1 = { x : x**2  for x in range(1, 4) }
print(d1)

d2 = { x : x**2  for x in range(1, 11)  if x%2!= 0 }
print(d2)

d3 = { x : x**2  if x%2!=0 else x**3  for x in range(1, 11) }
print(d3)