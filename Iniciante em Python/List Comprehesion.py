lstnm = [x for x in range(11)]
print(lstnm)

lstmnr = [x for x in range(25) if x < 16]
print(lstmnr)

livros_ac = ['Assassins 1', 'Assassins 2',
             'Assassins BH', 'Assassins RV', 'Asssasins Renegado']
novalist = []

for x in livros_ac:
    if 'R' in x:
        novalist.append(x)
    print(novalist)


novalist = [x for x in livros_ac if "R" in x]
print(novalist)


p2rs = [x for x in range(101) if x % 2 == 0]
print(p2rs)


def ache_primos(n):
    return [x for x in range(2, n+1)if all(x % y != 0 for y in range(2, int(x ** 0.5)+1))]


print(ache_primos(101))

numbers = [22, 4000, 1945, 1966, 123, 666, 2003, 1999]
quadradada = [x**2 for x in numbers]
print(quadradada)


Celsius = [29, 22, 32, 38, 16, 17, 30, 40, 12]
Fahrenheit = [((float(9)/5)*temp + 32) for temp in Celsius]
print(Fahrenheit)
