""" 26) Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).
 """

nome = input("Digite nome: ")
while len(nome) < 3:
    nome = input("Digite um nome válido: ")
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    idade = input("Digite um nome válido: ")
salario = float(input("Digite seu salário: "))
while salario < 0:
    salario = float(input("Digite um salário válido: "))
sexo = input("Digite seu sexo: m - masculino e f- feminino")
while sexo != 'm' or sexo != 'f':
    sexo = input("Digite um caracter válido: ")
estadocivil = input("Estado Civil: 's', 'c', 'v', 'd'")
lista = ['s', 'c', 'v', 'd']
while estadocivil != lista:
    estadocivil = input("Digite um estado civil válido: ")
