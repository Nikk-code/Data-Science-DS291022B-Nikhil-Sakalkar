"""
Set .intersection() Operation
https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

"""

input()
a = set(map(int,input().split()))
input()
b = set(map(int,input().split()))
print(len(a.intersection(b)))
