""" 18) Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.
 """
prova1 = float(input("Digite nota prova1: "))
while (prova1 > 5) or (prova1 < 0):
    prova1 = float(input("Digite novamente a nota prova1: "))

prova2 = float(input("Digite nota prova2: "))
while prova2 > 5 or prova2 < 0:
    prova2 = float(input("Digite novamente a nota prova2: "))

prova3 = float(input("Digite nota prova3: "))
while prova3 > 10 or prova3 < 0:
    prova3 = float(input("Digite novamente a nota prova3: "))
media = prova1 + prova2 + prova3
if media >= 6:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")