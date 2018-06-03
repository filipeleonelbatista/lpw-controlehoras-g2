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

/admin/projetos
Testar o permissionamento, somente quem tiver o codigo de administrador pode abrir esta pagina

/admin/clientes
Testar o permissionamento, somente quem tiver o codigo de administrador pode abrir esta pagina

/admin/funcionarios
Testar novamente o cadastro do funcionario. Está funcionando o delete, falta o update.

/admin/atividades
Testar o permissionamento, somente quem tiver o codigo de administrador pode abrir esta pagina

/lancamentos
Impedir que o contador inicie direto ao abrir a pagina. ao clicar em iniciar ele grava a hora no banco em uma tabela reserva e depois quando clicar em terminar ele grava a data e hora de inicio e final. apresentando uma janela para selecionar o projeto e atividade.

Baixei o datepiker pro flask, tem que ver como ele se comporta no post das informações.

/relatorios/horastrabalhadas
Precisa baixar do banco as informações e ja entregar a tabela pronta. Horas trabalhadas pelo usuário em todos os projetos.

/relatorios/horasxprojeto
Ter um selecionador dos projetos do usuario ativo e filtrar as horas por projetos.

/perfil
entendo como tela de edição de usuário. Colocar o upload do avatar. No Base colocar a foto de perfil.

/logout
quando clicar deve executar uma  função que derrube a sessão do usuário e mande pra tela inicial o  "/"

```
