#Exercício 13
'''
• Crie uma string dinâmica exibindo o seu nome e a sua idade;
• Crie uma outra string dinâmica exibindo uma quantidade de dinheiro que você possui(Coloque centavos)
'''
nome = "Juliano"
idade = 21
print("Meu nome é %s e tenho %d"%(nome,idade))
#Exibindo só as duas primeiras letras do meu nome 
print("Meu nome é %.2s e tenho %d"%(nome,idade))

dinheiro = 20.556677
print("Meu nome é %s, tenho %d e tenho R$%.2f" % (nome , idade , dinheiro))