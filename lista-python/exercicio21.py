""" 21) Crie um programa que leia dois valores e mostre na tela um menu :
a. Somar
b. Multiplicar
c. Maior
d. Menor
e. Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
"""
valor1 = float(input("Digite num1:")) 
valor2 = float(input("Digite num2:")) 
x = True
while x == True:
    print("------------MENU-----------")
    escolha = int(input("1 - Soma de 2 números \n"
                        "2 - multiplicar\n "                
                        "3 - maior \n"
                        "4 - menor \n"
                        "Qualquer outro valor - Sair"))
    if (escolha == 1):
        print(f"A soma correspondente é {valor1 + valor2}")
    elif (escolha == 2):
        print(f"O numero {valor1} x {valor2} é {valor1 *  valor2}")
    elif (escolha == 3):
        print(f"O valor maior é {max(valor1, valor2)}")
    elif (escolha == 4):
        print(f"O valor menor é {min(valor1, valor2)}")
    else:
        x = False