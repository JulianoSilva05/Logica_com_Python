#Exercício 19
'''
• Escreva um programa que recebe uma base e uma potência;
• Exiba o resultado na tela;
'''
base = int(input("Digite o numero base da equação: \n"))
expoente = int(input("Digite a potência: \n"))
calculo = base**expoente
print("O numero %d elevado à %d é %d" % (base, expoente, calculo))