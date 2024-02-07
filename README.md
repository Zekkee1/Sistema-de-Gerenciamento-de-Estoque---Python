<h1 align="center">
# Sistema-de-Gerenciamento-de-Estoque---Python
</h1>


# Descrição
Este sistema faz a importação de arquivos XML que são notas fiscais para ter o controle do estoque de acordo com a entrada e saídas apontadas pelo usuário.
Foi desenvolvido utilizando o criador de interface grafica QT Designer para criar o visual do sistema e python junto com Pyside6 para programar todas as funções do sistema
, além disso foi utilizado o Pandas para manipular os dados da tabela e SQLite para criar um banco de dados local.

Link do Download direto - https://drive.usercontent.google.com/download?id=1rw-VY7GMlEqXYMq7AHsAfpSrRq9Sw8n2

# Ferramentas
<ul>
  <li>Python</li>
  <li>QT Designer</li>
  <li>PySide6</li>
  <li>Pandas</li>
  <li>SQLite - Banco de dados</li>
</ul>


# Preview
## Página - Login

#### Nesta pagina o usuário poderá efetuar o login com base nos usuários cadastrados no banco de dados.
#### Por padrão o sistema ja possui 2 usuários cadastrados, um Administrador e um Usuário.
### Administrador: 
USERNAME: admin | SENHA: admin
### Usuário: 
USERNAME: usuario | SENHA: usuario

#### Os dados dos Usuários poderão ser alterados na pagina "Usuários" se o perfil logado for de Administrador

<img src="https://private-user-images.githubusercontent.com/99279134/303114112-00402bf5-8682-4d7c-abb1-37e2d49353f6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDczMzQ4MTMsIm5iZiI6MTcwNzMzNDUxMywicGF0aCI6Ii85OTI3OTEzNC8zMDMxMTQxMTItMDA0MDJiZjUtODY4Mi00ZDdjLWFiYjEtMzdlMmQ0OTM1M2Y2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA3VDE5MzUxM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTRkOWY0Y2M5ZjJkMzU1NWQ4NjE5OGUyYTY4NzAwYmMyODE2NjdiNWQ5MGJmNmY4M2QzODJkZGYyNWZmZGM2ZTYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.sONmcnFMWvpj1qzJvWK9YlbRhpxjpDpMqo56vduC46c">



  ## Página - Home

  #### Pagina inicial do aplicativo
  
<img src="https://private-user-images.githubusercontent.com/99279134/302808185-791b53d5-e411-4e42-a738-e5b552dc77e7.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjMzMzUsIm5iZiI6MTcwNzI2MzAzNSwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxODUtNzkxYjUzZDUtZTQxMS00ZTQyLWE3MzgtZTViNTUyZGM3N2U3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVlMTE3NzI4ZDhjNmNiNzgxODcxMzFjMWQ1NjVjM2RhZTZlZWE1ZTIyNzhlYzQxMjJhNzhkODEzZDBhYmNkODgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.YtPbMuTYlfZnM_KzZLBpJYz35TAUHCK3mdoi8F-Y6Rg" >


  ## Página - Importar

  #### Nesta pagina é possivel selecionar a pasta que contem todas as notas fiscais e o sistema cadastrará todas no banco de dados de uma só vez
<img src="https://private-user-images.githubusercontent.com/99279134/302808188-39bbf902-b6d5-4a9d-950e-87dd7a31530f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjMzMzUsIm5iZiI6MTcwNzI2MzAzNSwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxODgtMzliYmY5MDItYjZkNS00YTlkLTk1MGUtODdkZDdhMzE1MzBmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVmMGJmMGViOTMzNjg1NDE3ZDE2ZGU0ZTU2ZTAyY2U5NTRmNjczYmFmZjhkMWRjMmNlYjJlYzc5NGY0N2FlZmImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.v-lLoNhYwoMHWscZpgljeGHxwLxklBVTtut70_ZDzuk" >


  ## Página - Tables > Aba Base

  #### Nesta pagina poderão ser vizualizados os dados principais das notas fiscais, o usuário poderá dar baixa e estornar a nota fiscal para o estoque
<img src="https://private-user-images.githubusercontent.com/99279134/302808194-036c4f6c-ca0d-477c-94b8-a1301ed928d1.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjMzMzUsIm5iZiI6MTcwNzI2MzAzNSwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxOTQtMDM2YzRmNmMtY2EwZC00NzdjLTk0YjgtYTEzMDFlZDkyOGQxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTE1OTRkYWM1YmMzOTU1NTE4OTE2ZGI4MmY3NjgwNTk3ODE3ZGE4M2RiOWYwZThhMzBjZTIyNWUwYmU3MmJjZDAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.uaFCJ3PTZO5FP0v0utK3dWCpTERgFT3xh71DdzcTWl4" >


  ## Página - Tables > Aba Geral
  #### Nesta pagina o usuário poderá vizualisar os dados gerais de todas as notas cadastradas no banco de dados. 
  #### O usuário com o perfil "administrador" poderá selecionar as notas clicando no numero á esquerda da nota e excluí-las do banco de dados.
  
  <img src="https://private-user-images.githubusercontent.com/99279134/303114102-452c9253-019c-4a44-a8c0-e0ee3a449af2.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDczMzQ4MTMsIm5iZiI6MTcwNzMzNDUxMywicGF0aCI6Ii85OTI3OTEzNC8zMDMxMTQxMDItNDUyYzkyNTMtMDE5Yy00YTQ0LWE4YzAtZTBlZTNhNDQ5YWYyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA3VDE5MzUxM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWRlM2ViYzA3ZjMxOGM5MTE2NzRlN2YyZGJjOTIwZjg1MjFhY2IzZjhkNGJkYTliMmZhMDliOGE1MmFiYTdmZmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.7DlzB5_BHknftW-EuagtPZej8XRXpH2l4A883IaoQP0" >
  
  O usuário também poderá gerar um excel com o resumo de todas as Notas da tabela geral.
  <img src="https://private-user-images.githubusercontent.com/99279134/303114110-e8ffa22d-8026-4cd2-99e3-34c96324c2f2.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDczMzQ4MTMsIm5iZiI6MTcwNzMzNDUxMywicGF0aCI6Ii85OTI3OTEzNC8zMDMxMTQxMTAtZThmZmEyMmQtODAyNi00Y2QyLTk5ZTMtMzRjOTYzMjRjMmYyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA3VDE5MzUxM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTY3ZmMxNzEwNTcwNmY3MDU3MGZkYzczY2ZkZWQ4ZGQ1MzU2NzMwYWJhNzRkYmE3NjdkMzg5NzQwYmYyMzQwNDEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.2dbKiMmJvlr_fSWmMjrCe2Br_mCEDAYe2lAsITtlpS0" >


  ## Página - Usuários

  #### Nesta pagina somente usuários com perfil de "Administrador" poderão vizualiza-la.
  #### Ao selecionar um usuário da tabela o "Administrador" poderá: excluir usuário, cadastrar novo usuário, atualizar dados dos usuários.
<img src="https://private-user-images.githubusercontent.com/99279134/302808190-dee9e1d0-eed3-4c89-ac40-d62f0b749d49.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjMzMzUsIm5iZiI6MTcwNzI2MzAzNSwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxOTAtZGVlOWUxZDAtZWVkMy00Yzg5LWFjNDAtZDYyZjBiNzQ5ZDQ5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBhY2VkYzc1ZmM2MWFlODYwMjg1MjkzZDBmNjdlNDQyM2Y4YjQ1NjQwMzY4M2U0ZDAzNGMyZDRkNzk2OWZkZWImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.ml8OvJcVma3H6nMJNYGzXLdQ9-lZs24LpkjTMTNC2xI" >

## Página - Usuários > cadastro de usuarios

#### Nesta página o administrador poderá cadastrar um novo usuário no banco de dados.
<img src="https://private-user-images.githubusercontent.com/99279134/302808195-0c4f7272-0cd5-4e15-b4da-d6fd1e87399d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjMzMzUsIm5iZiI6MTcwNzI2MzAzNSwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxOTUtMGM0ZjcyNzItMGNkNS00ZTE1LWI0ZGEtZDZmZDFlODczOTlkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM1ZDQzNDU4MDdkZDdlY2U0YzQwODkyMzE5MmQxYmQxODEzY2JhZTgyZWRkOWRlYTNjMzQyMzljYzJmNzViNTcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.qnkB4xzDu0mCMSSGqOO49OKfX4ctmb0lJUjeJjpOAV4" >

## Página - Usuários > Atualizar Dados do Usuário

#### Nesta página o administrador poderá atualizar os dados do usuário selecionado.
<img src="https://private-user-images.githubusercontent.com/99279134/302808197-814ad65a-6e98-4b76-9218-3cb1fd6ce470.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjMzMzUsIm5iZiI6MTcwNzI2MzAzNSwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxOTctODE0YWQ2NWEtNmU5OC00Yjc2LTkyMTgtM2NiMWZkNmNlNDcwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTViYzczZTYzZWIyMmIwN2U3OGI3MjNhMmM1MDhkZmY5MGM4MzE4YTkxNzdiOTZhODY1YWVjNDBiOTJlNWNlMWQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.LjWYg5QSdNz9L_XjbtnyoJ66Kg6WIaeaCaxvdaSOb94" >

## Página - Sobre

<img src="https://private-user-images.githubusercontent.com/99279134/302808199-5bc64410-00b4-4a8c-bef8-5dc1eeae7ea9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjQxNjAsIm5iZiI6MTcwNzI2Mzg2MCwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxOTktNWJjNjQ0MTAtMDBiNC00YThjLWJlZjgtNWRjMWVlYWU3ZWE5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNTc0MFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZkYTJjNjVkYWM1OTBkMzcyOTIxYmNhYTc2ODNlOGE4MTJjOTNiYzVlMWMyMzc5M2Q3M2Q5NjQ2ZjgyYTJlZGQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.uwv9w-mk0Ye6a7uiRUk5-ont5vPbcPIGZIkCil63I4U" >


## Página - Sobre

<img src="https://private-user-images.githubusercontent.com/99279134/302808178-2f69e5f4-e046-43fe-a8a6-48a74def331e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjQxNjAsIm5iZiI6MTcwNzI2Mzg2MCwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxNzgtMmY2OWU1ZjQtZTA0Ni00M2ZlLWE4YTYtNDhhNzRkZWYzMzFlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNTc0MFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTYwMjBkNTU3NzBlNjYwZTVmYmYxNzlmODhjOTk2NjE0MTcwNGUyMWQ3NWQ5NWE2MTdkNmU3NzM1N2M1ZDQ3N2MmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.F-Z6H12wwXG5NKRxVHCPpXPHk7e84DXgA63c717B1kw" >

