from TelephonesBR import  TelephonesBR
import re

#default_mold = "(xx)aaaa-wwww"
#default = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
#text = "i like the  number 2143432432 and that number too 09934823785"
#response = re.search(default, text)
#print(response.group())

# telephone = "9947272443"

telephone = "551126481234"
telephone_object = TelephonesBR(telephone)

#telephone_object2 = TelephonesBR(telephone2)
#default = "([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})([0-9]{4})"
#response = re.search(default, telephone2)
#print(response.group(1, 2, 3, 4))

print(telephone_object)