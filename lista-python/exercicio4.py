# 4) Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre ele.
elemento = input("Digite algo: ")
print(f"O tipo de dado de {elemento} é {type(elemento)}")
print(f'o elemento é maiúsculo: {elemento.isupper()}')
print(f'o elemento é minúsculo: {elemento.islower()}')
print(f'o elemento é uma letra: {elemento.isalpha()}')
print(f'o elemento é numérico: {elemento.isnumeric()}')
print(f'o elemento é só espaço: {elemento.isspace()}')
print(f'o elemento é alfanumérico: {elemento.isalnum()}')
print(f'o elemento é capitalizada: {elemento.istitle()}')