# Estrutura else
'''
• A estrutura else vai ocorrer apenas quando o if não for executado;
• Ou seja, podemos executar outra parte do código para uma situação inversa do if;
• Exemplo:
    if condição:
        código
    else:
        código
'''
poupanca = 200
saque = float(input("Quanto deseja sacar?\n"))

if saque <= poupanca:
    print("Saque no valor de R$%.2f autorizado"%saque)
    print("Seu novo saldo é de R$%.2f"%(poupanca - saque))
else:
    print("Saldo insuficiente, seu saldo é R$%.2f"%poupanca)