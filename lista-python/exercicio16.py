""" 16) Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
conversão.
 """
print("-------Escolha o tipo de conversão------")
temperatura = (input(f"1 - Fahrenheit para Celsius \n"
                      "2 - Celsius para Fahrenheit \n"))
if temperatura == 1:
    fahrenheit = float(input("Digite a temperatura: "))
    print(f"A temperatura convertida é {(fahrenheit - 32) / 1.8}")
elif (temperatura == 2):
    celsius = float(input("Digite a temperatura: "))
    print(f"A teperatura convertida para Fahrenheit é {celsius * 1.8 + 32}")