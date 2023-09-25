""" 20) Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se aposentar.
As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos """
idade = int(input("Digite sua idade: "))
tempo = int(input("Digite seu tempo de serviço:"))

if idade >= 65 or tempo >= 30 or idade >= 60 & tempo >= 25:
    print("Você pode se aposentar")
else:
    print("Infelizmente você ainda não pode se aposentar")
        