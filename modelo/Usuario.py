import re

class Usuario:
  """
  Classe que representa um usuário do sistema.

  A classe `Usuario` armazena informações sobre um usuário, como ID, nome, 
  email e idade. O ID é gerado automaticamente a partir de um contador global.
  Também fornece validações para os campos `email` e `idade`.

  Atributos:
  - id (int): Identificador único do usuário.
  - nome (str): Nome do usuário.
  - email (str): Email do usuário (com validação).
  - idade (int): Idade do usuário (com validação).

  """
  
  _contador_id = 1

  def __init__(self, nome, email, idade):
    """
    Inicializa um novo usuário com os dados fornecidos.

    Parâmetros:
    - nome (str): Nome do usuário.
    - email (str): Email do usuário.
    - idade (int): Idade do usuário.
    """
    self.nome = nome
    self.email = email
    self.idade = idade
    self.id = Usuario._contador_id
    Usuario._contador_id += 1
    
  @property 
  def nome(self):
    """
    Retorna o nome do usuário.

    Retorno:
    - str: O nome do usuário.
    """
    return self._nome
  
  @nome.setter
  def nome(self, nome):
    """
    Define o nome do usuário.

    Parâmetro:
    - nome (str): O nome do usuário.
    
    Exceção:
    - ValueError: Se o nome possuir menos de 3 caracteres.
    """
    if len(nome) < 3:
      raise ValueError('O nome deve possuir no mínimo 3 caracteres.')
    self._nome = nome
    
  @property 
  def email(self):
    """
    Retorna o email do usuário.

    Retorno:
    - str: O email do usuário.
    """
    return self._email
  
  @email.setter
  def email(self, email):
    """
    Define o email do usuário, com validação de formato.

    Parâmetro:
    - email (str): O email do usuário.

    Exceção:
    - ValueError: Se o email não for válido.
    """
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
      raise ValueError('Email inválido.')
    self._email = email
    
  @property 
  def idade(self):
    """
    Retorna a idade do usuário.

    Retorno:
    - int: A idade do usuário.
    """
    return self._idade
  
  @idade.setter
  def idade(self, idade):
    """
    Define a idade do usuário, com validação de faixa etária.

    Parâmetro:
    - idade (int): A idade do usuário.

    Exceção:
    - ValueError: Se a idade não estiver entre 1 e 125 anos.
    """
    if not (1 <= idade <= 125):
      raise ValueError('A idade deve estar entre 1 e 125 anos.')
    self._idade = idade
    
  def __str__(self):
    """
    Retorna uma representação em string do usuário.

    Retorno:
    - str: Representação formatada do usuário.
    """
    return f'ID: {self.id}, Nome: {self.nome}, Email: {self.email}, Idade: {self.idade}'
