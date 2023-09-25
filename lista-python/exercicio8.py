# 8) Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input("Digite largura em metros: "))
altura = float(input("Digite altura em metros: "))
area = largura * altura
print(f"A área da parede é {area}m2 e a quantidade de litro de tinta necessária é {area / 2}Litros de tinta")