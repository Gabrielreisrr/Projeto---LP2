import sqlite3

def gerarBanco(banco):
  conn = sqlite3.connect(banco)
  cursor = conn.cursor()

  #Criando tabelas (FUNCIONARIOS, CHAVEACESSO, PRODUTOS e VENDAS).
  try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "funcionarios"(
                           "idFuncionario" INTEGER NOT NULL,
                           "nomeCompleto" TEXT NOT NULL,
                           "CPF" INTEGER NOT NULL,
                           "dataCadastro" TEXT NOT NULL,
                           
                           PRIMARY KEY ("idFuncionario" AUTOINCREMENT)); 
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "chaveAcesso"(
                            "idChave" INTEGER NOT NULL,
                            "idFuncionario" INTEGER NOT NULL,
                            "chave" TEXT NOT NULL,
                            
                            PRIMARY KEY ("idChave" AUTOINCREMENT),
                            FOREIGN KEY ("idFuncionario") REFERENCES funcionarios("idFuncionario"));
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "produtos"(
                             "idProduto" INTEGER NOT NULL,
                             "idFuncionario" INTEGER,
                             "nomeProduto" TEXT NOT NULL,
                             "dataInclusao" TEXT NOT NULL,
                             "valor" TEXT NOT NULL,
                             
                             PRIMARY KEY ("idProduto" AUTOINCREMENT),
                             FOREIGN KEY ("idFuncionario") REFERENCES funcionarios("idFuncionario"));
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "vendas"(
                               "idVenda" INTEGER NOT NULL,
                               "idProduto" INTEGER NOT NULL,
                               "dataVenda" TEXT NOT NULL,
                               "cpfCliente" INTEGER NOT NULL, 

                               PRIMARY KEY ("idVenda" AUTOINCREMENT),
                               FOREIGN KEY ("idProduto") REFERENCES produtos("idProdutos"));
    """)

    print(f"\033[31mA criação do Banco {banco} foi bem sucedida!\033[0m")
    return conn
  except sqlite3.Error as error:
    print(error) #definição para erro de abertura do banco.
