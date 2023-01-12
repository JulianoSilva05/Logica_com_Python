#Strings com decimais
'''
• Para inserir os decimais temos um sintaxe um pouco diferente dos demais tipos de dados;
• Por causa do número de casas decimais que vamos exibir;
• Ex.:
• print("Você tem R$%.2f no banco"%valor)
'''
valor = 20.30
print("Você tem R$%f no banco"%valor)#sem distinguir a quantidade de casas decimais, sempre mostra 6 casas decimais
print("Você tem R$%.2f no banco"%valor)#informando a quantidade de casas decimais

pi = 3.141592653
print("O valor de %.2f"%pi)

