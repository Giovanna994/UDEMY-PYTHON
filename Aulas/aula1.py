# ----- aula 1 ------

#Permite escrever um comentário, não é multi-linha

"""
DocString, o Python lê o que fica escrito aqui e guarda na memória
Não é uma a forma correta de fazer um comentário
Porém pode ser usado como um
E é multi-linha
"""

print('Hello World!') #Permite mostrar um texto na tela

# ----- aula 6 ------

# Conversão de tipo, coerção
# type convertion, type casting, coercion = é o ato de converter um tipo em outro
# Tipos imutáveis e primitivos = str, int, float, bool

print(1+1)
print('a' + 'b')
print('1', type('1'))
print(int('1'), type(int('1')))
print(int('1') + 1)
print(float('1') + 1)
print(type(float('1') + 1))
print(bool('')) # vazio é considerado False
print(bool(' ')) # mesmo com apenas um espaço ou com algum caractere, é considerado True
print(str(11) + 'b')