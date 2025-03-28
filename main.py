from paginas.Menu import Menu

# Inicia a aplicação com o Menu
pagina_atual = Menu()
sair = False

while not sair:
  """
  Exibe a interface da página atual, processa os dados e a opção selecionada
  pelo usuário. O fluxo de navegação entre as páginas é gerido aqui.
  """
  
  # Exibe a interface da página atual
  pagina_atual.exibir_interface()
  
  # Processa os dados necessários para a página atual
  pagina_atual.processar_dados()
  
  # Processa a opção selecionada e retorna a próxima página a ser exibida
  nova_pagina = pagina_atual.processar_opcao_selecionada()
  
  # Se uma nova página for selecionada, atualiza a página atual
  if nova_pagina is not None:
    pagina_atual = nova_pagina
  else:
    # Caso a navegação seja para a finalização, encerra o loop
    print('\nEncerrando Aplicação...')
    sair = True
