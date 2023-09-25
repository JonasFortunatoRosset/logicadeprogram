""" 23) Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
não continuar a escrever valores. """
lista = []
while True:
    num = int(input("Digite um num int: "))
    continuar = input("Digite S ou N para continuar a adicionar valores").upper()
    if continuar == 'N':
        break
    lista.append(num)
print(f"A média dos valores é {num / len(num)}")
print(f"O maior valor é {max(num)}")
print(f"O maior valor é {min(num)}")