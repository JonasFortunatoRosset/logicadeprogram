# 9) Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para Euros.
nome = input("Digite seu nome: ")
real = float(input("Digite a quantidade de dinheiro que você possui em reais: "))
print(f"O valor convertido para dolares é {real/5.41}")
print(f"O valor convertido para euros é {real/5.43}")
