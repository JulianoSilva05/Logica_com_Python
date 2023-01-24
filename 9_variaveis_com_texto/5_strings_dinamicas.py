#Strings dinâmicas
'''
• Podemos inserir variáveis em strings de outra maneira;
• E assim deixá-las DINÂMICAS, compondo elas com valores diferentes;
• O símbolo de composição é o %
• Porém cada tipo de dado tem um caractere diferente em seguida do %: d para inteiros, s para strings e f para floats
'''
nome = "Juliano"
print("Bom dia, %s"%nome)
idade = 21
print("Meu nome é %s e tenho %d anos"%(nome,idade))
