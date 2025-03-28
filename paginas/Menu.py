from paginas.Pagina import Pagina
from paginas.CadastroUsuario import CadastroUsuario
from paginas.ListagemUsuarios import ListagemUsuario
from paginas.BuscarUsuario import BuscarUsuario
from paginas.RemoverUsuario import RemoverUsuario
from paginas.AtualizarUsuario import AtualizarUsuario

class Menu(Pagina):
  """
  Classe que representa o menu principal do sistema.
  
  Esta classe herda de `Pagina` e implementa os métodos abstratos `exibir_interface`, 
  e `processar_opcao_selecionada` para a funcionalidade específica de exibição do menu.
  """

  def exibir_interface(self):
    """
    Exibe a título do menu principal.
    """    
    print('\n----- Sistema de Usuários -----\n')

    
  def processar_dados(self):
    """
    Método necessário para atender a interface, mas não possui implementação.
    """
    pass

  def processar_opcao_selecionada(self) -> "Pagina":
    """
    Processa a opção escolhida pelo usuário e retorna a página correspondente.
    Caso o usuário escolha sair, retorna None.
    """
    
    while True:
      print('[1] Cadastrar usuário')
      print('[2] Listar Todos os usuários')
      print('[3] Buscar um usuário')
      print('[4] Remover um usuário')
      print('[5] Atualizar um usuário')
      print('[0] Sair')
      
      try:
        pagina_selecionada = int(input('\nDigite a opção desejada: '))
        
        match pagina_selecionada:
          case 1:
            return CadastroUsuario()
          case 2:
            return ListagemUsuario()
          case 3:
            return BuscarUsuario()
          case 4:
            return RemoverUsuario()
          case 5:
            return AtualizarUsuario()
          case 0:
            return None
          case _:
            print('\nValor Inválido')
      except:
        print('\nValor Inválido')
  
