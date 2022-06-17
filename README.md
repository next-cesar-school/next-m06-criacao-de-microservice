![Repository](https://img.shields.io/github/languages/count/next-cesar-school/next-m06-criacao-de-microservice)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

<h1 align="center">Gerenciador de Projetos</h1>

Criação de um microserviço que gerencia a criação e manutenção de novos projetos, a partir de aplicação API.

## 🛠️ Ferramentas e Tecnologias

- Python 3
- IDE: Visual Studio Code
- Flask - framework web usado
- SQLAlchemy - conexão com banco de dados MySQL
- Flask-Restful
- Flask-Migrate

## ⚙️ Funcionalidades

- Lista de projetos cadastrados
- Informações sobre um projeto em específico
- Cadastro de novos projetos
- Atualização de projetos
- Remoção de projetos
- Lista de usuários
- Informações sobre um usuário em específico
- Cadastro de novo usuário
- Remoção de usuários
- Lista de usuários locados em cada projeto
- Relação entre usuários e projetos

## 💻 Como executar o projeto

Antes de iniciar a aplicação é necessário a instalação das seguintes ferramentas: Python, Git e IDE de sua preferência. Além disso, a criação do banco de dados "project_manager" no MySQL.

    
    # Clone este repositório
    $ git clone https://github.com/next-cesar-school/next-m06-criacao-de-microservice.git

    # Acesse a pasta do projeto no terminal
    $ cd next-m06-criacao-de-microservico

    # Inicialize o programa no vscode
    $ code .

    # Instale as dependências
    $ pip install requirements.txt

    # Coloque a senha do seu banco de dados na linha especificada abaixo do arquivo "config_general.py"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:**SuaSenha**@localhost/project_manager'

    # Execute a aplicação em modo de desenvolvimento
    $ flask run

    # O servidor iniciará na porta:5000 - acesse http://localhost:5000/index


## Links úteis

- [Documentação Flask: https://flask.palletsprojects.com ](https://flask.palletsprojects.com)
- [Documentação SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## ✒️ Autores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/pedronb">
        <img src="https://avatars.githubusercontent.com/u/101605764?v=4" width="100px;" alt="Foto de Pedro Bezerra GitHub"/><br>
        <sub>
          <b>Pedro Bezerra</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/PauloCunha4741">
        <img src="https://avatars.githubusercontent.com/u/100804589?v=4" width="100px;" alt="Foto de Paulo Cunha GitHub"/><br>
        <sub>
          <b>Paulo Cunha</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/rdfalmeida">
        <img src="https://avatars.githubusercontent.com/u/82606681?v=4" width="100px;" alt="Foto de Rodolfo Almeida GitHub"/><br>
        <sub>
          <b>Rodolfo Almeida</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="">
        <img src="https://pps.whatsapp.net/v/t61.24694-24/146727662_444870719892891_6316879880955366861_n.jpg?ccb=11-4&oh=990189892b0cc689a44d3e5f81c9f7d3&oe=62BAD732" width="100px;" alt="Foto de Guilherme Carvalho"/><br>
        <sub>
          <b>Guilherme Carvalho</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="">
        <img src="https://pps.whatsapp.net/v/t61.24694-24/266945878_156782213338150_2540409486423836171_n.jpg?ccb=11-4&oh=01_AVyomvyqcdtIc16-axd5C0kFfdqEv1UsKxpi4vl6AREoYw&oe=62B9036D" width="100px;" alt="Foto de Joab Souza"/><br>
        <sub>
          <b>Joab Souza</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## 🎁 Agradecimentos

Agradecemos a toda equipe do programa NExT, realizado pela CESAR School, em especial aos nossos monitores Bruno Fernando e Pedro Victor que se manteram sempre dispostos a nos auxiliar com quaisquer dificuldades durante a elaboração do projeto, além de contribuirem ativamente com o nosso desenvolvimento, não só como alunos, mas como desenvolvedores. 

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/PedroVFPS">
        <img src="https://pps.whatsapp.net/v/t61.24694-24/117654423_642983866656788_8831793664379222594_n.jpg?ccb=11-4&oh=01_AVzaVtAVXdOjrlkxiDrqnGGjEUekbqULpRFXbOoBJcVOdQ&oe=62B9AB17" width="100px;" alt="Foto de Pedro Victor GitHub"/><br>
        <sub>
          <b>Pedro Victor</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Bruno-Fernando">
        <img src="https://avatars.githubusercontent.com/u/20926638?v=4" width="100px;" alt="Foto de Bruno Fernando GitHub"/><br>
        <sub>
          <b>Bruno Fernando</b>
        </sub>
      </a>
    </td>


