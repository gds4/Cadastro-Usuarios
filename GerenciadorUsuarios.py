from modelo.Usuario import Usuario

class GerenciadorUsuarios:
  """
  Classe responsável pela gestão de usuários no sistema.
  Permite adicionar, listar, buscar, atualizar e remover usuários.
  """
  
  usuarios = []

  def adicionar_usuario(self, nome: str, email: str, idade: int):
    """
    Adiciona um novo usuário à lista de usuários.
    
    Parâmetros:
    nome (str): Nome do usuário.
    email (str): Email do usuário.
    idade (int): Idade do usuário.
    
    Retorna:
    bool: True se o usuário foi adicionado com sucesso, False em caso de erro.
    """
    try:
      usuario = Usuario(nome, email, idade)
      self.usuarios.append(usuario)
    except ValueError as erro:
      print(f'Erro ao cadastrar usuário: {erro}')
      return False
    return True
      
  def listar_usuarios(self):
    """
    Exibe a lista de todos os usuários cadastrados no sistema.
    Se não houver usuários cadastrados, exibe uma mensagem indicando isso.
    """
    
    if len(self.usuarios) == 0:
      print('Nenhum usuário cadastrado.')
      return
      
    for usuario in self.usuarios:
      print(usuario)

  def buscar_usuario(self, id_usuario: int):
    """
    Busca um usuário pelo ID.
    
    Parâmetros:
    id_usuario (int): ID do usuário a ser buscado.
    
    Retorna:
    Usuario: O usuário encontrado ou None se não houver usuário com o ID informado.
    """
    for usuario in self.usuarios:
      if usuario.id == id_usuario:
        return usuario
    return None

  def atualizar_usuario(self, id_usuario: int, novo_nome: str, novo_email: str, nova_idade: int):
    """
    Atualiza os dados de um usuário existente.
    
    Parâmetros:
    id_usuario (int): ID do usuário a ser atualizado.
    novo_nome (str): Novo nome do usuário.
    novo_email (str): Novo email do usuário.
    nova_idade (int): Nova idade do usuário.
    
    Retorna:
    bool: True se o usuário foi atualizado com sucesso, False em caso de erro.
    """
    usuario = self.buscar_usuario(id_usuario)
    if usuario:
      try:
        usuario.nome = novo_nome
        usuario.email = novo_email
        usuario.idade = nova_idade
      except ValueError as erro:
        print(f'Erro ao atualizar usuário: {erro}')
        return False
      return True

  def remover_usuario(self, id_usuario: int):
    """
    Remove um usuário da lista de usuários.
    
    Parâmetros:
    id_usuario (int): ID do usuário a ser removido.
    
    Retorna:
    bool: True se o usuário foi removido com sucesso, False se o usuário não for encontrado.
    """
    usuario = self.buscar_usuario(id_usuario)
    if usuario:
      self.usuarios.remove(usuario)
      return True
    return False
  
  def buscar_usuarios_por_nome(self, nome_trecho: str):
    """
    Busca usuários que possuam um nome que contenha o trecho fornecido.
    
    Parâmetros:
    nome_trecho (str): Nome ou trecho de nome a ser buscado.
    
    Retorna:
    list: Lista de usuários cujos nomes contêm o trecho fornecido (insensível a maiúsculas/minúsculas).
    """
    usuarios_encontrados = []
    for usuario in self.usuarios:
      if nome_trecho.lower() in usuario.nome.lower():
        usuarios_encontrados.append(usuario)
    
    return usuarios_encontrados