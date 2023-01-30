#Exercicio 34
'''
Crie um loop que exibe os números digitados do usúario na tela;
O loop deve ser cancelado quando o usuário digitar 0;
'''
x = 0
while x < 1:
    numero = int(input("Digite um numero: "))
    print(numero)

    if numero == 0 :
        print("Saindo do loop: ")
        break