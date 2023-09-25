# Diferenca entre while e for
# While se usa quando nao se sabe o fim, enquanto for vdd a condicao ira rodar
# O for vai executar quando se sabe o fim do laco

decisao = 0

while decisao != 3:
    decisao = int(input('digite 1 para logar 2 paraq cadastrar e 3 para sair'))

    if decisao == 1:
        print('logando')
    elif decisao == 2:
        print('cadastrando')
    else:
        print('sair')

# contem o 3 parametro que e para dizer se e de forma crescente ou decrescente
for i in range(1, 1001):
    print(i)

for i in range(0, 11):
    for j in range(0, 11):
        print(f'{i} x {j} = {i*j}')