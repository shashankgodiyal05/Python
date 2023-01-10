## Date - 28/12/2022

    # Breaking the loop( break )

a = 1

while a <= 10:
    print("a =", a)
    
    if a == 5:
        break

    a +=1

print("\n\n")


    # Skipping the loop iteration( continue )

b = 1

while b <= 10:
    b +=1
    if b == 5:
        continue

    print("b =", b)
    
print("\n\n")


    # else block with while loop

        # doesnt work with break statement
        # runs when the condition at while gets false.

c = 1

while c <= 8:
    print(c)

    c += 1

else:
    print("While block got terminated. ")


d = 1

while d <= 8:
    print(d)
    
    if d == 5:
        break

    d += 1

else:
    print("While block got terminated when the value of d is", d)

## else block does not work with break statement.

e = 1

while e <= 8:
    e += 1
    
    if e == 5:
        continue

    print("e =",e)

else:
    print("While block got terminated when the value of d is", e)


    ## Nested while loop

f = 1

while f <= 3:
    print("f =", f)
    g =1

    while g <= 3:
        print("\tg =", g)

        g += 1

    f += 1


h = 1

while h <= 3:
    print("f =", h)
    i =1

    while i <= 3:
        print("\ti =", i, end="")

        # we write "print(" i =", i, end="")" to print the output in the same line.

        i += 1

    print()
    h += 1


    ## For loop
        # works on collection
        # works on data
        # cant iterate infinite times.

for j in range(1, 11):
    print(j)


for k in range(1, 11):
    print(k)

    if k == 6:
        break


for l in range(1, 11):

    if l == 6:
        continue

    print(l)


list1 = ["hello", 1, 54, "shashank", 5.3, 'a']

for m in list1:

    if m == "shashank":
        continue

    print(m)
