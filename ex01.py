print('Hello, world')
nome = input('Digite seu nome: ')  # Criando a variável nome
idade = 23

print(nome, idade)
"""
Tipo de váriaveis
1. int: número inteiros, sem parte decimal: 0 5 -1 1000
2. float: números reais, números com parte decimal, negativos ou inteiros: 1.0 -2.7
3. str: cadeias de caracteres, ou seja, dados textuais (string)
4. bool: valores lógicos (booleanos): True ou False
"""
print(type(idade))  # Imprime o tipo da variável idade
linguagem = input('Qual é a linguagem de programação que você está estudando?')
print('A linguagem que você está estudando é', linguagem)

# > Operadores artiméticos
"""
- Soma: +
- Subtração: -
- Multiplicação: *
- Divisão: /
- Divisão inteira: //
- Resto da divisão: %
- Potencia: **

"""
# > Operadores Booleanos
idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 2.0
print(idade1 > idade2)  # Maior que
print(idade1 <= idade2) # Menor ou igual a
print('Python' == 'python')  # Igual a
print('Python' != 'Abaxi')  # Diferente de
