<table>
  <tr>
    <td>
      <img alt="logo" src="https://github.com/user-attachments/assets/fbd63f92-7fd0-4293-b3dd-6804d0c379fa" width="225" />
    </td>
    <td>
      <h1>PROJETO → "Gestão Hotelaria</h1> 
    </td>
  </tr>
</table>
<br>

<img alt="decoração" src="https://github.com/user-attachments/assets/e2b5452a-aac6-4471-bae4-356a6571f94f" width="450" />

### Descrição do projeto →
O projeto "Gestão de Hotelaria" foi realizado com o objetivo de desenvolver uma
aplicação web completa voltada para a administração e gerenciamento de um sistema hoteleriro, oferecendo praticidade, organização e eficiência para os processos internos de um hotel. A proposta principal do sistema é permitir o controle e gerenciamento das principais áreas operacionais do ambiente hoteleiro, centralizando funcionalidades importantes dentro de uma única plataforma web. O sistema foi planejado para auxiliar tanto no gerenciamento administrativo quanto no controle das A aplicação possui funcionalidades voltadas para: <br>
- Cadastro e gerenciamento de hóspedes;
- Controle e administração de quartos;
- Realização e acompanhamento de reservas;
- Gerenciamento de hospedagens;

Uma das requisições do projeto, foram que fossem devidamente utilizados os seguintes programas em sua realização: <br>
- **Backend:** Python com FastAPI <br>
   Responsável pela lógica da aplicação, gerenciamento das rotas, processamento das informações e comunicação com o banco de dados.
- **Frontend:** Jinja2 (renderização de templates) <br>
   Utilizado para a renderização dinâmica dos templates HTML da aplicação, permitindo a integração entre interface e backend.
- **Banco de Dados:** MySQL <br>
  Responsável pelo armazenamento, organização e gerenciamento das informações do sistema.
- **Arquitetura:** MVC (Model, View, Controller) <br>
  Estrutura utilizada para separar responsabilidades dentro da aplicação, facilitando a organização, manutenção e escalabilidade do projeto.
<br>
Todas as informações e instruções para a realização do projeto foram passadas pelo professor orientador da matéria de Back-End Carlos através de um notion enviado:
<br>
<br>
<p align="center">
  <a href="https://teal-arithmetic-d58.notion.site/Sistema-Web-de-Gest-o-Hoteleira-35e7766264ab80a5ae7dfd673ef391f8">
    <img src="https://img.shields.io/badge/📄%20Orientação-Documentação-blue?style=for-the-badge">
  </a>
</p>
<img alt="decoração" src="https://github.com/user-attachments/assets/e2b5452a-aac6-4471-bae4-356a6571f94f" width="450" />

### Instruções de instalação →
Para a execução correta do sistema, é necessário preparar o ambiente de desenvolvimento e instalar todas as dependências utilizadas no projeto.

***Criação de ambiente virtual →*** <br>
Inicialmente, deve-se realizar a clonagem do repositório do projeto através do GitHub. Após acessar a pasta principal da aplicação, recomenda-se a criação de um ambiente virtual Python, permitindo o isolamento das bibliotecas utilizadas no sistema e evitando conflitos com outras instalações existentes na máquina.
A criação do ambiente virtual pode ser realizada com o seguinte comando no terminal:

```bash
    python -m venv venv
```
Após a criação do ambiente virtual, é necessário ativá-lo.
No sistema operacional Windows, utiliza-se:

```bash
  ./venv/Scripts/Activate.ps1 
```

Já em sistemas Linux ou MacOS, utiliza-se:

```bash
  source venv/bin/activate
```

Com o ambiente virtual ativado, deve-se instalar todas as dependências necessárias para o funcionamento da aplicação. Porém asntes de se instalar as dependências que serão utilizadas é necessário que o python esteja em sua versão mais recente, para isso podemos utilizar o comando:

```bash
  python.exe -m pip install --upgrade pip 
```

***Instalação de dependências →*** <br>
Utilizamos algumas dependências para a realização do projeto durante sua criação, a baixo se encontra o passo a passo para a instalação de cada dependência utilizada: <br>

***Fastapi***
```bash
    pip install fastapi
```
ou como uma forma mais completa de instalar o FastAPI com dependências extras é possível utilizar:

```bash
    pip install "fastapi[standard]"
```

***Jinja2***
```bash
    pip install jinja2
```

***Uvicorn***
```bash
   pip install uvicorn
```

***Mysql connector***
```bash
    pip install mysql-connector-python
```

É possível instalar todas as dependências de uma só vez utilizando um único comando, no nosso caso instalamos o Uvicorn junto do Jinja2 por exemplo. Porém segue a baixo o comando para a instalação de todas as dependências juntas:

```bash
      pip install fastapi jinja2 mysql-connector-python uvicorn
```
Caso queira confirmar se todas as dependências foram instaladas é necessário somente utilizar esse comando no terminal:

```bash
      pip list
```


<img alt="decoração" src="https://github.com/user-attachments/assets/e2b5452a-aac6-4471-bae4-356a6571f94f" width="450" />

### Configurações do banco de dados →
Para poder ser realizada a configuração do banco de dados, primeiro de tudo é necessário instalar o MySQL por meio da sua página web oficial. Após sua instalação abra o MySQL workbench e execute o seguinte comando para sua realização

```MySQL
      CREATE DATABASE hotelaria;
        USE hotelaria;
```

Após a criação da DATABASE foi realizada a estrutura base do banco de dados que foi organizada em três tabelas principais: hospedes, quartos e reservas, possuindo relacionamentos entre si através de chaves estrangeiras.

```MySQL
      -- Tabela hospedes
CREATE TABLE hospedes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NULL,
    telefone VARCHAR(20) NULL,
    cpf VARCHAR(14) UNIQUE
);

-- Tabela quartos
CREATE TABLE quartos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    numero VARCHAR(10) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    valor_diaria DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL
);

-- Tabela reservas
CREATE TABLE reservas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    hospede_id INT NOT NULL,
    quarto_id INT NOT NULL,
    data_checkin DATE NOT NULL,
    data_checkout DATE NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    
    FOREIGN KEY (hospede_id) REFERENCES hospedes(id),
    FOREIGN KEY (quarto_id) REFERENCES quartos(id)
);
```
- **Tabela Hospedes**<br>
    A tabela hospedes é responsável por armazenar as informações dos clientes cadastrados no sistema.
- **Tabela Quartos**<br>
    A tabela quartos é responsável pelo armazenamento das informações dos quartos disponíveis no hotel.
- **Tabela Reservas**<br>
    A tabela reservas é responsável pelo gerenciamento das hospedagens realizadas no hotel, relacionando hóspedes e quartos.


<img alt="decoração" src="https://github.com/user-attachments/assets/e2b5452a-aac6-4471-bae4-356a6571f94f" width="450" />

### Configurações da conexão com o MySQL →
Para a criação da conexão entre a aplicação e o banco de dados MySQL a mesma é realizada através do arquivo "dao.py", responsável por estabelecer a comunicação com o banco utilizado pelo sistema.
No arquivo, é utilizada a biblioteca mysql.connector, que permite ao Python acessar e executar comandos no MySQL.

```python
      import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hotelaria"
    )

```
- **host="localhost"** <br>
Define o servidor onde o banco de dados está hospedado.
O termo "localhost" indica que o MySQL está sendo executado na própria máquina do usuário.
- **user="root"** <br>
Define o usuário utilizado para acessar o MySQL.
O usuário "root" é o administrador padrão do banco de dados.
- **password=""** <br>
Campo utilizado para inserir a senha do MySQL.
Caso o banco possua senha configurada, ela deve ser informada entre as aspas.
- **conectar()** <br>
   Retorna uma conexão ativa com o banco de dados, permitindo que outras partes do sistema realizem consultas, inserções, atualizações e exclusões de informações.

<img alt="decoração" src="https://github.com/user-attachments/assets/e2b5452a-aac6-4471-bae4-356a6571f94f" width="450" />

### Como executar o projeto →
Após realizar a instalação das dependências, configuração do ambiente virtual e criação do banco de dados, o sistema poderá ser executado localmente utilizando o servidor Uvicorn, responsável pela execução da aplicação FastAPI.

Inicialmente é necessário acessar a pasta principal do projeto (ou nesse caso o repositório) e em seguida ativar o ambiente virtual através do terminal seguindo os mesmos passos que foram designados na parte de "Instruções de instalação".
Após a ativação do ambiente virtual, execute a aplicação utilizando o comando:

```bash
      uvicorn app:app --reload
```

- **uvicorn** <br>
Inicia o servidor responsável pela execução da aplicação FastAPI.
- **app:app** <br>
O primeiro app refere-se ao nome do arquivo app.py.
O segundo app refere-se à instância criada dentro do arquivo:
- **--reload** <br>
Permite que o servidor reinicie automaticamente sempre que houver alterações no código-fonte, facilitando o desenvolvimento da aplicação.

Após executar o comando, o terminal exibirá uma mensagem semelhante a:

```bash
     Uvicorn running on http://127.0.0.1:8000
```

O sistema poderá ser acessado através do navegador, utilizando o endereço dado pelo próprio terminal:

```bash
      [pip list](http://127.0.0.1:8000)
```


