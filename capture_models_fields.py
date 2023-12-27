import re

e = r' {2}|\t(\w+) ?= ?models.'
s = input('Paste your model class declaration: \n')
if s:
    m = re.findall(s, e)
    if m:
        print(m)
