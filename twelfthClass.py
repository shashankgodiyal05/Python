## Date - 04/01/2023


## Methods on String

s = "python programming"

    # capitalize()
        # Return a capitalized version of the string.
        # More specifically, make the first character have upper case and the rest lower case.

print(s.capitalize())
# this will resutlt- Python programming

    ## casefold()
        # Return a version of the string suitable for caseless comparisons.

print(s.casefold())
# this will result python programming

    # lower()
        # Return a copy of the string converted to lowercase.

print(s.lower())
# this will result python programming

    # upper()
        # Return a copy of the string converted to uppercase.

print(s.upper())
# this will result- PYTHON PROGRAMMING

    # title()
        # Return a version of the string where each word is titlecased.
        # More specifically, words start with uppercased characters and all remaining cased characters have lower case.

print(s.title())
# this will result- Python Programming

    # swapcase()
        # Convert uppercase characters to lowercase and lowercase characters to uppercase.

S = "Python Progamming"
print(S.swapcase())
# this will result- pYTHON pROGRAMMING

# So the above methods are to perform the operations on the case of values


    # count()
        # Return the number of non-overlapping occurrences of substring sub in string S

print(s.count('m'))
# this will result- 2

    # endswith()
        # s.endswith(suffix[, start[, end]]) -> bool
        # Return True if s ends with the specified suffix, False otherwise. With optional start, test s beginning at that position. With optional end, stop comparing s at that position. suffix can also be a tuple of strings to try.

print(s.endswith('g'))
# this will result- True

    # startswith()
        # s.startswith(prefix[, start[, end]]) -> bool
        # Return True if s starts with the specified prefix, False otherwise. With optional start, test s beginning at that position. With optional end, stop comparing s at that position. prefix can also be a tuple of strings to try.

print(s.startswith('p'))
# this will result- True

    # expandtabs()
        #Return a copy where all tab characters are expanded using spaces.
        # If tabsize is not given, a tab size of 8 characters is assumed.

S1 = "Python \tProgramming"
print(S1.expandtabs(12))
# this will result- Python      Programming

    # index()
        # S.index(sub[, start[, end]]) -> int
        # Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.
        # Raises ValueError when the substring is not found.

print(s.index('o'))
# this will result- 4

    # find()
        # S.find(sub[, start[, end]]) -> int
        # # Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.
        # Return -1 on failure.

print(s.find('m'))
# this will result- 13

    # split()
        # Return a list of the substrings in the string, using sep as the separator string.
        # Note, str.split() is mainly useful for data that has been intentionally delimited. With natural text that includes punctuation, consider using the regular expression module.

print(s.split(" "))
# this will result a list- ['python', 'programming']

    # join()
        # Concatenate any number of strings.
        # The string whose method is called is inserted in between each given string. The result is returned as a new string.

li = ['python', 'programming']
print(", ".join(li))
# this will result- python, programming

    # splitlines()
        # Return a list of the lines in the string, breaking at line boundaries.
        # Line breaks are not included in the resulting list unless keepends is given and true.

s1 = ''' Mera naam sinchan hai me shararat se bhara
badi mushkil me padi meri family nohara. '''

print(s1.splitlines())
# this will result- ['Mera naam sinchan hai me shararat se bhara', 'badi mushkil me padi meri family nohara.']

    # strip()
        # Return a copy of the string with leading and trailing whitespace removed.
        # If chars is given and not None, remove characters in chars instead.

print(s.strip('p'))
# this will result- ython programming

    # lstrip()
        # Return a copy of the string with leading whitespace removed form the left side of the string.
        # If chars is given and not None, remove characters in chars instead.

print(s1.lstrip())
# this will result- Mera naam sinchan hai me shararat se bhara
# badi mushkil me padi meri family nohara.

    # rstrip()
        # Return a copy of the string with trailing whitespace removed from the right side of the string.
        # If chars is given and not None, remove characters in chars instead.

print(s1.rstrip())
# this will result-  Mera naam sinchan hai me shararat se bhara
# badi mushkil me padi meri family nohara.

    # removeprefix()
        # Return a str with the given prefix string removed if present.
        # If the string starts with the prefix string, return string[len(prefix):]. Otherwise, return a copy of the original string.

print(s.removeprefix("p"))
# this will result- ython programming

    # removesuffix()
        # Return a str with the given suffix string removed if present.
        # # If the string ends with the suffix string and that suffix is not empty, return string[:-len(suffix)]. Otherwise, return a copy of the original string.

print(s.removesuffix("ming"))
# this will result- python program

    # replace()
        # Return a copy with all occurrences of substring old replaced by new.
        # count
        # Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.
        # If the optional argument count is given, only the first count occurrences are replaced.

print(s.replace("python","java"))
# this will result- java programming

course = "Python"
language = "Java"
string1 = "{} programming"
string2 = "{} programming and {} programming"
string3 = "{1} programming and {0} programming"

    # format()
        # Return a formatted version of String, using substitutions from args and kwargs. The substitutions are identified by braces ('{' and '}').

print(string1.format(course))
# this will result- Python programming

print(string2.format(course, language))
# this will result- Python programming and Java programming

print(string3.format(course, language))
# this result Java programming and Python programming

string4 = "python_123"

    # isalnum()
        # Return True if the string is an alpha-numeric string, False otherwise.
        # A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

print(string4.isalnum())
# this will result- False

    # isalpha()
        # Return True if the string is an alphabetic string, False otherwise.
        # A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

print(string4.isalpha())
# this will result- False

    # isnumeric()
        # eturn True if the string is a decimal string, False otherwise.
        # A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

print(string4.isnumeric())
# this will result- False

    # isdecimal()
        # Return True if the string is a decimal string, False otherwise.
        # A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

print(string4.isdecimal())
# this will result- False

    # isdigit()
        # Return True if the string is a digit string, False otherwise.
        # A string is a digit string if all characters in the string are digits and there is at least one character in the string.

print(string4.isdigit())
# this will result- False

    # isascii()
        # Return True if all characters in the string are ASCII, False otherwise.
        # ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

print(string4.isascii())
#  this will result- True

    # islower()
        # Return True if the string is a lowercase string, False otherwise.
        # A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

print(string4.islower())
# this will result- True

    # isupper()
        # Return True if the string is an uppercase string, False otherwise.
        # A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

print(string4.isupper())
# this will result- False

    # isidentifier()
        # Return True if the string is a valid Python identifier, False otherwise.
        # Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as "def" or "class".

print(string4.isidentifier())
# this will result- True
