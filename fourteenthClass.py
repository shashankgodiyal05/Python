## Date - 10/01/2023


    ## Tuple-

tpl1 = (2, 3.5, 67 + 8j, [3, 4, "python"], (56, 57, 58.86))
tpl2 = ("ducat", 54, 6)
print(tpl1)

# li = list(tpl1)
# li.append("Ducat")
# print(tuple(li))

print(tpl1.count(2))
print(tpl1.index(3.5))

print(len(tpl1))

# print(tpl1.sum()) this will work if the tuple contain all integer type elements.
# print(tpl1.max()) this will work if the tuple contain all integer type elements.
# print(tpl1.min()) this will work if the tuple contain all integer type elements.

for x in tpl1:
    print(x)

print(tpl1[-1])
print(tpl1[:-1])

# we can add two tupples and multiply the tuple to a integer
print(tpl1 + tpl2)
print(tpl2 * 2)

# single element tuple
t2 = (5, )



    ## Set-

st1 = {2, 3.5, 67 + 8j, (56, 57, 58.86), "python"}

print(len(st1))
# print(st1.sum()) this will work if the set contain all integer tpye elements.
# print(st1.max()) this will work if the set contain all integer type elements.
# print(st1.min()) this will work if the set contain all integer type elements.

for x in st1:
    print(x)


# Methods:

    # add()- Add an element to a set. This has no effect if the element is already present.

st1.add("Hello")
print(st1)

    # clear()- clears the whole set and gives an empty set.

st1.clear()
print(st1)

    # copy()- Return a shallow copy of a set.

st2 = st1.copy()
print(st2)

    # pop()

print(st1)
st1.pop()
print(st1)

    # remove()

print(st1)
st1.remove("python")
print(st1)

st3 = {5, 4, (5, 4, 3.5), 2, "python"}

    # intersection()- Return the intersection of two sets as a new set. (i.e. all elements that are in both sets.)

print(st1.intersection(st3))

    # intersection_update()- Update a set with the intersection of itself and another.

print(st1.intersection_update(st3))

    #  union()- Return the union of sets as a new set. (i.e. all elements that are in either set.)

print(st1.union(st3))

    # difference()- Return the difference of two or more sets as a new set. (i.e. all elements that are in this set but not the others.)

print(st1.difference(st3))

    # difference_update()- Remove all elements of another set from this set.

print(st3.difference_update(st1))

    # symmetric_difference()- Return the symmetric difference of two sets as a new set. (i.e. all elements that are in exactly one of the sets.)

print(st1.symmetric_difference(st3))

    # issubset()- Report whether another set contains this set.

print(st3.issubset(st1))

    # issuperset()- Report whether this set contains another set.

print(st1.issuperset(st3))

    # isdisjoint()- Return True if two sets have a null intersection.

print(st1.isdisjoint(st3))

    # update()- Update a set with the union of itself and others.

st1.update({23, 4, 1})
print(st1)
