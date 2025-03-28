from paginas.Pagina import Pagina
from GerenciadorUsuarios import GerenciadorUsuarios

class ListagemUsuario(Pagina):
  """
  Classe responsável por listar todos os usuários cadastrados.
  
  Exibe uma lista de todos os usuários no sistema.
  
  Esta classe herda de `Pagina` e implementa os métodos abstratos `exibir_interface`, 
  `processar_dados` e `processar_opcao_selecionada` para a funcionalidade específica 
  de listagem de usuários.
  """

  def exibir_interface(self):
    """
    Exibe o título da interface de listagem de usuários.
    """
    print('\n----- Listagem de usuários -----\n')

  def processar_dados(self):
    """
    Processa a listagem dos usuários cadastrados.
    Chama o gerenciador de usuários para listar todos os usuários.
    """
    gerenciador = GerenciadorUsuarios()
    gerenciador.listar_usuarios()

  
  def processar_opcao_selecionada(self) -> "Pagina":
    """
    Processa a escolha de navegação após a listagem de usuários.
    Permite ao usuário retornar ao menu principal.
    """
    while True:
      print('\n[0] Retornar ao menu')
      
      try:
        opcao = int(input('\nDigite a opção desejada: '))
        
        match opcao:
          case 0:
            from paginas.Menu import Menu
            return Menu()
          case _:
            print('\nValor Inválido.')
      except ValueError:
        print('\nValor Inválido.')
