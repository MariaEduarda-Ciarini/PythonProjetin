# Loop For

InTupol = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in InTupol:
    print(i)

Lang_USED = ["Python", "SQL", "R", "Java", "C+",
             "JavaScript", "Fortran", "Cobol", "Ruby"]
for j in Lang_USED:
    print(j)

for c in range(0, 20):
    print(c)

# Números pares dentro da lista

ParsNumber = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
for num in ParsNumber:
    if num % 2 == 0:
        print(num)

# Intervalo de 3 em 3

for p in range(0, 101, 3):
    print(p)

# Com Strings

for caracter in "Python AN.dados, Gráficos, Searchs, Back-End, Calculos, Estatísticas":
    print(caracter)

for n in range(0, 3):
    for a in range(0, 3):
        print(a)


# Loop For Aninhados

lst = [0, 1, 2, 3, 4, 5, 6]
lst2 = [1, 2, 3, 4]

# Loop externo
for elemento_lst in lst:

    # Loop interno
    for elemento_lst2 in lst2:

        print('\n', elemento_lst * elemento_lst2)

    print('---')

list1 = [10, 16, 24, 39, 47]
list2 = [32, 89, 47, 76, 12]
for elemento_list1 in list1:
    for elemento_list2 in list2:
        if elemento_list1 == 47 and elemento_list2 == 47:
            print("O número 47 foi encontrado nas duas listas")

listA1 = [10, 16, 24, 39, 47]
listA2 = [32, 89, 47, 76, 12]
soma = 0
for lista in [listA1, listA2]:
    for num in lista:
        if num % 2 == 0:
            soma += num
print(" A soma dos números pares das duas lista é igual a", soma)

matrizA = [[99, 88, 102], [23, 100, 483], [903.23, 9237.00, 1234]]
MaiorNumber = 0

for linha in matrizA:
    for num in linha:
        if num > MaiorNumber:
            MaiorNumber = num
    print("Maior número:", MaiorNumber)


dictionar = {'k1': 'python', 'k2': 'sql', 'k3': 'r'}
for item in dictionar:
    print(item)

# Loop While

i = 0
while i < 100:
    print(i)
    i = i + 13

x = 0
while x < 4:
    print('O valor de x nesta iteração é: ', x)
    print('x ainda é menor que 10, adicionando 1 a x')
    x += 1
else:
    print('Volta no Loop completa!')


for chek in 'Python Curso Aprendizagens':
    if chek == 'z':
        continue
    print(chek)
