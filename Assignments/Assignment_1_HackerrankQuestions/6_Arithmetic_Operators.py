"""
Arithmetic Operators

https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    def add(x,y):
        return x + y

    def sub(x,y):
        return x - y

    def mul(x,y):
        return x * y

    print(add(a,b))
    print(sub(a,b))
    print(mul(a,b))
