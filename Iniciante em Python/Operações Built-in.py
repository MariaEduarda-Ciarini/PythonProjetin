# Operador IN
MEC3 = ["Algoritmos", 9.0, 2023]
print(MEC3)
print(2023 in MEC3)
print(9.0 in MEC3)

# Built-in
Numberz_MEC23 = [1929, 2008, 2020, -2022]
print(Numberz_MEC23)
print(len(Numberz_MEC23))
print(max(Numberz_MEC23))
print(min(Numberz_MEC23))

DataScAc = []
for item in Numberz_MEC23:
    DataScAc.append(item)

print(DataScAc)
print(Numberz_MEC23)

CountriES = ['BRA', 'EUA', 'UK', 'LUX']
print(CountriES)
CountriES.extend(['SUI', 'JPN', 'ITA'])
print(CountriES)
print(CountriES.index('UK'))
print(CountriES.index('ITA'))
CountriES.insert(3, 2024)
print(CountriES)
CountriES.sort
print(CountriES)
CountriES.reverse()
print(CountriES)
CountriES.remove(2024)
print(CountriES)

# Dicionário

EScountri = {"LUX": 2024, "EUA": 2025, "ITA": 2026, "SUI": 2029, "BRA": 2023}
print(EScountri)
print(type(EScountri))
print(len(EScountri))
print(EScountri.keys())
print(EScountri.values())
print(EScountri.items())
print(EScountri["LUX"])

print(EScountri["ITA"])
MEC20 = {'M1': 21, 'M2': 22, 'M3': 23, 'M4': 26, 'M5': 20}
print(MEC20)
print(type(MEC20))
EScountri.update(MEC20)
print(EScountri)
print(type(EScountri))
