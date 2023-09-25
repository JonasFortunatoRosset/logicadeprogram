# 13) Escreva um Programa que leia uma lista de 5 números inteiros, mostre a soma deles
print("----------Digite 5 Números-----------------")
lista = []
for i in range(5):
    lista.append(int(input(f"Digite o número{i + 1}: ")))
print(f"A soma dos itens da lista é {sum(lista)}")