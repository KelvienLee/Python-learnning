import re


str = '匹adj配的a内容'

pa = re.match(r'a-z', str)

print(pa)