#Expressões lógicas
'''
Os operadores lógicos podem ser combinados em expressões lógicas;
As expressões lógicas consistem em duas comparações com um operador lógico entre estas;
Desta maneira resumimos o código e também podemos criar mais variedades de comparações;
Ex.:
idade > 18 and passaporte == True
'''
idade = 18
carteiraMotorista = True

print(idade >= 18 and carteiraMotorista == True)
print("Se True: Pode dirigir")
print("Se False: Não pode dirigir")

velocidade = 120
radar = 100
radarFuncionando = True

print(velocidade > radar and radarFuncionando == False)#True and False = False
print("Se True: Multado")
print("Se False: Não recebe multa")

print(velocidade > radar and not radarFuncionando == False)#True and True = True
print("Se True: Multado")
print("Se False: Não recebe multa")


    