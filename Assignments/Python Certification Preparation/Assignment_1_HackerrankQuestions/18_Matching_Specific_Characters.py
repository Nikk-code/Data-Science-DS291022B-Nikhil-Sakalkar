'''

Matching Specific Characters
https://www.hackerrank.com/challenges/matching-specific-characters/problem

'''

Regex_Pattern = r'^\d\w{4}\.$'    # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
