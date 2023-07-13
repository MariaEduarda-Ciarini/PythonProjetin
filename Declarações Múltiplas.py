# Declarações Múltiplas

x2 = 2
y3 = 5.07
z1 = 20
print(x2)
print(y3)
print(z1)
SomaE = x2 + y3 + z1
print(SomaE)

SomaF = x2 * z1 * y3
print(SomaF)

a = 3
b = 1.5
c = 4.50
Area = a * b
print(Area)

Peri = 2 * (b+2) * a
print(Peri)

mult = 2 * c + a * a
print(mult)

NickName = 'Maria Eduarda'
Mean = 'Ciarni'
FullName = NickName + " " + Mean
print(FullName)

# Strings
print('Python\nPara\nTodos\n!!!')

Dudinha = "Back-End, Análise de Dados, Data Science"
print(Dudinha.upper())
print(Dudinha.lower())
print(Dudinha.split())
print(Dudinha.capitalize())
print(Dudinha.count("a"))
print(Dudinha.count("e"))
print(Dudinha.find("End"))
print(Dudinha.islower())
print(Dudinha.isspace())
print(Dudinha.isalnum())
print(Dudinha.endswith("e"))

# Comparando **Strings**
print("Dudinha" == 'nha')
print("Dudinha" == 'Du')
print("Dudinha" == "Dudinha")

# Estruturas de Dados
LanPro_B = ["Python", "SQL", "Java", "R"]
print(LanPro_B)
print(type(LanPro_B))

Sit_BanJr = ["Science", "Graphic", "Dados", "Estatísticas"]
print(Sit_BanJr)
print(type(Sit_BanJr))

All_BPJR = ["java, python, banco de dados, r"]
print(All_BPJR)
print(type(All_BPJR))

Num1_Str = [20, 18, 19, "Análista"]
print(Num1_Str)
print(type(Num1_Str))

Sit_BanJr.append("Pesquisas")
print(Sit_BanJr)

nestle = [[18, 19, 20], [16, 17, 15], [32, 21, 25]]
print(nestle)
print(type(nestle))
print(nestle[0])
print(nestle[2])
print(nestle[1])

# matrizes
Vari_A = nestle[0]
print(Vari_A)
print(type(Vari_A))

Vari_B = Vari_A[0]
print(Vari_B)
print(type(Vari_B))

print(Vari_A[0:2])

Concat = [100, 90, 75]
print(Concat)

Concat2 = [80, 85, 105]
print(Concat2)

Concaten_List = Concat + Concat2
print(Concaten_List)
print(type(Concaten_List))
Concaten_List.sort()
print(Concaten_List)
