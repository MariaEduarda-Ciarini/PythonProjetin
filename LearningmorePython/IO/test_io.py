file = open('contacts.csv.csv', encoding='UTF-8', mode='w')
print(type(file.buffer))

# content = file.buffer.read()
# print(content)

text_in_bytes = bytes('Text in bYtES', 'UTF-8')
#print(text_in_bytes)
#print(type(text_in_bytes))

contact = bytes('15, Sasha, Sasha@braus.com.br', 'UTF-8')
file.buffer.write(contact)

file.close()