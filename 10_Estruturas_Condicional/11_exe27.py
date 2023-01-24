# Exercício 27
'''
• Crie um programa que receba a categoria, em valor numérico, de um produto;
• Se for 1 = Exiba "Bolsa"
• Se for 2 = Exiba "Tênis"
• Se for 3 = Exiba "Mochila"
• Caso não seja nenhum dos valores, exiba que a categoria não foi encontrada;
'''
categoria = int(input("Digite a categoria do produto: \n1 - Bolsa\n2 - Tênis\n3 - Mochila\n"))
if categoria == 1:
    print("A categoria escolhida foi Bolsa")
elif categoria == 2:
    print("A categoria escolhida foi Tênis")
elif categoria == 3:
    print("A categoria escolhida foi Mochila")
else:
    print("Categoria invalida")