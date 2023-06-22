#NOME: Gabriel de Souza Reis BP3034089
#      Ryan Soprani BP3033309
#
#      Projeto LP2

import schema
import funcionarios
import chave
import produtos
import vendas
from carregaTela import barProgress
from limpaConsole import limpaConsole
from datetime import date
from time import sleep
import matplotlib.pyplot as matplot

senhaAdm = 1234
metaDia = 5000.00
#MENU 1 (tela login/registro)
def menu1():
  limpaConsole()
  print("*" * 30)
  print("***" + "Inicio".center(24) + "***" )
  print("*" * 30)
  print("""
\033[31m[1]\033[0m Fazer login
\033[31m[2]\033[0m Registrar-se
\033[31m[3]\033[0m Sair

\033[33m[4]\033[0m ADM
  """)
  return int(input("Escolha uma opção: "))

#MENU 2 (tela registro)
def menu2():
  limpaConsole()
  print("*" * 30)
  print("**" + " Registrando Funcionario ".center(4) + "**" )
  print("*" * 30)

def menuLogin(): # MENU 3 (tela Login)
  limpaConsole()
  print("*" * 30)
  print("***" + "login".center(24) + "***" )
  print("*" * 30)
  print("\033[31mSeja bem-vindo a tela de login, insira suas informações corretamente\n\033[0m")

def menuPrincipal(cpf, funcionario):
  print("*" * 30)
  print("***" + "Caixa".center(24) + "***" )
  print("***" + f"{funcionario.puxaNome(cpf)} ".center(24) + "***" )
  print("*" * 30)
  print("""
\033[31m[1]\033[0m Abrir caixa
\033[31m[2]\033[0m Adicionar Produtos
\033[31m[3]\033[0m Ver Produtos
\033[31m[4]\033[0m Perfil
\033[31m[5]\033[0m Voltar pra menu inicial

\033[31m[6]\033[0m Grafico
  """)
  return int(input("Escolha uma opção: "))

def menuAdm():
  print("***\tFUNÇÕES ADMINISTRATIVAS\t***\n\n")
  print("""
  \033[33m[1]\033[0m Ver Tabelas
    
  \033[33m[2]\033[0m Alterar Tabela de Funcionarios
  \033[33m[3]\033[0m Alterar Tabela de Produtos

  \033[33m[4]\033[0m Excluir Tabela de Produtos
  \033[33m[5]\033[0m Demitir Funcionario

  \033[33m[6]\033[0m Voltar
    
  """)
  return int(input("Escolha uma opção: "))

if __name__ == '__main__':
  banco = input("Informe o nome do banco: ")
  conn = schema.gerarBanco(banco)
  objProdutos = produtos.Produtos(conn)
  aux1 = objProdutos.gerarProdutosIniciais()
  print(aux1)
  sleep(4)
  
  m1 = menu1()
  limpaConsole()
  while m1 != 3:
    limpaConsole()    
    if m1 > 4 or m1 < 1:
      barProgress()
      print(f"\033[31mOpção {m1} é invalida, tente novamente!\033[0m")
      sleep(2)
      m1 = menu1()
      
    if m1 == 1:
      limpaConsole()
      funcionario = funcionarios.Funcionarios(conn)
      objChave = chave.ChaveAcesso(conn)
      menuLogin()
            
      cpf = input("Entre com seu CPF: ")
      if funcionario.verificaCpf(cpf) == True:
        funcional = input("Entre com sua Funcional: ")
        if objChave.verificaChave((funcional, cpf)) == True:
          
          barProgress()
          print("\033[31mLogin realizado com sucesso!\033[0m")
          sleep(3)
          limpaConsole()
          m2 = int(menuPrincipal(cpf,funcionario))

          while m2 != 5:
            
            if m2 == 1:
              limpaConsole()
              objVenda = vendas.Vendas(conn)
              opcaoCaixa = int(input("Digite \033[31m1\033[0m para passar um produto ou \033[31m2\033[0m para fechar o caixa: "))
              soma = 0
              while opcaoCaixa != 2:
                
                if opcaoCaixa == 1:
                  limpaConsole()
                  objProdutos.mostrarProdutos()
                  idProduto = input("Entre com o ID do produto: ")
                  if objProdutos.verificaId(idProduto) == True:
                    cpfCliente = input("Entre com o CPF do cliente: ")
                    if len(str(cpfCliente)) == 11:
                      valorDia = objProdutos.puxaValor(idProduto)
                      soma += float(valorDia)
                      barProgress()
                      objVenda.registrarVenda(idProduto, cpfCliente)
                      sleep(2)
                      limpaConsole()
                      opcaoCaixa = int(input("Digite \033[31m1\033[0m para passar um produto ou \033[31m2\033[0m para fechar o caixa: "))
                    else:
                       print("Este CPF não é valido")
                    sleep(2)
                    continue
                  else:
                    print("Este id não é valido")
                    sleep(2)
                    continue
              if opcaoCaixa == 2:
                objVenda.fecharCaixa(soma)
                soma = 0
                input("Pressione \033[31m<ENTER>\033[0m para voltar.\n")
                limpaConsole()
                print("Saindo...")
                limpaConsole()
                sleep(2)
                m2 = int(menuPrincipal(cpf,funcionario))
                
              else:
                print("Opção invalida, Retornando...")
                sleep(2)
                limpaConsole()
                m2 = int(menuPrincipal(cpf,funcionario))

            elif m2 == 2:
              limpaConsole()
                            
              opcao2 = int(input("\n\033[31m[1]\033[0m Adicionar novo produto\n\033[31m[2]\033[0m Voltar\nEscolha uma opção: "))
              
              if opcao2 == 1:
                objProdutos.mostrarProdutos()
                funcionarioId = funcionario.puxaId(cpf)
                nomeProduto = input("Entre com o nome do produto: ")
                dataInsercao = str(date.today())
                valorProduto = float(input("Digite o valor do produto: "))
                barProgress()
                objProdutos.adicionarProduto((funcionarioId, nomeProduto, dataInsercao, valorProduto))
                sleep(5)
                limpaConsole()
                m2 = menuPrincipal(cpf,funcionario)
                
              else:
                barProgress()
                print("Voltando...")
                sleep(2)
                limpaConsole()
                m2 = menuPrincipal(cpf,funcionario)
                                             
            elif m2 == 3:
              objProdutos.mostrarProdutos()
              input("Pressione \033[31m<ENTER>\033[0m para voltar.")
              print("Voltando...")
              sleep(2)
              limpaConsole()
              m2 = int(menuPrincipal(cpf,funcionario))
              
            elif m2 == 4:
              limpaConsole()
              funcionario.exibirFuncionarioUnico(cpf)
              print("voltando...")
              sleep(3)
              limpaConsole()
              m2 = int(menuPrincipal(cpf,funcionario))
              
            elif m2 == 6:
              objVenda = vendas.Vendas(conn)
              barProgress()
              limpaConsole()
              vendasDia = objVenda.vendaDia()
              
              faltou = metaDia - vendasDia
              atingido = vendasDia
              fig, ax = matplot.subplots()
              
              ax.bar(['Meta Diaria', 'Alcançado', 'faltou'], [metaDia, vendasDia, faltou], color=['red', 'green', 'blue'])
              
              ax.set_xlabel('Dia', fontsize=12)
              ax.set_ylabel('Valor', fontsize=12)
              ax.set_title('Comparação em relação à metaDiária', fontsize=14)
              
              ax.tick_params(axis='x', labelsize=10)
              ax.tick_params(axis='y', labelsize=10)
              
              ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
              matplot.tight_layout()
              matplot.show()
              input("\nPressione \033[31m<ENTER>\033[0m para voltar")
              sleep(1)
              limpaConsole()
              m2 = menuPrincipal(cpf,funcionario)
              
            else:
              barProgress()
              print((f"\033[31mA opção {m2} é invalida!\033[0m"))
              sleep(1)
              limpaConsole()
              m2 = menuPrincipal(cpf,funcionario)
              
          limpaConsole()
          m1 = menu1()
 
        else:
          barProgress()
          print("\n\033[31mCPF ou Funcional invalido. Voltando ao menu inicial.\033[0m")
          sleep(3)
          m1 = menu1()
      else:
        barProgress()
        print("\n\033[31mCPF ou Funcional invalido. Voltando ao menu inicial.\033[0m")
        sleep(3)
        m1 = menu1()
        
    elif m1 == 2:
      senha = int(input("Para Realizar o cadastro, digite a senha do administrador: "))
      
      if senha == senhaAdm:
        funcionario = funcionarios.Funcionarios(conn)
        limpaConsole()
        menu2()
             
        cpf = int(input("Digite seu CPF: "))
        if len(str(cpf)) == 11 and funcionario.verificaCpf(cpf) == False:
          nomeCompleto = input("Digite seu NOME COMPLETO: ")
          dataRegistro = str(date.today())
          infos = (nomeCompleto,cpf, dataRegistro)
          aux = funcionario.criaFuncionario(infos)
          barProgress()
          print(aux)
          objChave = chave.ChaveAcesso(conn)
          print(f"{objChave.criarChave(nomeCompleto)}")
          
          input("\nPressione \033[31m<ENTER>\033[0m para voltar.")
          limpaConsole()
          m1 = menu1()

        else:
          barProgress()
          print("O Cpf é invalido")
          sleep(2)
          continue
      else:
        barProgress()
        print("\033[31mSenha Incorreta!\033[0m")
        sleep(3)
        m1 = menu1()
        
    elif m1 == 4:
      
      senha = int(input("Digite a senha do administrador: "))
      
      if senha == senhaAdm:
        barProgress()
        limpaConsole()
        funcionario = funcionarios.Funcionarios(conn)
        objProdutos = produtos.Produtos(conn)
        objVenda = vendas.Vendas(conn)
        objChave = chave.ChaveAcesso(conn)
  
        mAdm = menuAdm()
        while mAdm != 6:
          if mAdm > 6 or mAdm < 1:
            barProgress()
            print(f"Opção {mAdm} inválida.")
            sleep(2)
            limpaConsole()
            mAdm = menuAdm()
  
          if mAdm == 1:
            
            limpaConsole()
            barProgress() 
            print("*"* 80)
            objProdutos.mostrarProdutos()
            print("*"* 80)
            funcionario.mostraFuncionarios()
            print("*"* 80)
            objVenda.mostraVendas()
            print("*"* 80)
            input("\nPressione \033[31m<ENTER>\033[0m para voltar.")
            limpaConsole()
            mAdm = menuAdm()
            
          elif mAdm == 2:
            barProgress()
            limpaConsole()
            funcionario.mostraFuncionarios()
            cpf = input("Insira o CPF do funcionario que deseja alterar: ")
            if funcionario.verificaCpf(cpf) == True:
              nvNome = input("Digite o novo nome desejado: ")
              infos = (nvNome,cpf)
              x = funcionario.alterarNome(infos)
              print(x)
              sleep(2)
              limpaConsole()
              mAdm = menuAdm()

            else:
              barProgress()
              print("O Cpf é invalido")
              sleep(2)
              continue

          elif mAdm == 3:
            barProgress()
            limpaConsole()
            objProdutos.mostrarProdutos()
            id = input("Insira o ID do produto: ")
            if objProdutos.verificaId(id) == True:
              nvNome = input("Digite o novo nome do Produto: ")
              nvValor = input("Digite o novo valor: ")
              infos = (nvNome,nvValor, id)
              x = objProdutos.alteraProduto(infos)
              print(x)
              sleep(2)
              limpaConsole()
              mAdm = menuAdm()
              
            else:
              barProgress()
              print("O ID é invalido")
              sleep(2)
              continue
              limpaConsole()
              mAdm = menuAdm() 

          elif mAdm == 4:
            barProgress()
            limpaConsole()
            objProdutos.mostrarProdutos()
            id = input("Insira o ID do produto: ")
            if objProdutos.verificaId(id) == True:
              x = objProdutos.excluirProduto(id)
              print(x)
              sleep(2)
              limpaConsole()
              mAdm = menuAdm()
                            
            else:
              barProgress()
              print("O ID é invalido")
              sleep(2)
              continue
              limpaConsole()
              mAdm = menuAdm()
              
          elif mAdm == 5:
            barProgress()
            limpaConsole()
            funcionario.mostraFuncionarios()
            cpfDemissao = input("Insira o CPF do funcionario que deseja Demitir: ")
            if funcionario.verificaCpf(cpfDemissao) == True:
              x = objChave.excluirChave(cpfDemissao)
              print(x)
              sleep(2)
              limpaConsole()
              mAdm = menuAdm()
              
            else:
              barProgress()
              print("O CPF é invalido ou o Funcionario já foi Demitido")
              sleep(2)
              continue
              limpaConsole()
              mAdm = menuAdm()
              
          else:
            barProgress()
            print(f"\033[31mA opção {mAdm} é invalida!\033[0m")
            sleep(2)
            limpaConsole()
            mAdm = menuAdm()
            
        barProgress()
        print("Voltando...")
        limpaConsole()
        m1 = menu1()
      else:
        barProgress()
        print("\033[31mSenha Incorreta!\033[0m")
        sleep(3)
        limpaConsole()
        m1 = menu1()

    else:
      barProgress()
      print(f"\033[31mA opção {m1} é invalida!\033[0m")
      sleep(2)
      limpaConsole()
      m1 = menu1()
      
  print("Finalizando Programa...")