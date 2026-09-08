print(12, 34)
# Utilizada para exibir coisas na tela
# Ela recebe um 'argumento' (normamente passa para uma função)

print('Teste')
# Pra duplicar a linha basta clicar nela e apertar Ctrl+C e em seguida Ctrl+V

# Por padrão, o Print imprime o 'argumento' dentro dele e aplica um espaço e a quebra de linha

print(25, 52, sep='-') # sep = Argumento Nomeado
print(4, 4, 5, sep=" + ") # Com o Sep, o separador que não fica visivel aparece pra nós
print(4, 5, 8, sep="a")
print(5, 4, 8, sep="\n") # \n quebra a linha
print(4, 5, 8, sep="a")
print(5, 4, 8, sep="\n", end=" = ") # end = final do print, final do ultimo argumento, nesse caso é o 8
print(5, 4, 8, sep="\n", end="\n=")