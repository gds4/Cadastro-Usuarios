from paginas.Pagina import Pagina
from GerenciadorUsuarios import GerenciadorUsuarios

class BuscarUsuario(Pagina):
  """
  Classe responsável por buscar um usuário pelo nome.
  Permite ao usuário pesquisar por um usuário específico 
  e exibe os dados encontrados ou uma mensagem de erro se nenhum usuário for encontrado.
  
  Esta classe herda de `Pagina` e implementa os métodos abstratos `exibir_interface`, 
  `processar_dados` e `processar_opcao_selecionada` para a funcionalidade específica 
  de busca de usuário.
  """

  def exibir_interface(self):
    """
    Exibe o título da interface de busca de usuário.
    """
    print('\n----- Buscar Usuário -----\n')

  def processar_dados(self):
    """
    Processa a busca de um usuário pelo nome.
    Solicita ao usuário o nome ou trecho do nome e exibe as informações dos usuários encontrados,
    ou uma mensagem de erro caso nenhum usuário seja encontrado.
    """
    gerenciador = GerenciadorUsuarios()
    
    nome_trecho = input('Digite o nome ou trecho do nome do usuário: ')
    usuarios_encontrados = gerenciador.buscar_usuarios_por_nome(nome_trecho)
    
    if not usuarios_encontrados:
      print('\nNenhum usuário encontrado.')
    else:
      print('\nUsuários encontrados:')
      for usuario in usuarios_encontrados:
        print(usuario)

  def processar_opcao_selecionada(self) -> "Pagina":
    """
    Processa a escolha de navegação após a busca de usuário.
    Permite ao usuário retornar ao menu ou buscar outro usuário.
    """
    sair = False
    while not sair:
      print('\n[0] Retornar ao menu')
      print('[1] Buscar Novamente')
      
      try:
        opcao = int(input('\nDigite a opção desejada: '))
        
        match opcao:
          case 0:
            sair = True
            from paginas.Menu import Menu
            return Menu()
          case 1:
            sair = True
            return BuscarUsuario()
          case _:
            print('\nValor Inválido')
      except ValueError:
        print('\nValor Inválido')
