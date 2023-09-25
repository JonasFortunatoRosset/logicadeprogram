# 11) Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E ao final mostrar seu nome e salário final calculado.
nome = input("Digite seu nome: ")
horas = float(input("Digite horas trabalhadas: "))
valor = float(input("Digite o valor a ser recebido por hora trabalhada: "))
salariobruto = horas * valor
print(f"Seu salário bruto é {salariobruto}")
print(f"{nome}, Seu salário com 2% de desconto do INSS é {salariobruto - (salariobruto * 0.02)}")