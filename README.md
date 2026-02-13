# Lista de Desejos de Filmes e Séries Usando Python e Flask

Este projeto é uma aplicação web simples que permite aos usuários criar e gerenciar uma lista de desejos de filmes e séries. A aplicação é construída usando Python e Flask, sendo uma projeto ideal para iniciantes que desejam aprender sobre desenvolvimento web com Flask e pedido para ser feito por nossos professores do Senai, João Roccella e Edgard. Esse porjeto foi estilizado usando o framework Bootstrap para garantir uma interface amigável e responsiva. Usamos também uma integração com o bando de dades SQLite para armazenar as informações das atividades. Esse projeto foi fundamental para o aprendizado de conceitos como rotas, templates, formulários e manipulação de banco de dados em Flask. A aplicação permite aos usuários adicionar filmes ou séries à sua lista de desejos, visualizar a lista completa e remover itens conforme necessário. É uma ótima maneira de praticar habilidades de desenvolvimento web e criar um projeto funcional e divertido!

links úteis e usados de base para estilizar com o bootstrap: 
 - [CSS variables](https://getbootstrap.com/docs/5.3/customize/css-variables/)
 - [Bootstrap 5 CheatSheet](https://bootstrap-cheatsheet.themeselection.com/)
 - [Cheatsheet OFC document](https://getbootstrap.com/docs/5.3/examples/cheatsheet/)

Para implementar este projeto, você pode seguir os seguintes passos:

1. Faça um Fork deste repositório para sua conta, clicando no botão "Fork" no canto superior direito da página do repositório no GitHub.

2. Clone o repositório para sua máquina local usando o comando:

    ~~~bash
    git clone <url_seu_repositorio>
    ~~~

3. abra seu porjeto no IDE preferido

4. Crie, preferencialmente, um ambiente virtual para o projeto e ative-o:

    - Criação do ambiente virtual:    
    ~~~bash
    python -m venv venv
    ~~~

    - Ativação do ambiente virtual:
    - No bash:
    ~~~bash
    source .venv/Scripts/activate
    ~~~
    - No PowerShell:
    ~~~powershell
    .\.venv\Scripts\Activate.ps1
    ~~~

5. Instale todas as dependências constantes no arquivo `requirements.txt`:

    ~~~python 
    pip install -r requirements.txt
    ~~~

6. Copie o arquivo `.env.example` cole na riaz do projeto e renomeie para `.env`

7.  Edite um arquivo `.env` para definir o caminho do banco de dados na
     `DATABASE`. Exemplo:

    ~~~env
    DATABASE='./data/meubanco.db'
    ~~~

8. Rode a aplicação no Python ultilizando o comando:

    ~~~bash
    flask run
    ~~~

9. Acesse a aplicação no navegador através do endereço e porta endicados no terminal. Exemplo:
`http://127.0.0.1:5000`

10. Agora você pode começar a usar a aplicação para criar e gerenciar sua lista de desejos!

