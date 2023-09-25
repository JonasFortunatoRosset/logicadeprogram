""" 25) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
 """
nome = input("Digite seu nome: ")
senha = input("Digite senha: ")
while senha == nome:
    senha = input("Digite uma senha válida: ")
print(f"Nome de usuário: {nome} e senha {senha}")