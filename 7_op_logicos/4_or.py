#Operador OR
'''
O operador or vai comparar um boobeano com outro;
Podemos utilizar com duas comparações;
O resultado do operador and também será um boolean;
'''
# → O and só retorna FALSE se ambos valores forem FALSE;
#Tabela Verdade
'''
A   |   B   |   A OR B
0   |   0   |     0
0   |   1   |     1
1   |   0   |     1
1   |   1   |     1
'''
a = 5
b = 10
print(a > b or b == 11)
print(b > a or b == 10)
print(a > b or b == 10)
print(b > a or b == 20)

nome = "Juliano"
idade = 33
print(nome == "Juliano" or idade < 33)