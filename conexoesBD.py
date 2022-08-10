import mysql.connector

dbconfig = {'host': '127.0.0.1', 'user': 'root', 'password': 'password', 'database': 'mycodinggamedb'}

def log(email, senha):
    logmail = email
    logsenha = senha
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    if logmail != "" and logsenha != "":
        parametro = tuple(logmail)
        _SQL = """select * from usuario where email = '"""+logmail+"""';"""
        cursor.execute(_SQL)
        res = cursor.fetchall()
        if len(res) > 0:
            for row in res:
                id, nome, palavrapasse, nivel, emailLogin = row
                print(row)
                print(palavrapasse+" = "+logsenha)
                if palavrapasse == logsenha:
                    print(nome)
                    return nome
                else:
                    print("Pois é "+nome+", a condição falhou")
                    return nome
