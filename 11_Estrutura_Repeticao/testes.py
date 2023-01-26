'''
n = int(input("Tabuada de:"))
x = 1
while x <= 10:
    print(n," x ",x," = ",n*x)
    x=x+1

fim = int(input("Contar os impares até: "))
num = 1
while num <= fim:
    if num % 2 != 0:
        print(num)
    num = num + 1
'''
n = 1
soma = 0
while n <= 10:
 x = int(input("Digite o %d número:"%n))
 soma = soma + x
 n = n + 1
print("Soma: %d"%soma)