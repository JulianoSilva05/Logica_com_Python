#Exercício 36
'''
Crie um programa que recebe o valor inteiro, que será considerado dinheiro;
Imprima na tela o número de células entregues ao usuário;
Ex.: Pediu 60 reias, recebeu uma nota de 50 e uma de 10;
As notas disponíveis são: 100, 50, 20, 10
Entregue as notas de maior valor para menor;
'''
saque = int(input("Valor do saque: "))
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota2 = 0
while saque > 0:
    while saque >= 100:
        nota100 = nota100 + 1
        saque = saque - 100
    while saque >= 50:
        nota50 = nota50 + 1
        saque = saque - 50
    while saque >= 20:
        nota20 = nota20 + 1
        saque = saque - 20
    while saque >= 10:
        nota10 = nota10 + 1
        saque = saque - 10
    while saque >= 2:
        nota2 = nota2 + 1
        saque = saque - 2
    break
if saque == 0:
    print("NOTAS de 100 = %d"%nota100)
    print("NOTAS de 50 = %d"%nota50)
    print("NOTAS de 20 = %d"%nota20)
    print("NOTAS de 10 = %d"%nota10)
    print("NOTAS de 2 = %d"%nota2)
else:
    print("Valor indisponivel para saque!")

