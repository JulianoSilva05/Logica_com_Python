#Conversão de dados
'''
• Os dados que vem da função input são do tipo string;
• Ou seja, se quisermos utilizar um número para realizar uma soma precisamos conver seu tipo;
• A função int() vai converter para inteiro;
• A função float() vai converter para ponto flutuante;
'''
numero_texto = input("Digite um numero:")
print(type(numero_texto))# essa linha de codigo retorna o tipo de dado da string numero_texto
numero = int(numero_texto) # aqui, criamos uma variavel "numero" que recebe a conversão o numero_texto de string para interiro
print(type(numero)) #imprime o tipo da variavel numero
#podemos também já converter a string para numero assim que o usuario digitar, desta forma já salva como interio

numero_int = int(input("Digite um numero: "))
print(type(numero_int))

dinheiro_carteira = float(input("Digite o dinheiro que tem na carteira: "))
print(dinheiro_carteira)
dinheiro_banco = input("Digite o dinheiro que possui na conta bancaria: ")
dinheiro_convertido = float(dinheiro_banco)
dinheiro_total = dinheiro_carteira + dinheiro_convertido
print("Você possui R$%.2f na carteira e R$%.2f no banco! Ao todo, vou possui R$%.2f" %(dinheiro_carteira, dinheiro_convertido, dinheiro_total))