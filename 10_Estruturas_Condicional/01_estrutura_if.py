#Estrutura de condição
'''
• A estrutura de condição serve para criar uma bifurcação no nosso código;
• Ou seja, executar um determinado trecho apenas se uma condição for verdadeira;
• A mais famosa é a estrutura if, porém também temos else e elif;
'''
# Estrutura IF
'''
• O if vai receber uma condição, que se for avaliada como VERDADEIRA o software entra em um bloco de código diferente;
• Caso a condição não seja verdadeira, o bloco é ignorado;
• A estrutura e sintaxe é a seguinte:
if condicao:
    bloco a ser executado

'''
if 10 > 5:
    verdura = "Cenoura"
    print("Entrou no IF")
    print(verdura)
print("Está sem o 'tab', é impresso depois do IF")

print("#"*80)

nome = "Juliano"
idade = 21
if nome == "Juliano" and idade == 21:
    print("Oi Juliano")

