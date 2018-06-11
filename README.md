## for Linux
```
01. [criar pasta]
02. [entrar na pasta - cd pasta]
03. [instalar - python3 -m venv venv]
04. [ativar a virtualização - . venv/bin/activate]
05. [ciar arquivo de dependencia - requirements.txt]
06. [instalar dependencias - pip install -r requirements.txt]
07. [inicializar o banco de dados - python3 manage.py db init]
08. [criar a migração - python3 manage.py db migrate]
09. [atualizar a migração - python3 manage.py db upgrade]
10. [criar o primeiro usuario para administrar o sistema - python3 manage.py adduser 123 admin]
11. [executar o sistema - python3 manage.py runserver]

```
## install packege
pip3 install -r requirements.txt

## Rodar o servidor:
python manage.py runserver

## Links Uteis
1. [Tutoriais do Bootstrap com modelos](https://www.w3schools.com/bootstrap/default.asp)
2. [Elementos Bootstrap](https://getbootstrap.com/docs/3.3/components/#btn-dropdowns-sizing)
3. [Guia basico do GIT](http://rogerdudler.github.io/git-guide/index.pt_BR.html)
4. [Documentação de MarkDown para escrever o ReadME](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) 
5. [Documentação dos Graficos para flask](https://pythonspot.com/flask-and-great-looking-charts-using-chart-js/) 

### Comentarios das paginas
```
/dashboard
Fariamos alguns graficos para apresentar com os relatórios das telas de relatórios.

/
Precisa criar o aviso de usuário invalido.

/admin 
esta acessivel por URL para qualquer tipo de usuario. 
colocar alguma diretiva is admin required

/lancamentos
Impedir que o contador inicie direto ao abrir a pagina. ao clicar em iniciar ele grava a hora no banco em uma tabela reserva e depois quando clicar em terminar ele grava a data e hora de inicio e final. apresentando uma janela para selecionar o projeto e atividade.

Baixei o datepiker pro flask, tem que ver como ele se comporta no post das informações.

/relatorios/horastrabalhadas
Precisa baixar do banco as informações e ja entregar a tabela pronta. Horas trabalhadas pelo usuário em todos os projetos.

/relatorios/horasxprojeto
Ter um selecionador dos projetos do usuario ativo e filtrar as horas por projetos.

/perfil
entendo como tela de edição de usuário. Colocar o upload do avatar. No Base colocar a foto de perfil.

```
