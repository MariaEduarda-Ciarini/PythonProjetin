import re

mytxt = "Meu email é duciamo@gmail.com e voce pode me achar em outro email bssndd@gmail.com"

# Expressões Regulares para contar quantas vezes o caracter @ aparece no texto

fintxt = len(re.findall("@", mytxt))
print(" O caractere '@' aparece", fintxt, "vezes no texto.")

fintxt = len(re.findall("du", mytxt))
print(" O caractere 'du' aparece", fintxt, "vezes no texto.")

# Expressão regular para extrair a palavra que aparece após a palavra "voce" no mytxt

fintxt = re.findall(r'voce (\w+)', mytxt)
print("A palavra após 'voce' é:", fintxt[0])

fintxt = re.findall(r'outro (\w+)', mytxt)
print("A palavra após 'outro' é:", fintxt[0])

# Expressão regular para extrair endereços de emails de uma string

emails = re.findall(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', mytxt)
print(emails)


# Extraindo os adverbios da frase

txt_1 = "Estudando a documentação e aplicando os conceitos em Python, mas a documentação da um preguiça."

for i in re.finditer(r"\w+ção\b", txt_1):
    print('%02d-%02d: %s' % (i.start(), i.end(), i.group()))
