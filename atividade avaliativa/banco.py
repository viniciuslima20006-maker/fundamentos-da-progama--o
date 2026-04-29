#alunos cadastrados

quantidade=int(input("Digite a quantidade de alunos cadastrados: "))

turma=[]

for i in range(quantidade):

    nome= input("Digite o nome do aluno: ")
    nota1=float(input("Digite a nota do aluno: "))
    nota2=float(input("Digite a nota do aluno: "))
    nota3=float(input("Digite a nota do aluno: "))

    media = (nota1+nota2+nota3)/3

    if media >= 7.0:
            situação= "aprovado"
    if media >=5.0 and media <7.0:
            situação= "recuperação"
    if media<5:
        situação= "reprovado"    

    aluno= ([nome,nota1,nota2,nota3,media,situação])
    turma.append(aluno)

print ("---Resumo da turma---")
for aluno in turma:
 print(f"Nome: {aluno[0]}, Nota 1: {aluno[1]}, Nota 2: {aluno[2]}, Nota 3: {aluno[3]}, Média: {aluno[4]:.2f}, Situação: {aluno[5]}")

