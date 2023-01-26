'''
Crie um programa que recebe a renda do usário;
Baseado na renda ele vai liberar um limite para o Cartão de crétido;
Se for menos de 2000, 1000 de limite;
Menos que 4000, 2000 de limite;
Menos 6000, 3000 de limite;
Se for maior que 10000, insira uma mensagem para falar com o gerente.
'''
salario = float(input("Digite o valor do seu salario: \n"))
if salario < 2000:
    limite = 1000
elif salario < 4000:
    limite = 2000
elif salario < 10000:
    limite = 3000
else:
    print("Fale com o gerente!")

print("para uma renda de R$",salario,"Seu limite é R$",limite)