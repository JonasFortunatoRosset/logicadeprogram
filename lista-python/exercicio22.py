""" 22) Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
Desconsiderando o valor 1000 da parada. """
lista = []
while True:
    num = int(input("Digite um num int: "))
    if num == 1000:
        break
    lista.append(num)
print(f"A quantidade de números digitados é {len(lista)} e a soma é {sum(lista)}")