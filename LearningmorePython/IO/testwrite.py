file_contact = open('contatos - Copia.csv', encoding='UTF-8', mode='w+')

contacts = ['11, Mikasa,gmikasa@mikasa.com.br\n',
            '12, Eren, eren@yeager.com.br\n',
            '13, Hange, zoe@commander.com.br\n'
            '14, Levi, ackerman@levi.com.br\n']

for contact in contacts:
    file_contact.write(contact)

file_contact.flush()

file_contact.seek(0)

for line in file_contact:
    print(line)
