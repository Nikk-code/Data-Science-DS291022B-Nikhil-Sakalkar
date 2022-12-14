Q1 What are Data Types?
>A data type is a set of values and a set of operations defined on data. An implementation of a data type is an expression of data and operations in terms of a specific programming language such as Java, C ++, or Python.

Q2 Name four of the main data types in Python
>Numbers, strings, lists, dictionaries, tuples, files, and sets are generally considered the main types of data. Types, None, and Booleans are sometimes also classified this way. The integer, floating-point, complex, fraction and decimal are numerical data types and simple strings and Unicode strings in Python 2 and text strings and byte strings in Python 3 are the types of string data types.

Q3 Why are these data types known as Python’s core data types?
>They are known as the core data types because they are part of the Python language itself and are always available to create other objects, you usually need to call functions in imported modules.Most of the data types have a specific syntax for generating objects: “spam”, for example, is an expression that creates a string and determines the set of operations that can be applied to it. For this reason, main types are built into Python syntax. Instead, you must call the built-in open function to create a file object.

Q4 What does immutable mean and what three types of Python core data types are considered immutable?
>An immutable data type is a type of object which cannot be modified after its creation. Numbers, strings, and tuples in Python fall into this category. Although you cannot modify an immutable object in place, you can always create a new one by running an expression.

Q5 What does sequence mean and which three types of data fall into this category?
>A sequence data type is a collection of objects ordered by a specific position. In Python, Strings, lists, and tuples are the data types based on sequences. The Sequences share common sequence operations, such as indexing, concatenation, and slicing, but also have type-specific method calls.

Q6 What does mapping mean and what kind of data type is based on mapping?
>The term mapping refers to an object that maps keys to associated values. The Python dictionary is the only type of mapping in the base typeset. Mappings do not maintain any left-to-right position order; they support access to stored data by key, as well as type-specific method calls.

Q7 Define a function in Python.
>A block of code that is executed when it is called is defined as a function. The keyword def is used to define a Python function.

Q8 Describe multithreading in Python.
>Using Multithreading to speed up the code is not the go-to option, even though Python comes with a multi-threading package.
The package has the GIL or Global Interpreter Lock, which is a construct. It ensures that only one of the threads executes at any given time. A thread acquires the GIL and then performs work before passing it to the next thread.
This happens so fast that to a user it seems that threads are executing in parallel. Obviously, this is not the case as they are just taking turns while using the same CPU core. GIL passing adds to the overall overhead to the execution.
As such, if you intend to use the threading package for speeding up the execution, using the package is not recommended.

Q9 Explain Inheritance.
>Inheritance enables a class to acquire all members of another class. These members can be attributes, methods, or both. By providing reusability, inheritance makes it easier to create as well as maintain an application.

![LCO Mascot](https://hackr.io/blog/media/explain-inheritance-min.png)

>The class which acquires is known as the child class or the derived class. The one that it acquires from is known as the superclass, base class, or the parent class. There are 4 forms of inheritance supported by Python:

- Single inheritance: A single derived class acquires members from one superclass.
- Multi-Level inheritance: At least 2 different derived classes acquire members from two distinct base classes.
- Hierarchical inheritance: A number of child classes acquire members from one superclass
- Multiple inheritance: A derived class acquires members from several superclasses.

Q 10 What is the map() function used for?
>The map() function applies a given function to each item of an iterable. It then returns a list of the results. The value returned from the map() function can then be passed on to functions to the likes of the list() and set().
Typically, the given function is the first argument and the iterable is available as the second argument to a map() function. Several tables are given if the function takes in more than one argument.

Q 11 What is the // operator? What is its use?
>The // is a Floor Divisionoperator used for dividing two operands with the result as quotient displaying digits before the decimal point. For instance, 10//5 = 2 and 10.0//5.0 = 2.0.

Q 12 What is the split function used for?
>The split function breaks the string into shorter strings using the defined separator. It returns the list of all the words present in the string.

Q 13 What is a pass in Python?
> The no-operation Python statement refers to a pass. It is a placeholder in the compound statement, where there should have a blank left or nothing written there.

Q 14 What are the is, not and in operators?
>Operators are functions that take two or more values and return the corresponding result.
- is: returns true when two operands are true
- not: returns inverse of a boolean value
- in: checks if some element is present in some sequence.

Q 15 What are tuples in Python?
>A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.

Q 16 What is the difference between tuples and lists in Python?
>The main differences between lists and tuples are − Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists.

Q 17 How will you convert a String to an object in python?
>eval(str) − Evaluates a string and returns an object.

Q 18 What is the purpose of ** operator?
>** Exponent − Performs exponential (power) calculation on operators. a**b = 10 to the power 20 if a = 10 and b = 20.

Q 19 What is lambda function in python?
>‘lambda’ is a keyword in python which creates an anonymous function. Lambda does not contain block of statements. It does not contain return statements.

Q 20 How to overload constructors or methods in Python?
>Python's constructor: _init__ () is the first method of a class. Whenever we try to instantiate an object __init__() is automatically invoked by python to initialize members of an object. We can't overload constructors or methods in Python. It shows an error if we try to overload.

```python

class student:    
    def __init__(self, name):    
        self.name = name    
    def __init__(self, name, email):    
        self.name = name    
        self.email = email    
         
# This line will generate an error    
#st = student("rahul")    
    
# This line will call the second constructor    
st = student("rahul", "rahul@gmail.com")    
print("Name: ", st.name)  
print("Email id: ", st.email)  


```
