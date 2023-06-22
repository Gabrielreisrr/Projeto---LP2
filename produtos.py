import sqlite3
from datetime import date 
from tabulate import tabulate
import limpaConsole
import carregaTela

valores = [
    (None, "Produto 1", "2023-06-20", "700.00"),
    (None, "Produto 2", "2023-06-21", "1500.00"),
    (None, "Produto 3", "2023-06-22", "800.00"),
    (None, "Produto 4", "2023-06-23", "760.00"), 
]

class Produtos:

  def __init__(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()
    self.idProduto = ""
    self.idFuncionario = ""
    self.nomeProduto = ""
    self.dataInclusao = ""

  def gerarProdutosIniciais(self):
        self.cursor.execute("SELECT COUNT(*) FROM produtos")
        resultado = self.cursor.fetchone()
        quantidade = resultado[0]
        if quantidade == 0:
            self.cursor.executemany("""
                INSERT INTO produtos (idFuncionario, nomeProduto, dataInclusao, valor)
                VALUES (?, ?, ?, ?)
            """, [(None,) + valor[1:] for valor in valores])
            self.conn.commit()
            return "Produtos iniciais gerados com sucesso!"
        else:
            return "Os produtos já foram gerados anteriormente."

  def mostrarProdutos(self):
    self.cursor.execute("SELECT * FROM produtos")
    resultado = self.cursor.fetchall()
    headers = ["idProduto", "idFuncionario", "nomeProduto", "dataInclusao", "valor"]
    print(tabulate(resultado, headers=headers, tablefmt="fancy_grid"))

  def adicionarProduto(self, infos):
    self.cursor.execute("INSERT INTO produtos (idFuncionario, nomeProduto, dataInclusao, valor) VALUES (?, ?, ?, ?);", infos)
    self.conn.commit()
    print("\033[31mProduto inserido com sucesso!\033[0m")
    print("\n Formatação do produto inserido:\n")
    produtoNome = (infos[1], )
    self.cursor.execute("SELECT * FROM produtos WHERE nomeProduto = ?", produtoNome)
    resultado = self.cursor.fetchall()
    headers = ["idProduto", "idFuncionario", "nomeProduto", "dataInclusao", "valor"]
    print(tabulate(resultado, headers=headers, tablefmt="fancy_grid"))

  def puxaValor(self, id):
    self.cursor.execute("SELECT valor from produtos WHERE idProduto = ?" , id)
    resultado = self.cursor.fetchone()
    return resultado[0]

  def verificaId(self, id):
    self.cursor.execute("SELECT COUNT(*) FROM produtos WHERE idProduto = ?", (id,))
    resultado = self.cursor.fetchone()
    quantidade = resultado[0]
    if quantidade > 0:
        return True  
    else:
        return False

  def alteraProduto(self, infos):
    self.cursor.execute("UPDATE produtos SET nomeProduto = ?, valor = ? WHERE idProduto = ?;", infos)
    self.conn.commit()
    return "Produtos atualizado com sucesso"

  def excluirProduto(self, idProduto):
    self.cursor.execute("DELETE FROM produtos WHERE idProduto = ?;", (idProduto,))
    self.conn.commit()
    return "Produto excluído com sucesso"
    
   

 

  
    
    
  