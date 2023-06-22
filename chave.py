import sqlite3
import random
import string
import funcionarios

#Gerador de senha automatico
def gerarFuncional(comprimento = 6):
  digitos = string.digits
  senha = ''.join(random.choice(digitos) for i in range(comprimento))
  funcional = "SP" + senha
  return funcional

#Criando classe Chave (Funcional)
class ChaveAcesso:
  
  def __init__(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()
    self.idChave = ""
    self.idFuncionario = ""

  def criarChave(self, nome):
    funcionalSenha = gerarFuncional()
    self.cursor.execute("SELECT idFuncionario FROM funcionarios WHERE nomeCompleto = ?", (nome, ))
    resultado = self.cursor.fetchone()
    if resultado is not None:
      idFuncionario = resultado[0]
      aux = (idFuncionario, funcionalSenha)
      self.cursor.execute("INSERT INTO chaveAcesso (idFuncionario, chave) VALUES (?, ?);", aux)
      self.conn.commit()
      return f"Conta: \033[31m{nome}\033[0m\nSUA FUNCIONAL É: \033[31m{funcionalSenha}\033[0m"
    else:
      print("Funcionário não encontrado.")
  
  def verificaChave(self, chaveCpf):
    self.cursor.execute("SELECT COUNT(c.chave) FROM chaveAcesso c INNER JOIN funcionarios f ON c.idFuncionario = f.idFuncionario WHERE c.chave = ? AND f.CPF = ?", chaveCpf)
    resultado = self.cursor.fetchone()
    quantidade = resultado[0]
    if quantidade > 0:
      return True
    else:
      return False 

  def excluirChave(self, cpf1):
    
    self.cursor.execute("DELETE FROM chaveAcesso WHERE idFuncionario IN (SELECT idFuncionario FROM funcionarios WHERE cpf = ?);", (cpf1,))
    self.conn.commit()
    return "Chave de acesso excluída com sucesso"



    
    