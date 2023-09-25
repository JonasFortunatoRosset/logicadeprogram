# 7) Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15% de aumento.
produto = float(input("Escreva o valor do produto: "))
print(f"O valor do produto com 5% de desconto é {produto - (produto * 0.05)}")
print(f"O valor do produto com 15% de aumento é {produto + (produto * 0.15)}")