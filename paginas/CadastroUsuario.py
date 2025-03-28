from paginas.Pagina import Pagina
from GerenciadorUsuarios import GerenciadorUsuarios


class CadastroUsuario(Pagina):
  """
  Classe responsável pelo cadastro de usuários no sistema.
  
  Esta classe herda de `Pagina` e implementa os métodos abstratos `exibir_interface`, 
  `processar_dados` e `processar_opcao_selecionada` para a funcionalidade específica 
  de cadastro de usuário.
  """
  
  def exibir_interface(self):
    """
    Exibe o título da interface de cadastro de usuários.
    """
    print('\n----- Cadastro de Usuários -----')
    
  def processar_dados(self):
    """
    Captura os dados do usuário e os armazena no sistema.
    Permite cancelar a operação digitando [-1].
    """
    print('\nDigite [-1] para cancelar operação\n')
    
    nome = input('Digite o nome do usuário: ').strip()
    if nome == '-1': 
      return
    
    email = input('Digite o email do usuário: ').strip()
    if email == '-1':
      return
    
    sair = False
    while not sair:
      idade = input('Digite idade do usuário: ').strip()
      if idade == '-1':
        return
      try:
        idade = int(idade)
        sair = True
      except ValueError:
        print('\nIdade inválida! Deve ser um número inteiro.') 
  
    gerenciador_usuarios = GerenciadorUsuarios()
    cadastrado_sucesso = gerenciador_usuarios.adicionar_usuario(nome, email, idade)
    
    if cadastrado_sucesso:
      print('\nUsuário cadastrado com sucesso!')
      
  def processar_opcao_selecionada(self) -> "Pagina":
    """
    Processa a opção selecionada pelo usuário após o cadastro.
    Retorna ao menu ou permite um novo cadastro.
    """
    while True:
      print('\n[0] Retornar ao menu')
      print('[1] Cadastrar novamente')
      
      try:
        opcao = int(input('\nDigite a opção desejada: '))
        
        match opcao:
          case 0:
            from paginas.Menu import Menu
            return Menu()
          case 1:
            return CadastroUsuario()
          case _:
            print('\nValor Inválido')
      except ValueError:
        print('\nValor Inválido')
