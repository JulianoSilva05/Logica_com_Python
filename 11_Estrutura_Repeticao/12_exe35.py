#Exercicio 35
'''
Crie um loop que detecta se um número é primo ou não;
Número primo é o número que é dividido apenas por ele mesmo e o número 1;
'''
numero = int(input("Digite um numero: "))
divisoes = 0
contador = numero
'''
Logica: vou começar com o numero digitado, divido ele por ele mesmo e vou decrescendo em 1, e faço a verificação.
Declaro uma variavel contador para receber o valor digitado em "Numero".
Não posso alterar o valor de "NUMERO" por isso crio outra variavel para receber esse numero!
'''
while contador > 0:
    if numero % contador == 0:
        divisoes = divisoes + 1
    contador = contador - 1

if divisoes == 2 :
    print("O numero %d é primo"%numero)
else:
    ("Numero não é primo")