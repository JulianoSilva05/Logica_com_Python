# Estrutura elif
'''
• A estrutura elif é a forma que temos de escrever outrs ifs antes do else
• Podemos fazer mais chegagens no código, antes de retornar um else;
• Obs.: O else não é obrigatorio, podemos ter só if e elif
'''
nome = input("Digite seu nome:\n")

if nome == "Juliano":
    senha = "12345678"
    input("Digite sua senha:")
    if senha == "12345678":
        print("Bem vindo ao sistema, Juliano!")
    else:
        print("Senha incorreta!")
elif nome == "Alex":
    senha = "abc123456"
    input("Digite sua senha:\n")
    if senha == "abc123456":
        print("Bem vindo ao sistema, Alex!")
    else:
        print("Senha incorreta!")
else:
    print("Usário não cadastrado!")