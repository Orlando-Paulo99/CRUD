import mysql.connector

banco=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="dbinfox"
)
cursor=banco.cursor()

pergu=int(input(" 1-Cadastra\n 2-Pesquisar\n 3-Atualizar\n 4-Deletar"))
if( pergu==1):
    nome=input("Nome do aluno")
    endereco=input("Endereço do aluno")
    fone=int(input("Telefone do aluno"))
    email=input("E-mail do aluno")
    
    cadastro="INSERT INTO dbclientes(nome,endereco,fone,email) VALUES(%s ,%s ,%s ,%s)"
    vaiSql=(nome,endereco,fone,email)
    cursor.execute(cadastro,vaiSql) 
    banco.commit()
elif(pergu==2):
    pesquisa = "SELECT * FROM dbclientes "
    cursor.execute(pesquisa)
    # fetchall recebe tudo de pesquisa e retorna atraves de uma tupla
    resultado =cursor.fetchall()
    for x in resultado:
        print(x[0], x[1],x[2],x[3],x[4])

elif(pergu==3):
    pergunta=input("1--alterar endereço\n2-alterar telefone\n3-alterar e-mail")
    if pergunta=="1":
        id_cliente=input("digite seu id")
        novo_end=input("digite o novo endereço")
        comando=f"UPDATE dbclientes SET endereco='{novo_end}' WHERE idcli='{id_cliente}'"
        cursor.execute(comando)
        banco.commit()
    elif(pergunta=="2"):
        tell=input("digite seu novo telefone")
        id_cli=input("digite seu id")
        comand=f"UPDATE dbclientes SET fone='{tell}' WHERE idcli='{id_cli}'"
        cursor.execute(comand)
        banco.commit()
    elif(pergunta=="3"):
        novoEmail=input("digite seu novo e-mail")
        idC=input("digite seu id")
        comand=f"UPDATE dbclientes SET email='{novoEmail}' WHERE idcli='{idC}'"
        cursor.execute(comand)
        banco.commit()
    else:
        print("opção invalida")
elif(pergu==4):
    id_cli=input("qual seu o id que deseja deletar")
    comand=f"DELETE FROM dbclientes WHERE idcli='{id_cli}'"
    cursor.execute(comand)
    banco.commit()


else:
    print("opção errada")
