from paginas.Pagina import Pagina
from GerenciadorUsuarios import GerenciadorUsuarios

class AtualizarUsuario(Pagina):
  """
  Classe responsável por atualizar os dados de um usuário existente.
  
  Esta classe herda de `Pagina` e implementa os métodos abstratos `exibir_interface`, 
  `processar_dados` e `processar_opcao_selecionada` para a funcionalidade específica 
  de atualização de usuários.
  """
  
  def exibir_interface(self):
    """
    Exibe o título da interface de atualização de usuário.
    """
    print('\n----- Atualizar Usuário -----\n')
    
  def processar_dados(self):
    """
    Processa os dados de entrada para atualização do usuário.
    Solicita o ID do usuário, e em seguida permite a edição do nome, email e idade.
    Caso o valor informado seja vazio, mantém os dados atuais. 
    Se o valor for '-1', a operação é cancelada.
    """
    print('Digite [-1] para cancelar a operação.')
    print('Mantenha o campo vazio para manter os dados atuais.')
    
    id_usuario = input('\nInforme o ID do usuário que deseja atualizar: ')
    if id_usuario == '-1':
      return
    
    try:
      id_usuario = int(id_usuario)
    except ValueError:
      print('\nID inválido. Deve ser um número inteiro.')
      return
    
    gerenciador = GerenciadorUsuarios()
    usuario = gerenciador.buscar_usuario(id_usuario)
    
    if usuario is None:
      print('\nUsuário não encontrado.')
      return
    
    print(f'\nAtualizando o usuário: {usuario}')
    
    nome = input('\nDigite o novo nome do usuário: ').strip()
    if nome == '-1':
      return
    nome = usuario.nome if nome == "" else nome

    email = input('Digite o novo email do usuário: ').strip()
    if email == '-1':
      return
    email = usuario.email if email == "" else email

    sair = False
    while not sair:
      idade = input('Digite a nova idade para o usuário: ').strip()
      if idade == '-1':
        return
      try:
        idade = usuario.idade if idade == "" else int(idade)
        sair = True
      except ValueError:
        print('\nIdade inválida! Deve ser um número inteiro.') 
        
    atualizado_sucesso = gerenciador.atualizar_usuario(id_usuario=id_usuario, novo_nome=nome, novo_email=email, nova_idade=idade)
    
    if atualizado_sucesso: 
      print('\nUsuário atualizado com sucesso!')

  def processar_opcao_selecionada(self) -> "Pagina":
    """
    Processa a escolha de navegação após a atualização.
    Permite ao usuário retornar ao menu ou tentar atualizar o usuário novamente.
    """
    while True:
      print('\n[0] Retornar ao menu')
      print('[1] Atualizar usuário')
      
      try:
        opcao = int(input('\nDigite a opção desejada: '))
        
        match opcao:
          case 0:
            from paginas.Menu import Menu
            return Menu()
          case 1:
            return AtualizarUsuario()
          case _:
            print('\nValor Inválido')
      except ValueError:
        print('\nValor Inválido')
