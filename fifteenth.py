## Date - 11/01/2023

        ## Dictionary

dictionary1 = {'a' : "apple", 12 : "Twelve", 12.65: "Twelve Point Six Five"}

print(dictionary1)

for x in dictionary1:
    print(x)

dictionary1[12] = "Twelveeeee"
print(dictionary1)

# To add new element into the dictionary
dictionary1['b'] = "Ball"
print(dictionary1)



        # Methods

    # clear()

dictionary1.clear()
print(dictionary1)


    # copy()

dictionary2 = dictionary1.copy()
print(dictionary2)


    # get()- Return the value for key if key is in the dictionary, else default.

print(dictionary1.get('a'))


    # D.values() -> an object providing a view on D's values

# To print the values from the dictionary

print(dictionary1.values())

for x in dictionary1.values():
    print(x)


    # D.keys() -> a set-like object providing a view on D's keys

print(dictionary1.keys())

# To print the keys from the dictionary
for x in dictionary1.keys():
    print(x)


    # D.items() -> a set-like object providing a view on D's items

print(dictionary1.items())

# To print the both keys and values from the dictionary

for x in dictionary1.items():
    print(x)

print("\n\n\n")

for x, y in dictionary1.items():
    print(x, y)

    # pop()- D.pop(k[,d]) -> v, remove specified key and return the corresponding value. If the key is not found, return the default if given; otherwise, raise a KeyError.

dictionary1.pop('a')
print(dictionary1)


    # popitem()- 

dictionary1.popitem()
print(dictionary1)


    # update()-

dictionary1.update({'d' : 'doll', 'e' : 'elephant'})
print(dictionary1)


    # setdefault()-

dictionary1.setdefault("f","fox")
print(dictionary1)


    # fromkeys()- Create a new dictionary with keys from iterable and values set to value.

dictionary3 = {}

keys = [11, 22, 33, 44, 55]

dictionary3 = dictionary3.fromkeys(keys)
print(dictionary3)

dictionary3 = dictionary3.fromkeys(keys, "abhi khali hai")
print(dictionary3)