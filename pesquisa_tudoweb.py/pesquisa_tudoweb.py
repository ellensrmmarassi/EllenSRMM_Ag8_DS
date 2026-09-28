# Pesquisa de Satisfacao - TudoWeb
# Contadores de Repostas
excelente = 0
bom = 0
ruim = 0

for i in range (1,51):
    print(f"\nEntrevistado {i}")
    nome = input("Digite seu nome :  ")
    idade = int(input("Digite sua idade :  "))

    print(f"\nNome : {nome} - Idade : {idade} anos")

    print("\nAvalie o atendimento :  ")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opcao :  "))

# Verifica a opiniao do entrevistado
if opiniao == 1 :
    excelente += 1
    print("Resposta registrada : EXCELENTE ")
elif opiniao == 2 :
    bom += 2
    print("Resposta registrada : BOM ")
elif opiniao == 3 :
    ruim += 3
    print("Resposta registrada : RUIM ")
else:
    print("Resposta invalida ! ")

print("\nResultado da Pesquisa")
print(f"Total de respostas EXCELENTE : {excelente}")
print(f"Total de respostas BOM : {bom}")
print(f"Total de respostas RUIM : {ruim}")