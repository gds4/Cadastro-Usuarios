from abc import ABC, abstractmethod

class Pagina(ABC):
  """
  Classe abstrata que define a estrutura básica de uma página no sistema.
  """
  
  @abstractmethod
  def exibir_interface(self):
    """
    Método abstrato para exibir a interface da página.
    """
    pass
  
  @abstractmethod
  def processar_dados(self):
    """
    Método abstrato para processar dados da página.
    """
    pass
  
  @abstractmethod
  def processar_opcao_selecionada(self) -> "Pagina":
    """
    Método abstrato que processa a opção selecionada pelo usuário.
    Retorna uma nova instância de uma página ou None.
    """
    pass