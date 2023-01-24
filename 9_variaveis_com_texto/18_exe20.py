# Exercício 20
'''
• Crie um programa que recebe o saldo de um conta bancária com R$359.56;
• Depois insira uma nova quantia por meio de input;
• E remova um valor de R$125,98, referente a fatura de cartão de crédito;
• Imprima o valor da conta após as operações com string dinâmica;
'''
saldo = 359.56
fatura_cartao = 125.98
deposito = float(input("Qual o valor depositado: \n"))

saldo = saldo + deposito - fatura_cartao
print("Fatura do Cartão: R$%.2f \nDeposito em conta: R$%.2f\nSaldo: R$%.2f" % (fatura_cartao, deposito, saldo))
