## Date - 05/01/2023

### Collections

    ## 1. List

li = [1, 4, 5.6, 7+6j, 4, "python", [1, 4, 5.6, 7+6j, 4 ,"Ducat"]]
l1 = [45, 68, 45, 256, 843]



print(li)
print(li[5])
print(li[-1][-1])
print(li[2:-2])

for x in l1:
    print(l1[x])


        # Functions-

# len()- Return the number of items in a container.
print(len(li))

# max()- With a single iterable argument, return its biggest item. The default keyword-only argument specifies an object to return if the provided iterable is empty. With two or more arguments, return the largest argument.
print(max(l1))

# min()- With a single iterable argument, return its smallest item. The default keyword-only argument specifies an object to return if the provided iterable is empty. With two or more arguments, return the smallest argument.
print(min(l1))

# sum()- Return the sum of a 'start' value (default: 0) plus an iterable of numbers
# When the iterable is empty, return the start value. This function is intended specifically for use with numeric values and may reject non-numeric types.
print(sum(l1))


        # Methods-

# append()- Append object to the end of the list.
li.append("New Delhi")
print(li)
    
# insert()- Insert object before index.
li.insert(2, "New Delhi")
print(li)

# copy()- Return a shallow copy of the list.
li1 = li.copy()
print(li1)

# clear()- Clears the content of the list.
li1.clear()
print(li1)

# count()- Return number of occurrences of value.
print(li.count(4))

# index()- Return first index of value.Raises ValueError if the value is not present.
print(li.index(4))

# pop()- Remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.
li.pop(2)
print(li)

# remove()- 
li.remove("python")
print(li)

# reverse()- 
li.reverse()
print(li)

# sort()-
        # Sort the list in ascending order and return None.
        # The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).
        # If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.
        # The reverse flag can be set to sort in descending order.
# l1.sort()
print(l1)

# l1.sort(reverse=True)
print(l1)

# extend()- Extend list by appending elements from the iterable.
l1.extend([34, 52, 76, 4])
print(l1)




print(li + l1)
print(l1 * 4)

l2 = [1, 2, 3, 4, 5]
l3 = []
for x in l2:
        l3.append(x ** 2)

print(l3)