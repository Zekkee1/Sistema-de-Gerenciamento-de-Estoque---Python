<h1 align="center">
# Sistema-de-Gerenciamento-de-Estoque---Python
</h1>


# Descrição
Este sistema faz a importação de arquivos XML que são notas fiscais para ter o controle do estoque de acordo com a entrada e saídas apontadas pelo usuário.
Foi desenvolvido utilizando o criador de interface grafica QT Designer para criar o visual do sistema e python junto com Pyside6 para programar todas as funções do sistema
, além disso foi utilizado o Pandas para manipular os dados da tabela e SQLite para criar um banco de dados local.

Link do Download direto - https://drive.usercontent.google.com/download?id=145ObReP85Ly6SBugo7Sd03DS3uuI-kAm

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

<img src="https://github.com/Zekkee1/Sistema-de-Gerenciamento-de-Estoque---Python/assets/99279134/00402bf5-8682-4d7c-abb1-37e2d49353f6">



  ## Página - Home

  #### Pagina inicial do aplicativo
  
<img src="https://github.com/Zekkee1/Sistema-de-Gerenciamento-de-Estoque---Python/assets/99279134/791b53d5-e411-4e42-a738-e5b552dc77e7" >


  ## Página - Importar

  #### Nesta pagina é possivel selecionar a pasta que contem todas as notas fiscais e o sistema cadastrará todas no banco de dados de uma só vez
<img src="https://github.com/Zekkee1/Sistema-de-Gerenciamento-de-Estoque---Python/assets/99279134/39bbf902-b6d5-4a9d-950e-87dd7a31530f" >


  ## Página - Tables > Aba Base

  #### Nesta pagina poderão ser visualizados os dados principais das notas fiscais e o usuário poderá dar baixa e estornar a nota fiscal para o estoque
<img src="https://github.com/Zekkee1/Sistema-de-Gerenciamento-de-Estoque---Python/assets/99279134/036c4f6c-ca0d-477c-94b8-a1301ed928d1" >


  ## Página - Tables > Aba Geral
  #### Nesta pagina o usuário poderá vizualisar os dados gerais de todas as notas cadastradas no banco de dados. 
  #### O usuário com o perfil "administrador" poderá selecionar as notas clicando no numero á esquerda da nota e excluí-las do banco de dados.
  
  <img src="https://github.com/Zekkee1/Sistema-de-Gerenciamento-de-Estoque---Python/assets/99279134/452c9253-019c-4a44-a8c0-e0ee3a449af2" >
  
  O usuário também poderá gerar um excel com o resumo de todas as Notas da tabela geral.
  <img src="https://github.com/Zekkee1/Sistema-de-Gerenciamento-de-Estoque---Python/assets/99279134/e8ffa22d-8026-4cd2-99e3-34c96324c2f2" >


  ## Página - Usuários

  #### Nesta pagina somente usuários com perfil de "Administrador" poderão visualiza-la.
  #### O Administrador tambem poderá cadastrar um novo usuário.
  #### Ao selecionar um usuário da tabela o "Administrador" poderá: excluir usuário, atualizar dados do usuário.
<img src="https://github.com/Zekkee1/Sistema-de-Gerenciamento-de-Estoque---Python/assets/99279134/dee9e1d0-eed3-4c89-ac40-d62f0b749d49" >

## Página - Usuários > cadastro de usuarios

#### Nesta página o administrador poderá cadastrar um novo usuário no banco de dados.
<img src="https://github.com/Zekkee1/Sistema-de-Gerenciamento-de-Estoque---Python/assets/99279134/0c4f7272-0cd5-4e15-b4da-d6fd1e87399d" >

## Página - Usuários > Atualizar Dados do Usuário

#### Nesta página o administrador poderá atualizar os dados do usuário selecionado.
<img src="https://github.com/Zekkee1/Sistema-de-Gerenciamento-de-Estoque---Python/assets/99279134/814ad65a-6e98-4b76-9218-3cb1fd6ce470" >

## Página - Sobre

<img src="https://github.com/Zekkee1/Sistema-de-Gerenciamento-de-Estoque---Python/assets/99279134/5bc64410-00b4-4a8c-bef8-5dc1eeae7ea9" >


## Página - Contato

<img src="https://github.com/Zekkee1/Sistema-de-Gerenciamento-de-Estoque---Python/assets/99279134/2f69e5f4-e046-43fe-a8a6-48a74def331e" >

