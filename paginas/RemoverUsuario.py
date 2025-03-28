from paginas.Pagina import Pagina
from GerenciadorUsuarios import  GerenciadorUsuarios

class RemoverUsuario(Pagina):
  """
  Classe responsável por remover um usuário do sistema.
  
  Permite ao usuário confirmar a remoção de um usuário existente, 
  após fornecer o ID e confirmar a operação.
  
  Esta classe herda de `Pagina` e implementa os métodos abstratos `exibir_interface`, 
  `processar_dados` e `processar_opcao_selecionada` para a funcionalidade específica 
  de remoção de usuário.
  """
  
  def exibir_interface(self):
    """
    Exibe o título da página de remoção de usuário.
    """
    print('\n----- Remover Usuário -----\n')
    
  def processar_dados(self):
    """
    Processa a remoção de um usuário.
    Solicita o ID do usuário a ser removido e confirma a ação antes de excluí-lo.
    Se o ID for inválido ou o usuário não for encontrado, exibe uma mensagem de erro.
    """
    print('Digite [-1] para cancelar a operação.')
    
    sair = False
    while not sair:
      id_usuario = input('\nInforme o ID do usuário que deseja remover: ')
      if id_usuario == '-1':
        return
      
      try:
        id_usuario = int(id_usuario)
        sair = True
      except ValueError:
        print("\nID inválido. Deve ser um número inteiro.")
      
    gerenciador = GerenciadorUsuarios()
    usuario = gerenciador.buscar_usuario(id_usuario)
    
    if usuario is None:
      print('\nNão há nenhum usuario cadastrado com este id.')
      return
    
    sair = False
    while not sair:
      confirmacao_remocao = input(f'\nDeseja realmente remover o usuário [{usuario}]? S/N: ')
    
      if confirmacao_remocao.upper() == 'N':
        sair = True
        return
      elif confirmacao_remocao.upper() == 'S':
        gerenciador.remover_usuario(id_usuario)
        print('\nUsuário removido com sucesso!')
        sair = True
      else:
        print('\nOpção Inválida.')
      
  def processar_opcao_selecionada(self) -> "Pagina":    
    """
    Processa a escolha de navegação após a remoção de um usuário.
    Permite ao usuário retornar ao menu ou tentar remover outro usuário.
    """
    while True:
      print('\n[0] Retornar ao menu')
      print('[1] Remover novamente')
      
      try:
        opcao = int(input('\nDigite a opção desejada: '))
        
        match opcao:
          case 0:
            from paginas.Menu import Menu
            return Menu()
          case 1:
            return RemoverUsuario()
          case _:
            print('\nValor Inválido')
      except ValueError:
        print('\nValor Inválido')
