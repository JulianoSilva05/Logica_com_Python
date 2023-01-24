#Exercício 18
'''
• Crie uma variavel que receba um valor como salário;
• E outro coma que receba a procentagem de aumento;
• Exiba o valor total após o aumento!
'''
salario = float(input("Digite seu salario; \n"))
aumento = float(input("Digite o aumento em porcentagem: \n"))
salario_novo = salario * (aumento/100) + salario
print("Seu novo salario é R$%.2f" % salario_novo)