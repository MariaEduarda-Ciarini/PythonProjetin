import numpy as np

# Criando uma matriz lista de listas

arr_9 = np.array([[500, 211, 100], [300, 400, 150]])
print(arr_9)

print(arr_9.shape)

# Criando uma matriz 2x3 apenas com número 1

arr_10 = np.ones((2, 3))
print(arr_10)

# Função matrix

lista1 = [[9, 8, 7], [60, 50, 40], [10, 20, 30]]

arr_11 = np.matrix(lista1)
print(arr_11)

print(arr_11.shape)
print(arr_11.size)

# Indexação da matriz
print(arr_11[2, 1])

print(arr_11[0:2, 2])

print(arr_11[1, ])

# Forçando um tipo de dado

a = np.array([9, 10])
b = np.array([212.98, 512.09])
c = np.array([100, 990], dtype=np.int64)

print(a.dtype, b.dtype, c.dtype)

arr_12 = np.array([[90, 100, 20, 99], [290, 129, 15, 19]], dtype=float)
print(arr_12)

print(arr_12.itemsize)
print(arr_12.nbytes)
print(arr_12.ndim)


# Manipulando Objetos de 3 a 4 Dimensões com Numpy

# Criando um array numpy de 3 dimensões

arr_3D = np.array([[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
],
    [
    [13, 14, 15, 16],
    [17, 18, 19, 20],
    [21, 22, 23, 24]
]
])

print(arr_3D)

print(arr_3D.ndim)

# 2 elementos,  3 linhas dentro dos elementos, 4 colunas

print(arr_3D.shape)

print(arr_3D[0, 2, 1])

# Criando um array numpy de 4 dimensões

arr_4D = np.array([
    [
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ],
        [
            [21, 22, 23, 24, 25],
            [26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40]
        ],
        [
            [41, 42, 43, 44, 45],
            [46, 47, 48, 49, 50],
            [51, 52, 53, 54, 55],
            [56, 57, 58, 59, 60]
        ]
    ],
    [
        [
            [61, 62, 63, 64, 65],
            [66, 67, 68, 69, 70],
            [71, 72, 73, 74, 75],
            [76, 77, 78, 79, 80]
        ],
        [
            [81, 82, 83, 84, 85],
            [86, 87, 88, 89, 90],
            [91, 92, 93, 94, 95],
            [96, 97, 98, 99, 100]
        ],
        [
            [101, 102, 103, 104, 105],
            [106, 107, 108, 109, 110],
            [111, 112, 113, 114, 115],
            [116, 117, 118, 119, 120]
        ]
    ]
])

print(arr_4D)

print(arr_4D.ndim)

# Interpretação dos elementos
# 2 Grupos de elementos, 3 Sub-Grupos, 4 Linhas, 5 Colunas

print(arr_4D.shape)

print(arr_4D[0, 2, 1])

print(arr_4D[0, 2, 1, 4])
