#Estrutura de repetição
'''
Uma forma de executar uma ação x vezes;
Evita repetição de código desnecessariamente;
A repetição será executada até satisfazer uma condição no código;
Esta condição é semelhante a que utilizamos no if, realizamos uma comparação
'''#❶
x = 1
while x<=3: #❷
    print(x) #❸
    x = x + 1 #❹

fim=int(input("Digite o último número a imprimir:")) #❶
x = 1
while x <= fim: #❷
    print(x) #❸
    x = x + 1 #❹
    