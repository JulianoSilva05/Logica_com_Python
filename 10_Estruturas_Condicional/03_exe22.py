# Exercício 22
'''
• Crie um programa que recebe o número de rodas que o veículo possui;
• Se for mais que 2, imprima uma mensagem para pagar pedágio;
• Se for igual a 2, imprima uma mensagem dizendo que pode passar livremente;
'''
num_rodas = int(input("Digite a quantidade de rodas do seu veiculo: \n"))
if num_rodas >2:
    print("Paga pedagio!")

if num_rodas <= 2:
    print("Passa direto!")