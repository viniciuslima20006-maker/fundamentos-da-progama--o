# Estrutura de repetição
#if (se) -> Verifica se uma codição é true (verdadeire) .Se for, ele executa o codigo
# elif (senão se) -> é usado para testar varias condições. Ele só executa se as condições anteriores forem falsas.
# else (senão) -> executa o código se a condição if for false.

# idade_usuario = 15   
# # se o usuario for maior de 18 anos , eu vou passar a informacao;vc é maior de idade , senao vc e menor de idade 

# if idade_usuario >= 18:
#     print("voce e maior de idade")
# else:
#     print("voce e menor de idade")

idade= 73
if idade >=18:
    print ("voce e maior de idade.")
elif idade >= 0 and idade <18:
    (" você jovem de idade.")
elif idade>= 70:
    print("você é experiente de idade.")
else:
    prin("Você é menor de idade")