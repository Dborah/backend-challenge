# Backend Challenge

Desafio: Criar uma API para gestão de salas de reuniões, de acordo com as especificações apresentadas.

#### Principais tecnologias utilizadas:
Solução desenvolvida em [python](https://www.python.org/) versão 3.6.8.

- [Flask](http://flask.pocoo.org/): Micro Framework Web.
- [PostgreSQL](): Banco de Dados Relacional de alta performance de código aberto.
- [Pycharm Professional](https://www.jetbrains.com/pycharm/): IDE de desenvolvimento Python.
- [Ubuntu](http://releases.ubuntu.com/16.04/): versão Ubuntu 16.04.5 LTS.
- [DBeaver](https://dbeaver.io/download/): Para visualização da Base de Dados. Cliente SQL e ferramenta de administração de banco de dados.

## Preparando o Ambiente

**Iniciando o download do projeto:**

`$ git clone git@github.com:fcschmidt/backend-challenge.git`

Criar um arquivo `.env`

**Adicionando as variáveis de ambiente:**

```text
export FLASK_APP=manage.py
export FLASK_ENV=development
DEBUG=True
DATABASE_URL='dialect+driver://username:password@host:port/database' (opcional)
```

Sobre a configuração do SQLAlchemy: [https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls](https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls).

Caso não seja inserido o caminho `DATABASE_URL` no aquivo `.env`. Por default ele irá criar uma base de dados usando SQLite, no caminho `sqlite:////var/tmp/scheduling_dev.sqlite`.

**Criando um ambiente de desenvolvimento isolado com [virtualenv](https://virtualenv.pypa.io/en/latest/) ou [pipenv](https://pipenv.readthedocs.io/en/latest/):**

`$ virtualenv -p python3.6 .venv`.

**Ativando o ambiente:**
 
`$ source .venv/bin/activate`.

**Instalando as dependências do sistema:**

`$ pip install -r requirements.txt`.


## Gerando Migrações
```bash
flask db init
flask db migrate -m "Created Meeting Room"
flask db upgrade
```

## Executando a aplicação

Executa a aplicação: `$ flask run`.

Rodando na porta padrão, caso não seja alterado: [http://localhost:5000](http://localhost:5000).

Assim que iniciada a aplicação, um arquivo de `log` será criado na pasta logs.

## RestAPI Endpoints 

Endpoints de acesso aos Recursos.

Algumas ferramentas e modulos para acessar os recurso da API:

Via terminal [Curl](https://curl.haxx.se/), 

Usando Scripts em Python com [requests](http://docs.python-requests.org/en/master/),
 
Aplicações para testar API [Postman](https://www.getpostman.com/), [Insomnia](https://insomnia.rest/?utm_content=bufferd23bb&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer).


### API Salas

|Método|URI|Código do Status|Resposta|
|--------|--------|--------|--------|
|POST|`http://127.0.0.1:5000/api/v1/rooms`|201|Nova sala criada com sucesso.|
|PUT|`http://127.0.0.1:5000/api/v1/rooms/<int:room_id>`|200|Sala atualizado com sucesso.|
|DELETE|`http://127.0.0.1:5000/api/v1/rooms/<int:room_id>`|204|Sala deletado com sucesso.|


### API Agendamentos

|Método|URI|Código do Status|Resposta|
|--------|--------|--------|--------|
|POST|`http://127.0.0.1:5000/api/v1/schedules`|201|Agendamento criado com sucesso.|
|PUT|`http://127.0.0.1:5000/api/v1/schedules/<int:scheduling_id>`|200|Agendamento atualizado com sucesso.|
|DELETE|`http://127.0.0.1:5000/api/v1/schedules/<int:scheduling_id>`|204|Agendamento deletado com sucesso.|


### API Listar e Filtrar Agendamentos

|Método|URI|Código do Status|Resposta|
|--------|--------|--------|--------|
|GET|`http://127.0.0.1:5000/api/v1/schedules`|200|Lista todos os Agendamentos.|
|GET|`http://127.0.0.1:5000/api/v1/schedules?date=01/03/2019&room_number=10`|200|Lista e Filtra os Agendamentos por Data e Sala.|


## License
[MIT](https://opensource.org/licenses/MIT) © Fábio Schmidt
