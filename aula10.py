arquivo = open('aulaPython.txt', 'w') # coloca w para escrever
arquivo = open('aulaPython.txt', 'a') # coloca a para alterar
arquivo = open('aulaPython.txt', 'r') # coloca r para ler

# texto = 'oi Tudo bem com voce?'
# texto = arquivo.read()
texto = arquivo.readline()
# arquivo.write(texto)
print(texto)

arquivo.close()
