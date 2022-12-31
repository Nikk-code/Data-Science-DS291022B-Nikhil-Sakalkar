"""
Find a string
https://www.hackerrank.com/challenges/find-a-string/problem

"""


def count_substring(string, sub_string):
    counter = 0
    for i,c in enumerate(string):
        if i + len(sub_string) > len(string):
            break
        if string[i:i+len(sub_string)] == sub_string:
            counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
