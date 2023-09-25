""" 17) Fac¸a um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde h corresponde à altura):
• Homens: (72.7 ∗ h) − 58
• Mulheres: (62, 1 ∗ h) − 44, 7 """
altura = float(input("Digite sua altura: "))
sexo = input("Digite M - masculino e F - feminino").upper()
if sexo == 'M':
    print(f"Seu peso ideia é {72.7 * altura - 58}")
elif(sexo == 'F'):
    print(f"Seu peso ideal é {(62, 1 * altura) - 44, 7}")
else:
    print("Você digitou incorretamente")
