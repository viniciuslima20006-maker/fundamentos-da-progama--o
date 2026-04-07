print("Sistema de Emprestimo Bancario")

#Entradas dos dados
idade = int(input("Digite a idade do Cliente:"))
salario = float(input("Digite o salario do cliente"))
tempo_trabalhando = int(input ("Digite o tempo de trabalho (em anos):"))

#Estruturas condicionais

if idade < 18:
    print("Emprestimo reprovado. Cliente menor de idade.")
elif salario >=  5000:
    print("Emprestimo aprovado automaticamente.")
elif idade >= 18 and salario >= 2000 and tempo_trabalhando >= 2:
    print("Emprestimo aprovado.")
else: 
    print("Emprestimo reprovado.")
#verificar a idade, salario e o tempo de trabalho
 