import pymysql.cursors
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

#extrair dado
with conexao.cursor() as cursor:
    cursor.execute('select * from cadastros')
    dados = cursor.fetchall()
for dado in dados:
    print(dado['nome'])