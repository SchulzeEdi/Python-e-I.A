import matplotlib.pyplot as plt
import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='cursopython',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

autentico = False

def logarCadastrar():
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False

    if decisao == 1:
        nome = input('digite seu nome')
        senha = input('digite sua senha')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False
        if not autenticado:
            print('email ou senha errado')
    elif decisao == 2:
        print('Faca seu cadastro')
        nome = input('Digite seu nome')
        senha = input('Digite sua senha')

        for linha in resultado:
            if nome == linha['nome']:
                usuarioExistente = 1
        if usuarioExistente == 1:
            print('Usuario ja cadastrado')
        elif usuarioExistente == 0:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastros(nome, senha, nivel) VALUES (%s, %s, %s)', (nome, senha, 1))
                    conexao.commit()
                print('Usuario cadastrado com sucesso!')
            except:
                print('erro na hora de inserir dado')
    return autenticado, usuarioMaster

def cadastrarProduto():
    nome = input('Digite o nome do produto')
    ingrediente = input('Digite os ingredientes do produto')
    grupo = input('Digite o grupo pertencente a esse produto')
    preco = float(input('Digite o preco deste produto'))
    try:
        with conexao.cursor() as cursor:
            cursor.execute('insert into produtos(nome, ingredientes, grupo, preco) values (%s, %s, %s, %s)', (nome, ingrediente, grupo, preco))
            conexao.commit()
            print('Produto cadastrado com sucesso')
    except:
        print('Erro ao inserir os produtos no banco de dados')

def listarProdutos():
    produtos = []
    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtosCadastrados = cursor.fetchall()
    except:
        print('erro ao lista os produtos')
    for i in produtosCadastrados:
        produtos.append(i)
    if len(produtos) == 0:
        print('Nenhum produto cadastrado')
    else:
        for i in range(0, len(produtos)):
            print('ID:{id}, Nome:{nome}, preco:{preco}'.format(id=produtos[i]['id'], nome=produtos[i]['nome'], preco=produtos[i]['preco']))

def excluirProdutos():
    idDeletar = int(input('Digite o id referente ao produto que deseja apagar'))
    try:
        with conexao.cursor() as cursor:
            cursor.execute('delete from produtos where id = {}'.format(idDeletar))
            print('Produto excluido com sucesso')
    except:
        print('Erro ao excluir o produto')

def listarPedidos():
    pedidos = []
    decision = 0
    while decision != 2:
        pedidos.clear()
        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                listaPedidos = cursor.fetchall()
        except:
            print('Erro ao listar pedidos')

        for i in listaPedidos:
            pedidos.append(i)

        if len(pedidos) != 0:
            for i in range(0, len(pedidos)):
                print(pedidos[i])
        else:
            print('Nenhum pedido foi feito')

        decision = int(input('Digite 1 para dar um produto como entregue e 2 para voltar'))
        if decision == 1:
            idDeletar = int(input('Digite o id do pedido entregue'))
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete from pedidos where id = {}'.format(idDeletar))
                    print('Produto dao como entregue')
            except:
                print('Erro ao dar pedido como entregue')

def gerarEstatistica():
    nomeProdutos = []
    nomeProdutos.clear()

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtos = cursor.fetchall()
    except:
        print('Erro ao fazer consulta no banco de dados')

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from estatisticaVendido')
            vendido = cursor.fetchall()
    except:
        print('Erro ao realizar a consulta no banco de dados')

    estado = int(input('Digite 0 para sair, 1 para pesquisar por nome e 2 para pesquisar por grupo'))

    if estado == 1:
        decisao3 = int(input('Digite 1 para pesquisar por dinheiro e 2 por quantidade unitaria'))
        if decisao3 == 1:
            for i in produtos:
                nomeProdutos.append(i['nome'])

            valores = []
            valores.clear()
            for h in range(0, len(nomeProdutos)):
                somaValor = -1
                for i in vendido:
                    if i['nome'] == nomeProdutos[h]:
                        somaValor += i['preco']
                if somaValor == -1:
                    valores.append(0)
                elif somaValor > 0:
                    valores.append(somaValor+1)
        plt.plot(nomeProdutos, valores)
        plt.ylabel('quantidade vendida em reais')
        plt.xlabel('produtos')
        plt.show()

while not autentico:
    decisao = int(input('digite 1 para logar e 2 para cadastrar'))
    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()
    except:
        print('erro ao conectar ao banco de dados')
    autentico, usuarioSupremo = logarCadastrar()

if autentico:
    print('autenticado')
    decisaoUsuario = 1

    while decisaoUsuario != 0:
        decisaoUsuario = int(input('Digite 0 para sair, 1 para cadastrar produtos, 2 para listar os produtos cadastrados, 3 para excluir um produto e 4 para acessar os pedidos'))
        if decisaoUsuario == 1:
            cadastrarProduto()
        elif decisaoUsuario == 2:
            listarProdutos()
        elif decisaoUsuario == 3:
            listarProdutos()
            excluirProdutos()
        elif decisaoUsuario == 4:
            listarPedidos()
        else:
            gerarEstatistica()