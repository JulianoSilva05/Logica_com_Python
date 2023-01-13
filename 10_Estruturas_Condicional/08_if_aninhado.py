# If aninhado
'''
• Um if pode estar dentro de outro if
• Chamamos esse recurso de ESTRUTURA ANINHADAS
• Este tipo de lógica nos permite criar regra ainda mais complexas e personalizadas para nossa aplicação
'''
idade = int(input("Digite sua idade:\n"))
if idade >= 18:
    print("Pode entrar na balada")

    metodo_pagamento = input("Como você deseja pagar? digite: dinheiro ou cartão\n")
    if metodo_pagamento == "dinheiro":
        print("Fila para pagamento em dinheiro é a da esquerda!")
    else:
        print("Pagamento em cartão é a fila da direita!")
else:
    print("Não pode entrar na balada!")