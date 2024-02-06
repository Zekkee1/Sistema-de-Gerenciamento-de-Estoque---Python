<h1 align="center">
# Sistema-de-Gerenciamento-de-Estoque---Python
</h1>


## Descrição
Este sistema faz a importação de arquivos XML e faz o controle do estoque de acordo com a entrada e saídas de notas ficais apontadas pelo usuário.

Link do Download direto - https://drive.usercontent.google.com/download?id=1rw-VY7GMlEqXYMq7AHsAfpSrRq9Sw8n2


### 

## Ferramentas
<ul>
  <li>Python</li>
  <li>QT Designer</li>
  <li>PySide6</li>
  <li>Pandas</li>
  <li>SQLite - Banco de dados</li>
  <li>PYinstaller</li>
</ul>

## Preview
  ### Pagina - Home
  
<img src="https://private-user-images.githubusercontent.com/99279134/302808185-791b53d5-e411-4e42-a738-e5b552dc77e7.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjMzMzUsIm5iZiI6MTcwNzI2MzAzNSwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxODUtNzkxYjUzZDUtZTQxMS00ZTQyLWE3MzgtZTViNTUyZGM3N2U3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVlMTE3NzI4ZDhjNmNiNzgxODcxMzFjMWQ1NjVjM2RhZTZlZWE1ZTIyNzhlYzQxMjJhNzhkODEzZDBhYmNkODgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.YtPbMuTYlfZnM_KzZLBpJYz35TAUHCK3mdoi8F-Y6Rg" >


  ### Pagina - Importar
  
<img src="https://private-user-images.githubusercontent.com/99279134/302808188-39bbf902-b6d5-4a9d-950e-87dd7a31530f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjMzMzUsIm5iZiI6MTcwNzI2MzAzNSwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxODgtMzliYmY5MDItYjZkNS00YTlkLTk1MGUtODdkZDdhMzE1MzBmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVmMGJmMGViOTMzNjg1NDE3ZDE2ZGU0ZTU2ZTAyY2U5NTRmNjczYmFmZjhkMWRjMmNlYjJlYzc5NGY0N2FlZmImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.v-lLoNhYwoMHWscZpgljeGHxwLxklBVTtut70_ZDzuk" >


  ### Pagina - Tables
  
<img src="https://private-user-images.githubusercontent.com/99279134/302808194-036c4f6c-ca0d-477c-94b8-a1301ed928d1.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjMzMzUsIm5iZiI6MTcwNzI2MzAzNSwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxOTQtMDM2YzRmNmMtY2EwZC00NzdjLTk0YjgtYTEzMDFlZDkyOGQxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTE1OTRkYWM1YmMzOTU1NTE4OTE2ZGI4MmY3NjgwNTk3ODE3ZGE4M2RiOWYwZThhMzBjZTIyNWUwYmU3MmJjZDAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.uaFCJ3PTZO5FP0v0utK3dWCpTERgFT3xh71DdzcTWl4" >

  ### Pagina - Usuários
  
<img src="https://private-user-images.githubusercontent.com/99279134/302808190-dee9e1d0-eed3-4c89-ac40-d62f0b749d49.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjMzMzUsIm5iZiI6MTcwNzI2MzAzNSwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxOTAtZGVlOWUxZDAtZWVkMy00Yzg5LWFjNDAtZDYyZjBiNzQ5ZDQ5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBhY2VkYzc1ZmM2MWFlODYwMjg1MjkzZDBmNjdlNDQyM2Y4YjQ1NjQwMzY4M2U0ZDAzNGMyZDRkNzk2OWZkZWImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.ml8OvJcVma3H6nMJNYGzXLdQ9-lZs24LpkjTMTNC2xI" >

### Pagina - Usuários > cadastro de usuarios

<img src="https://private-user-images.githubusercontent.com/99279134/302808195-0c4f7272-0cd5-4e15-b4da-d6fd1e87399d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjMzMzUsIm5iZiI6MTcwNzI2MzAzNSwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxOTUtMGM0ZjcyNzItMGNkNS00ZTE1LWI0ZGEtZDZmZDFlODczOTlkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM1ZDQzNDU4MDdkZDdlY2U0YzQwODkyMzE5MmQxYmQxODEzY2JhZTgyZWRkOWRlYTNjMzQyMzljYzJmNzViNTcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.qnkB4xzDu0mCMSSGqOO49OKfX4ctmb0lJUjeJjpOAV4" >

### Pagina - Usuários > Atualizar Dados do Usuário

<img src="https://private-user-images.githubusercontent.com/99279134/302808197-814ad65a-6e98-4b76-9218-3cb1fd6ce470.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyNjMzMzUsIm5iZiI6MTcwNzI2MzAzNSwicGF0aCI6Ii85OTI3OTEzNC8zMDI4MDgxOTctODE0YWQ2NWEtNmU5OC00Yjc2LTkyMTgtM2NiMWZkNmNlNDcwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA2VDIzNDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTViYzczZTYzZWIyMmIwN2U3OGI3MjNhMmM1MDhkZmY5MGM4MzE4YTkxNzdiOTZhODY1YWVjNDBiOTJlNWNlMWQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.LjWYg5QSdNz9L_XjbtnyoJ66Kg6WIaeaCaxvdaSOb94" >


