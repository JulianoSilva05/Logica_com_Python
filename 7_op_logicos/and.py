#Operador AND
'''
O operador and vai copmparar um booleano com outro;
Podemos utilizar com duas comparações;
O resultado do operador and também será um boolean;
O and só retorna True se ambos os valores forem True
'''
#Tabela Verdade
'''
A   |   B   |   A AND B
0   |   0   |     0
0   |   1   |     0
1   |   0   |     0
1   |   1   |     1
'''
a = 5
b = 10
c = 2
d = 8

print(a > b and c > d)
print(a > b and c < d)
print(c < d and b < c)
print(not a < b and c > d)
print(not a > b and c > d)

print(a < b and b > c)