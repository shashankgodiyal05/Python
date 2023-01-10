## Date 02/01/2023

# did some doubt questions:-

# reverse a number

n = int(input("Enter a number:"))
rev = 0

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n //= 10

print("Reverse Number:", rev)


# Question no. 21 from loop_exercise1

for n in range(100, 401):
    n1 = n
    while n > 0:
        d = n % 10
        if d % 2 != 0:
            break
        n //= 10

    else:
        print(n1, end=" ")


# triange * pattern

for i in range(1, 6):
    print("* " * i)


# pyramid * pattern

i = 1
while i <=5:
    sp = 1
    while sp <= 5 - i:
        print(" ", end=" ")
        sp += 1
    
    st = 1
    while st <= (2 * i - 1):
        print("* ", end="")
        st += 1
    
    print()
    i += 1


# Pyramid * pattern with for loop

for i in range(1, 6):
    print("  " * (5 -i) + "* " * (2 * i -1))
