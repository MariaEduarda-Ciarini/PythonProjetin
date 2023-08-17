import re

default = "[0-9][a-z][0-9]"
text = "123 1a2 1cc 2aa"
response = re.search(default, text)
print(response)
print(response.group())

default = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
text = "aaabbbccc dudinha231@gmail.com.br"
response = re.search(default, text)
print(response.group())