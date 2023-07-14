# Análise Estatística Básica com Numpy

import numpy as np

arr_13 = np.array([15, 45, 12000, 198, 168.96])
print(arr_13.mean())

arr_14 = np.array([5000, 4500, 3500, 2500, 6350])
print(arr_14.mean())

# Desvio Padrão (Standard Deviation)

print(arr_13.std())
print(arr_14.std())

# Variância

print(np.var(arr_13))
print(np.var(arr_14))

# Operações Matemáticas com array Numpy

# Soma

arr_15 = np.arange(1, 10)
print(arr_15)
print(np.sum(arr_15))

arr_16 = np.arange(3, 11)
print(arr_16)
print(np.sum(arr_16))

# Retorna o produto dos elementos

print(np.prod(arr_15))
print(np.prod(arr_16))

# Retorna a soma acumulada dos elementos

print(np.cumsum(arr_15))
print(np.cumsum(arr_16))

# Soma dos arrays
arr_17 = np.array([2, 4, 8])
arr_18 = np.array([4, 4, 8])
arr_19 = np.add(arr_17, arr_18)

print(arr_19)

# Multiplicar as duas matrizes

arr_20 = np.array([[1, 2], [3, 4]])
arr_21 = np.array([[5, 6], [0, 7]])

arr_22 = np.dot(arr_20, arr_21)
print(arr_22)

arr_23 = np.array([[20, 40], [30,60]])
arr_24 = np.array([[25, 60], [70, 30]])
arr_25 = np.dot(arr_23, arr_24)
print(arr_25)

# Slicing

arr_26 = np.diag(np.arange(4))
print(arr_26)

print(arr_26[1, 1])
print(arr_26[1])
print(arr_26[:,2])

# Comparação

x = np.array([20, 50, 60, 10])
y = np.array([50, 50, 20, 20])

print(x == y)

# Somando um valor a cada elemento do array

print(np.array([3, 6, 9, 12]) + 1.5)

# Arrendondadamento

arr_27 = np.array([90.9, 91.9, 99.9, 0.9, 1.5, 2.9])
print(np.around(arr_27))

# Método flatten()

arr_28 = np.array([[1000, 2000, 3000, 4000],[5000, 6000, 7000, 8000]])
print(arr_28)

arr_29 = arr_28.flatten()
print(arr_29)
