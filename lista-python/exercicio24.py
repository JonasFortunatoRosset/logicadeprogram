""" 24) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido. """
valor = float(input("Digite valor entre 0 e 10"))
while valor <10 or valor < 0:
    valor = float(input("Digite valor válido: "))
print(f"Seu valor é {valor}")