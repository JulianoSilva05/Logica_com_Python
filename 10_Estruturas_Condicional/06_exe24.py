# Exercício 24
'''
• Crie um programa com a variável salario;
• Se for maior que 1800 imprima uma mensagem de que é nescessário pagar imposto de renda;
• Se não imprima uma menagem que não precisa pagar IR;
'''
salario = float(input("Digite valor do seu salario: \n"))
if salario > 1800:
    print("Paga IR!")
else:
    print("Não paga IR")