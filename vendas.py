import sqlite3
from datetime import datetime,date
from tabulate import tabulate

class Vendas:
  def __init__(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()
    self.idVenda = ""
    self.idProduto = ""
    self.dataVenda = ""
    self.cpfCliente = ""
    self.valorTotal = 0
    self.tempoAberto = None
    
  def registrarVenda(self, idProduto, cpfCliente):
    dataVenda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    venda = (idProduto, dataVenda, cpfCliente)
    self.cursor.execute("INSERT INTO vendas (idProduto, dataVenda, cpfCliente) VALUES (?, ?, ?);", venda)
    self.conn.commit()
    print("Venda registrada com sucesso!")

  def fecharCaixa(self, valorDia):
    try:
      self.cursor.execute("SELECT SUM(p.valor) FROM vendas v INNER JOIN produtos p ON v.idProduto = p.idProduto;")
      resultado = self.cursor.fetchone()
      self.valorTotal = resultado[0] if resultado[0] else 0

      self.cursor.execute("SELECT MIN(dataVenda), MAX(dataVenda) FROM vendas;")
      resultado = self.cursor.fetchone()
      dataInicio = resultado[0]
      dataFim = resultado[1]
      self.tempoAberto = None
      if dataInicio and dataFim:
        dataInicio = datetime.strptime(dataInicio, "%Y-%m-%d %H:%M:%S")
        dataFim = datetime.strptime(dataFim, "%Y-%m-%d %H:%M:%S")
        self.tempoAberto = dataFim - dataInicio

      print(f"Valor total de vendas da loja: R$ {self.valorTotal:.2f}")
      print(f"Valor total de vendas do caixa: R$ {valorDia}")
      if self.tempoAberto is not None:
        print(f"Tempo de funcionamento do caixa: {self.tempoAberto}")
    except:
      print("Erro ao fechar caixa")

  def mostraVendas(self):
    self.cursor.execute("SELECT * FROM vendas")
    resultado = self.cursor.fetchall()
    headers = ["idVenda", "idProduto", "dataVenda", "cpfCliente"]
    print(tabulate(resultado, headers=headers, tablefmt="fancy_grid"))

  def vendaDia(self):
    data = date.today()
    self.cursor.execute("SELECT SUM(p.valor) AS valor_total FROM vendas v INNER JOIN produtos p ON v.idProduto = p.idProduto WHERE DATE(v.dataVenda) = ?", (data,))
    resultado = self.cursor.fetchone()
    return resultado[0]
          


