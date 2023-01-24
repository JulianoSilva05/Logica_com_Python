#Decomposição de string 2
'''
• Se omitirmos o valor da esquerda ou da direita, o Python vai entender que queremos resgatar algo desde o início ou até o fim;
• print(frase[:5])
• Podemos incluir posições negativas, que o Python vai contar pela direita;
• print(frase[-2:10])
• 
'''
frase = "O rato roeu a ropa do rei de Roma"
print(frase[:5])
print(frase[2:])
print(frase[0:-2])
print(frase[-14:])#conta de tras para frente

