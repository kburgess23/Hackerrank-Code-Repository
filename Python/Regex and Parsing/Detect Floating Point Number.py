# https://www.hackerrank.com/challenges/introduction-to-regex/problem


import re

for _ in range(int(input())):
    print(bool(re.search(r'^[+-]?\d*\.\d{1,}$', input())))


# github.com/ArutselvanManivannan
