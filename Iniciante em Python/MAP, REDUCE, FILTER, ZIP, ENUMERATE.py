# Map

from functools import reduce
Numbs = [133, 5.000, 3690, 1457, 888, 83928329, 3298392832]
Powt = list(map(lambda x: x ** 2, Numbs))
print(Powt)

celsius = [25, 30, 21, 31, 27]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius))
print(fahrenheit)

# Reduce

Numbz = [20, 30, 68, 68, 10]
product = reduce(lambda x, y: x*y, Numbz)
print(product)

# Filter

numpars = [23, 20, 18, 92, 10, 82, 100, 200, 300]
pares = list(filter(lambda x: x % 2 == 0, numpars))
print(pares)


Estudantes = [
    {'Nome':  'Maria Eduarda', 'Notas': [10, 9, 7.6]},
    {'Nome': 'Walter White', 'Notas': [0.4, 1.4, 10]},
    {'Nome': 'Roberto Carlos', 'Notas': [6.4, 2.4, 4.2]},
]

Sera_q_passou = list(filter(lambda x: sum(
    x['Notas']) / len(x['Notas']) > 8.5, Estudantes))
print(Sera_q_passou)

# Zip

nomes = ['Maria', 'Zeus', 'Aristóteles']
idade = [19, 14, 30]
pessoas = list(zip(nomes, idade))
print(pessoas)

names = ['Sonya Blade', 'Kitana', 'Liu Kang']
ages = [40, 24, 32]
for names, ages in zip(names, ages):
    print(f'{names} is {ages} years old.')

names = ['Davinci', 'Turing', 'Maria Eduarda']
ages = [16, 18, 20]
hobbies = ['Nerd', 'Programação', 'Morrer de Trabalhar']
people = list(zip(names, ages, hobbies))
print(people)

# Enumerate

Livros = ["Cosmos", "Estoicismo", "Mindset", "AC1",
          "AC Renascença", "AC Brotherhood", "AC Revelations"]
for index, Livro in enumerate(Livros, start=1):
    print(f'{index}:{Livro}')
