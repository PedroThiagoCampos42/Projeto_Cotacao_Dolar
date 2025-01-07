# Cotacao_Dolar
Este projeto envolve montar uma extração de dados do Banco Central do Brasil (BACEN), sobre as variações do Dólar americano para o Real brasileiro utilizando Python e a biblioteca pandas. Depois montar uma visualização de dados utilizando o Metabase, um aplicativo de código aberto similar ao Power BI.

Ferramentas e softwares utilizados:
- Visual Studio Code (Gratuito).
- Python (Linguagem de código aberto).
- Metabase (Código aberto).
- Apache Hop *Extra* (Código aberto).

# 1° Extração de dados da API do BACEN
Seguindo o arquivo chamado "Extracao de dados para uma tabela". O arquivo python realiza a extração dos dados da API, e em seguida insere estes dados em uma tabela local do PostgreSQL.

![Imagens](imagens/Visualizacao_da_tabela-%20Table%20view.png)

# 2° Visualização de dados pelo Metabase
Com os dados das cotações já colocados na tabela do banco, através do Metabase é criada a visualização destes dados de forma a montar uma pergunta (question), e ajustar a visualização com base na média de cotações agrupadas por mês.

![Imagens](imagens/Visualizacao_do_grafico.png)
![Imagens](imagens/Visualizacao_do_editor.png)

This project revolves in making an data extraction from the brazilian central bank (BACEN), about the variations of the US Dolar to the brazilian Real via Python and the pandas library. After that making a data visualizations using Metabase, an open-source application similar to Power BI.

Tools and softwares used:
- Visual Studio Code (Free).
- Python (Open source language).
- Metabase (Open source).
- Apache Hop *Extra* (Open source).