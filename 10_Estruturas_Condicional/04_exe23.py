# Exercício 23
'''
• Escreva um programa que leia dosi números;
• Depois imprima o maior deles;
'''
num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número: \n"))
if num1 > num2:
    print("O %d é maior que %d"%(num1, num2))
if num1 < num2:
    print("O %d é maior que %d"%(num2,num1))
if num1 == num2:
    print("Os dois numeros são iguais")