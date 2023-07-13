# POO
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


p = Pessoa("Jurandi", "Silva")
print(p)
print(Pessoa)
print(p.nome)
print(p.sobrenome)


@dataclass
class Livro:
    titulo: str
    gênero: str
    paginas: int
    autor: str


L = Livro("Introdução à Linguagem SQL",
          "Tecnico Didatico",  141,  "Thomas Nield")
print(Livro)
print(L)
print(L.titulo)
print(L.gênero)
print(L.paginas)
print(L.autor)


@dataclass
class Cachorro:
    nome: str
    raça: str
    pelagem: str
    kg: int
    idade: int
    vacina_em_dia: str


Dog = Cachorro("Max", "Vagabundo", "Preto e Branco", "34", "12", "Deve estar")
print(Dog)

print(Dog.nome)
print(Dog.raça)
print(Dog.pelagem)
print(Dog.kg)
print(Dog.idade)
print(Dog.vacina_em_dia)


@dataclass
class random:
    x: int
    y: float
    z: int
    a: int
    b: int
    c: float


i = random(90, 20.0, 700, 250, 10, 232.90)
print(i)


@dataclass
class Funcionario:
    nome: str
    empresa: str
    salario: int


Func = Funcionario("Jurandi", "Nasa", 250000)
print(Func)
print(Func.nome)
print(Func.salario)
print(Func.empresa)
