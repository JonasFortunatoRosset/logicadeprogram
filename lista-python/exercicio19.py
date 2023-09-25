""" 19) Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
a. Soma de 2 n´umeros.
b. Diferença entre 2 números (maior pelo menor).
c.Produto entre 2 números.
d. Divisão entre 2 números (o denominador não pode ser zero).
 """
num1 = float(input("Digite num1:")) 
num2 = float(input("Digite num2:")) 
print("------------MENU-----------")
escolha = int(input("1 - Soma de 2 números \n"
                    "2 - Diferença entre 2 números (maior pelo menor).\n "                
                    "3 - Produto entre 2 números. \n"
                    "4 - Divisão entre 2 números (o denominador não pode ser zero)."))
num3 = max(num1, num2)
num4 = min(num1, num2)
while escolha<1 or escolha > 4:
    escolha = int(input("Digite novamente: "))
if escolha == 1:
    print(f"A soma é {num1 + num2}")
elif(escolha == 2):
    print(f"A diferença entre os números é de {num3 - num4}")
elif(escolha == 3):
    print(f"O produto entre {num1} e {num2} é {num1 * num2}")
else:
    print(f"A divisão entre os 2 números é {num3 / num4}")
