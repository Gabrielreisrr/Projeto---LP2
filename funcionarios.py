import sqlite3
from tabulate import tabulate


class Funcionarios:

  
  def __init__(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()
    self.nomeCompleto = ""
    self.cpf = ""
    self.dataCadastro = ""
    self.valor = ""

  def criaFuncionario(self, funcionario):
    self.cursor.execute("INSERT INTO funcionarios (nomeCompleto, cpf, dataCadastro) VALUES (?, ?, ?);", funcionario)
    self.conn.commit()
    return "\nO Registro do funcionario foi criado com sucesso"

  def verificaCpf(self, cpf):
    self.cursor.execute("SELECT COUNT(*) FROM funcionarios WHERE cpf = ?", (cpf,))
    resultado = self.cursor.fetchone()
    quantidade = resultado[0]
    if quantidade > 0:
        return True  
    else:
        return False

  def puxaNome(self,cpf):
    self.cursor.execute("SELECT nomeCompleto from funcionarios WHERE CPF = ?", (cpf, ))
    resultado = self.cursor.fetchone()
    return resultado[0]

  def puxaId(self,cpf):
    self.cursor.execute("SELECT idFuncionario from funcionarios WHERE CPF = ?", (cpf, ))
    resultado = self.cursor.fetchone()
    return resultado[0]

  def exibirFuncionarioUnico(self, cpf):
    self.cursor.execute("SELECT * FROM funcionarios WHERE CPF = ?", (cpf, ))
    resultado = self.cursor.fetchall()
    headers = ["idFuncionario", "nomeCompleto", "CPF", "dataCadastro"]
    print(tabulate(resultado, headers=headers, tablefmt="fancy_grid"))
    input("Pressione \033[31m<ENTER>\033[0m para voltar.\n")

  def mostraFuncionarios(self):
    self.cursor.execute("SELECT * FROM funcionarios")
    resultado = self.cursor.fetchall()
    headers = ["idFuncionario", "nomeCompleto", "CPF", "dataCadastro"]
    print(tabulate(resultado, headers=headers, tablefmt="fancy_grid"))

  def alterarNome(self, infos):
    aux = self.verificaCpf(infos[1])
    if aux == True:
      self.cursor.execute("UPDATE funcionarios SET nomeCompleto = ? WHERE CPF = ?;", infos)
      self.conn.commit()
      return "Nome atualizado com sucesso"
    else:
      return "Não foi possivel atualizar o nome"

  
    
    
    