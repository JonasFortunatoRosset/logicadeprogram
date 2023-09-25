# 14) Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista.
from operator import index

lista = ['arroz', 'batata', 'feijao', 'milho']
if 'arroz' in lista:
    print(f"O elemento arroz está na lista na posição {lista.index('arroz')}")
else: 
    print("O elemento não está na lista")