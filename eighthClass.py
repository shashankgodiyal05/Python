
## Date 28/12/2022

    # 2. Looping based control flow

    # while loop-

a = 1

while a <= 10:
    print("Hello Python.")
    a += 1


## printing counting 1 - 100

b = 1

while b <= 10:
    print(b)
    b += 1


## printing reverse counting 10 - 1

c = 10

while c >= 1:
    print(c)
    c -= 1


## table of 5

d = 1
num = 5

while d <= 10:
    print(num, "*", d, "=", num * d)
    d += 1


## table of 'n' where n is an input from the user.

n = int(input("Enter a number: "))
e = 1

while e <= 10:
    print(n, "*", e, "=", n * e)
    e += 1


## print the factors of a number 'n1' where n1 is the input from the user.

n1 = int(input("Enter the number: "))
f = 1

while f <= n1:
    if n1 % f == 0:
        print(f)

    f += 1


## check if 'n2' is prime or not.

n2 = int(input("Enter the number: "))
g = 1
count1 = 0

while g <= n2:
    if n2 % g == 0:
        count1 += 1

    g += 1

if count1 == 2:
    print(n2, "is a prime number.")

else:
    print(n2, "is not a prime number.")


## add all odd numbers between 1 - 20.

h = 1
sum1 = 0

while h <= 20:
    sum1 += h
    h += 2

print("The sum of all odd numbers between 1 - 20 is", sum1)


## add all the numbers between 1 - 10.

i = 1
sum2 = 0

while i <= 10:
    sum2 += i
    i += 1

print("The sum of all the numbers between 1 - 10 is", sum2)


## multiply all the numbers between 1 - 10.

j = 1
res1 = 1

while j <= 10:
    res1 *= j
    j += 1

print("The multiplication of all the numbers between 1 - 10 is", res1)


## find the sum of each digit of 54321

num1 = 54321
sum3 = 0
while num1 > 0:
    temp1 = num1 % 10
    sum3 += temp1
    num1 //= 10

print("the of all the digits of", num1, "is", sum3)
