# Exercício 25
'''
• Escreva um programa que recebe dois números;
• Insira a multiplicação entre eles em uma variável;
• Se for menor ou igual a 100 o resultado, insira uma mensagem de que o número é baixo;
• Se não, o número é alto;
'''
num1 = float(input("Digite um numero:\n"))
num2 = float(input("Digite outro numero:\n"))
multiplicacao = num1 * num2
if multiplicacao <= 100 :
    print("Número baixo")
else:
    print(multiplicacao)
    print("Numero alto")