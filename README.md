## lpw-controlehoras-g2
Trabalho do Tales 2018/1

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

## Questões pendentes.
1. Colocar o @login.require nas rotas para impedir o acecsso.
2. Colocar o if admini no menu para verificar se o usuario é administrador e liberar o menu de administrador.
3. terminar os outros cadastros

### Comentarios das paginas
```
/
A pagina de login está pronta, precisa fazer a criação do primeiro usuario e testar a validação.

/admin/projetos
Testar o permissionamento, somente quem tiver o codigo de administrador pode abrir esta pagina

/admin/clientes
Testar o permissionamento, somente quem tiver o codigo de administrador pode abrir esta pagina

/admin/funcionarios
Testar o permissionamento, somente quem tiver o codigo de administrador pode abrir esta pagina

/admin/atividades
Testar o permissionamento, somente quem tiver o codigo de administrador pode abrir esta pagina

/lancamentos
Programar o contador de horas para iniciar o contador e gravar. ao clicar em iniciar ele grava a data e hora que iniciou e ao clicar em gravar ele grava a data e hora que parou. só quando clicar em gravar a informação deve ir para a tabela oficial, poderiamos ter uma tabela de buffer pra evitar problemas.
Baixei o datepiker pro flask, tem que ver como ele se comporta no post das informações.

/relatorios/horastrabalhadas
Precisa baixar do banco as informações e ja entregar a tabela pronta.

/relatorios/horasxprojeto
não tive ideia ainda de como funciona. devemos ver com o tales

/relatorios
como seriam 2 telas conforme citado a cima podemos usar isso na tela inicial, para apresentar algo e nao deixar ela vazia

/perfil
entendo como tela de edição de usuário. Verificar se nao existe a necessidade de uma Foto de perfil

/logout
quando clicar deve executar uma  função que derrube a sessão do usuário e mande pra tela inicial o /

```
### Comentários adicionais
Na pagina base do bootstrap ja está com o IF no menu. só nao Habilitei por que nao tem um usuário validado e ativo que podemos usar.

Precisamos verificar o menu por que nao está muito responsivo. se voce olhar no celular nao fica top. falta isso pra ficar bom.
#run app
python3 manage.py runserver
