'''

itertools.permutations()
https://www.hackerrank.com/challenges/itertools-permutations/problem

'''

from itertools import permutations

def per(s, size):
    return "\n".join(sorted(["".join(i) for i in permutations(s,size)]))


user = input().split(" ")

s, size = user[0], int(user[1])

print(per(s,size))
