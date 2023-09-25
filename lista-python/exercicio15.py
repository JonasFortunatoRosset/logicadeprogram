"""15) Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
tela dizendo se está “quente”, “frio” ou “agradável”. """
temperatura = int(input("Digite a temperatura do ambiente: "))
if temperatura < 15:
    print("Está frio")
elif((temperatura >= 15) & (temperatura < 28)):
    print("Está agradável")
else:
    print("Está quente")