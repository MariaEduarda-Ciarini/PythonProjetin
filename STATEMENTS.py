if 1500 < 1499:
    print("Não, não é maior!")
else:
    print("Sim é maior")

if 2003 > 2023:
    print("Sim foi à 20 anos atrás")
else:
    print('Não, não é maior que 2023')

Livros2023 = 15
if Livros2023 < 15:
    print("Dobrou a meta!2x")
else:
    print("Ainda não bateu a meta, continue lendo mais!")

Idade = 19
if Idade > 18:
    print('Acesso liberado!')

Nominho = 'Maria'
if Idade > 18:
    if Nominho == 'Maria':
        print('Sim, é a Rainha')
    else:
            print('Não é ela, senhores!')

Dia = "Quarta"
if Dia == "Segunda":
    print("Odeio Segunda-feira, gutí gutí")
else:
    print("Hoje vai cair um pé D'aGua!")


if Dia == "Quinta":
    print("Dor de cabeça e chuva!")

elif Dia == "Domingo":
    print("Dia de estudar 10% e lêr")

elif Dia == "Quarta":
    print("Dia de estudar 20% e Lêr")

else:
    print("Dormir e comer")

print(6 > 3)
print(9 < 8.5)
print(19 > 15)
print(29 > 19)
print(29 == 30)
print(32 >= 31)
print(20 >= 20.50)
print(21.99 <= 21.89)

if 999 == 9998:
    print("Se for verdadeira")
if True:
    print("Yes, is False")

Age = 16
Name = 'Wawrzyniec'
if Age >= 16 and Name == 'Wawrzyniec':
    print('Wawrzyniec, passou no teste')

Sol = 29
TempNorml = "Acima de 17"
if (Sol >= 29) or (TempNorml == "Acima de 17"):
    print("Tudo no seu devido lugar")

NumBer = 230
if (NumBer > 229) and (NumBer % 2 == 0):
    print("Isso está sendo impresso porque as duas condições são verdadeiras")

NumBer = 100
if (NumBer > 101) and (NumBer % 2 == 0):
    print("Isso está sendo impresso porque as duas condições são verdadeiras")
else:
    print("Uma das duas condições é falsa")

NumBer = 130
if (not(NumBer > 84.30) and (NumBer % 2 == 0 )) or (NumBer == 130):
    print("Isso está sendo inputado porque as duas primeiras são verdadeiras ou a terceira é verdadeira!")

enjoyable_discipline = "Analise de Dados"
Nota_Finale = 80

if enjoyable_discipline == "Analise de Dados" and Nota_Finale >= 70:
    print("Aprovado no Curso de Analise de Dados!")

else:
    print("Tente refazer todo o curso com mais atenção e estude mais!")

Disciplina = input('Digite o curso que você quer:  ')
NotaFim = input ('Digite a sua nota disponibilizada (entre 0 e 100):' )

if Disciplina == 'Analista de Dados' and NotaFim  and float('80'):
    print("Parabens! você passou neste curso!")
else:
    print('Ops!! Tente denovo fazer o curso.')

Disciplina = input('Digite o curso que você quer: ')
NotaFim = input ('Digite a sua nota disponibilizada (entre 0 e 100):' )
NotaSemestral = input('Digite sua nota no semestre (entre 0 a 10): ')

if Disciplina == 'Analista de Dados' and NotaFim  and float('80') and float(NotaSemestral) !=6.5:
    print("Parabens! você passou neste curso!")

elif Disciplina == 'Data Science' and NotaFim and int('90') and float(NotaSemestral) !=1:
    print("Você passou com  %r%%  Em %s!. Parabens!" % (NotaFim, Disciplina))

else:
    print('Ops!! Tente denovo fazer o curso.')
