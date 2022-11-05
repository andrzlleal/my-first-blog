#input('Digite a sua idade: ')

#nome = input('Digite seu nome: ')

#idade = input('Digite sua idade: ')

#print('Seu nome é ', nome, 'e sua idade ', idade)

# idade = int(input("Informe sua idade: "))

# if idade >= 18 :
#     print("Liberado")

# elif idade == 16 :
#     print("Quase liberado")

# else : 
#     print('Não ta liberado')

# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite outro numero: '))

# print(n1**n2)

# nome_completo = ['andreza', 'mirely', 'leal']

# print(nome_completo[-1])

# nome_completo = []

# print(nome_completo)

# nome_completo.append('andreza')

# print(nome_completo)

# nome = input("Digite seu nome: ")
# sobrenome = input("Digite seu sobrenome: ")

# nome_completo = [nome, sobrenome]
# print(nome_completo[1])

# dicionario = {'nome': 'andreza', 'idade': 21, 'altura': 1.61, 'nacionalidade': 'brasileira' }
# print('seu nome é',dicionario['nome'], 'você tem', dicionario['idade'],'e sua altura é', dicionario['altura'])

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# altura = float(input("Digite sua altura "))

# dicionario = {'nome': nome, 'idade': idade, 'altura': altura}
# print(dicionario['nome'], dicionario['idade'], dicionario['altura'])

# lista = [1, 2, 3]
# print(lista)

# lista[0] = lista[-1]
# print(lista)

# lista = [2, 4, 7, 3, 6]
# print(lista)

# lista.pop(2)
# print(lista)

#print(len(lista))

#lista.sort()
#print(lista)

#lista.reverse()
#print(lista)

# nome = 'andreza'

# idade = 21

# altura = 1.61

# if (idade >= 18 or nome == 'andreza') and altura >= 1.61:
#     print("correto")


# nome = input("Informe seu nome: ")
# idade = int(input("Informe sua idade: "))
# cpf = input("Informe seu cpf: ")

# if nome == 'joao' and cpf == '00000000000':
#     print('Está liberado')

# elif idade > 21:
#     print('Está liberado')

# else:
#     print('Não está liberado')

#lista = ['uva', 'goiaba', 'melancia', 'abacaxi']

# for elemento in lista:
#     print(elemento)

# lista = [1, 4, 6, 7, 2]
# soma = 0

# for elemento in lista:
#     soma = elemento + soma

# print(soma)

# for numero in range(5):
#     print(numero)


# lista = []
# soma = 0
# for nota in range(5):
#     notas = float(input('Digite suas 5 notas: '))
#     lista.append(notas)
#     print(f'{soma} + {notas} = {soma + notas}')
#     soma = soma + notas


# print('Lista de notas:', lista)
# print('Soma das notas:', soma)   
# print('A média é: ', soma/5)


qnt = int(input("Informe a quantidade de notas: "))

soma = 0


for nota in range(qnt):
    notas = float(input('Digite sua nota:'))
    
    soma = soma + notas


media = soma/qnt
print(media)

if media >= 7:
    print("Aprovado")
else:
    print('Reprovado')
