import re
str1="what we think we become; we are Python programmer"
substr = "we"
res = [i.start() for i in re.finditer(substr,str1)] 
print(res)
