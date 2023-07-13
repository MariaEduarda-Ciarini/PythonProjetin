import numpy as np
print(np.__version__)

# Mais eficiente que listas

# Criando Arrays em forma de lista

arr_1 = np.array([1, 2, 3, 20, 30, 40, 50, 1000, 2003, 99])
print(arr_1)
print(type(arr_1))

# Formato do array

print(arr_1.shape)

# Indexação

print(arr_1[7])

# Exclusivo

print(arr_1[2:7])

print(arr_1[2:7+1])

# Imprimindo elementos dos índices
# Cria uma lista de índices

indices = [0, 2, 5, 8, 9]

print(arr_1[indices])

# Criando um padrão booleano para os elementos pares

pars = (arr_1 % 2 == 0)
print(pars)

print(arr_1[pars])

# Alterando um elemento do array

arr_1[7] = 60
print(arr_1)

# Funções Numpy

arr_2 = np.array([10, 20, 30, 40, 50])
print(arr_2)

# Usando métodos do array Numpy

# Soma Acumulada

print(arr_2.cumsum())

# Produto acumulado dos elementos array

# 10x20x30x40x50

print(arr_2.cumprod())

# Função arange -start, -stop, -step

arr_3 = np.arange(0, 31, 3)
print(arr_3)

print(type(arr_3))

print(np.shape(arr_3))

print(arr_3.dtype)

# Um array preenchidos com zeros

arr_4 = np.zeros(20)
print(arr_4)

# Número 1 na posição diagonal

arr_5 = np.eye(5)
print(arr_5)

# Valores passados como parâmetro em forma de diagonal.

arr_6 = np.diag(np.array([100, 200, 300, 400]))
print(arr_6)

# Array valores booleanos

arr_7 = np.array([True, False, False, True, False, True])
print(arr_7)

# Array com strings

arr_8 = np.array(['Python', 'SQL', 'Git', 'HTML'])
print(arr_8)

# Função linspace

print(np.linspace(0, 3))

print(np.linspace(0, 5, 10))

# Função logspace

print(np.logspace(0, 5, 10))
