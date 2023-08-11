file1 = open('contatos - Copia.csv', encoding='UTF-8', mode='w')
file2 = open('contatos - Copia.csv', encoding='UTF-8', mode='a')

conctact_aristarchus = '11,Aristarchus, Aristarchus@.com.br\n'
conctact_democritus = '11,Democritus, Democritus@.com.br\n'

file1.write(conctact_aristarchus)
file2.write(conctact_democritus)

file1.close()
file2.close()
