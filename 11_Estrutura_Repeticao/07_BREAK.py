#BREAK
'''
Com a instrução break podemos interromper uma repetição;
Ela pode ser inserida após determinada condição no código;
O break fará com que o loop seja cancelado totalmente, e o programa continua para a proxima linha de código;
'''
numero = 0
while numero < 10:
    print(numero)

    if numero == 5:
        break
    numero = numero + 1
print("Saiu do loop")

s=0
while True: 
    v=int(input("Digite um número a somar ou 0 para sair:"))
    if v==0:
        break 
    s = s+v 
print(s) 
