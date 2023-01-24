    # Date = 24/01/2023


'''
    Features of OOP

        1. Inheritance:-
            - base class or parent class
            - derived class or child class

        One of the core concepts in object-oriented programming (oop) languages is inheritance. It is a mechanism that allows you to create a hierarchy of classes that shares a set of properties and methods by deriving a class from another class. Inheritance is the capability of on class to derive or inherit the properties from another class.


        Benefits of Inheritance are:

        - It represents real-world relationships well.
        - It provides the reusability of a code. We dont have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
        - It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
        - Inheritance offers a simple, understandable model structure.
        - Less development and maintenance expenses result from an inheritance.

    

    Types of Inheritance:-

    a. single inheritance-

        Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.

'''
class Base:
    
    attr1 = 10
    attr2 = 20

    def method1(self):
        print("base method")

class derived11(Base):
    pass


d = derived11()
print(d.attr1)

d.attr1 = 54
print(d.attr1)


'''
    b. multiple inheritance-

        When a class can be derived from than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class.

'''
class Base111:

    attr1 = 10
    def method1(self):
        print("base method 1")

class Base21:

    attr2 = 20
    def method2(self):
        print("base method 2")

class deriverd1(Base111, Base21):
    pass


d = deriverd1()
d.method1()


'''
    c. multilevel inheritance-

    In multilevel inheritance, features of the base class and the derived class. This is similar to a relationship representing a child and a grandfather.

'''
class Base1:

    attr1 = 10
    def method1(self):
        print("base method 1")

class Base2:

    attr2 = 20
    def method2(self):
        print("base method 2")

class derived1(Base1, Base2):
    pass

class derived2(derived1):
    pass


d = derived2()
d.method2()


'''
    d. hierarchical inheritance-

        When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.

'''
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

obj1 = Child1()
obj2 = Child2()

obj1.func1()
obj1.func2()

obj2.func1()
obj2.func3()


'''
    e. hybrid inheritance-

        Inheritance consistiong of multiple types of inhertance is called hybrid inharitance.

'''
class School:
    def func1(self):
        print("This function is in school.")

class Student1(School):
    def func2(self):
        print("This function is in student 1.")

class Student2(School):
    def func3(self):
        print("This function is in student 2.")

class Student3(Student1,School):
    def func4(self):
        print("This function is in student 3.")


object = Student3()
object.func1()
object.func2()


'''
        2. Polymorphism:-

        The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.


    
    Types of Polymorphism:

    a. method overloading-

        Two or more methods have the same name but different numbers of parameters, or both. These methods are called overloaded methods and this is called method overloading.

'''
class Calculator():
    def add(self, a = 0, b = 0):
        return a + b

c = Calculator()

print(c.add())
print(c.add(4))
print(c.add(3, 8))


'''
    b. method overriding-

        Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes. When a method in a same parameters or signature and same return type (or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.

'''
class Base11:
    def method1(self):
        print("Base Method 1")

class Derived(Base11):
    def method1(self):
        print("Derived Method 1")
        super().method1()

d = Derived()
d.method1()


'''
    c. operator overloading-

        Operator overloading means giving extended meaning beyond their predifined operational meaning. For example operator + is used to add two integers as well as join two strings and merges two lists. It is achievable because '+' operator is overloaded by int class and str class. Same built-in operator or function shows different classes, this is called Operator Overloading.

'''
class calculator:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

    def __sub__(self, other):
        return self.a - other.a


c1 = calculator(3)
c2 = calculator(4)

print(c1 + c2)
print(c1 - c2)