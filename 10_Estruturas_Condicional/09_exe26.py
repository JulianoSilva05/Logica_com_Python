# Exercício 26
'''
• Escreva um programa que recebe um número;
• Verifique se o número é maior que 10, se não for, imprima uma mensagem avisando que para prosseguir precisa ser maior que 10;
• No primeiro if, verifique se o número é menos que 20, e imprima a multiplicação dele por 2;
• Se não, imprima o número multiplicado por 5;
'''
num = float(input("Digite um numero:\n"))
if num > 10:
    if num > 20:
        print("Numero x 2: %.1f"% (num*2))
    else:
        print("Numero x 5 = %.1f" % (num * 5))

else:
    print("Digite um valor acima de 10, por favor!")