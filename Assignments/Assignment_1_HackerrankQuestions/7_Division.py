"""

Python: Division
https://www.hackerrank.com/challenges/python-division/problem

"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    def division_int(x,y):
        return x // y

    def division_flt(x,y):
        return x / y

    print(division_int(a,b))
    print(division_flt(a,b))
