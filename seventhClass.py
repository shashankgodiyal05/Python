
## Date - 27/12/2022

## Control flow

    # 1. Condition based control flow

    # if

var1 = int(input("--> Enter a number: "))

if var1 % 2 == 0 :
    print(var1, "is an even number.")



    # if......else

if var1 % 2 == 0 :
    print(var1, "is an even number.")

else:
    print(var1, "is an odd number.")



    # if......elif......else

if var1 >= 1 and var1 <= 100:
    print(var1, "is in range of 1 - 100")
elif var1 > 100 and var1 <= 200:
    print(var1, "is in range of 100 - 200")
else:
    print("!Invalid Input.")



    # nested if

ch = input("--> Enter an Alphabet: ")

if ch >= 'a' and ch <= 'z':

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print("Input is vowel.")
    else:
        print("Input is consonant.")

else:
    print("!Invalid Input.")
