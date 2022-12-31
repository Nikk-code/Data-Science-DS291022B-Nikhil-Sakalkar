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

Single inheritance: A single derived class acquires members from one superclass.
Multi-Level inheritance: At least 2 different derived classes acquire members from two distinct base classes.
Hierarchical inheritance: A number of child classes acquire members from one superclass
Multiple inheritance: A derived class acquires members from several superclasses.
