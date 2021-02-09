# -*- coding: utf-8 -*-
"""Relatorio_Vendas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/157aEwgxxftEZgghvd911qfRNUjtoP_rX

Desafio:
Você faz parte da equipe de Analytics de uma grande marca de vestuário com mais de 25 lojas espalhadas em Shoppings de todo o Brasil.

Toda semana você precisa enviar para a diretoria um ranking atualizado com as 25 lojas contendo 3 informações:

Faturamento de cada Loja
Quantidade de Produtos Vendidos de cada Loja
Ticket Médio dos Produto de cada Loja
Além disso, cada loja tem 1 gerente que precisa receber o resumo das informações da loja dele. Por isso, cada gerente deve receber no e-mail:

Faturamento da sua loja
Quantidade de Produtos Vendidos da sua loja
Ticket Médio dos Produto da sua Loja
Esse relatório é sempre enviado como um resumo de todos os dados disponíveis no ano.

Solução do Desafio:
Para resolver o desafio vamos seguir a seguinte lógica:

Passo 1 - Importar a base de Dados

Passo 2 - Visualizar a Base de Dados para ver se precisamos fazer algum tratamento

Passo 3 - Calcular os indicadores de todas as lojas:
Faturamento por Loja
Quantidade de Produtos Vendidos por Loja
Ticket Médio dos Produto por Loja

Passo 4 - Calcular os indicadores de cada loja


**Passo 1 - Importando a Base de Dados + Passo 2 - Visualizando os Dados**
"""

import pandas as pd 

tabela_vendas = pd.read_excel("python/Vendas.xlsx")
display(tabela_vendas)

"""**Passo 3.1 - Calculando o Faturamento por Loja**"""

faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
faturamento = faturamento.sort_values(by='Valor Final', ascending=False)
display(faturamento)

"""**Passo 3.2 - Calculando a Quantidade Vendida por Loja**"""

quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
quantidade = quantidade.sort_values(by='ID Loja', ascending=False)
display(quantidade)

"""**Passo 3.3 - Calculando o Ticket Médio dos Produtos por Loja**"""

ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Medio'})
ticket_medio = ticket_medio.sort_values(by='Ticket Medio', ascending=False)
display(ticket_medio)



tabela_completa = faturamento.join(quantidade).join(ticket_medio)
display(tabela_completa)


lojas = tabela_vendas['ID Loja'].unique()

for loja in lojas:
  tabela_loja = tabela_vendas.loc[tabela_vendas['ID Loja'] == loja, ['ID Loja', 'Quantidade', 'Valor Final']]
  resumo_loja = tabela_loja.groupby('ID Loja').sum()
  resumo_loja['Ticket Médio'] = resumo_loja['Valor Final'] / resumo_loja['Quantidade']
  display(resumo_loja)
  