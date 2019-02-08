# Backend Challenge

Desafio: Criar uma API para gestão de salas de reuniões, de acordo com as especificações apresentadas.

#### Principais tecnologias utilizadas:
Solução desenvolvida em [python](https://www.python.org/) versão 3.6.8.

- [Flask](http://flask.pocoo.org/): Micro Framework Web.
- [PostgreSQL](): Banco de Dados Relacional de alta performance de código aberto.
- [Pycharm Professional](https://www.jetbrains.com/pycharm/): IDE de desenvolvimento Python.

## Instalando Dependências

## Executando a aplicação


## Recursos API

Recursos desenvolvidos.

### API Salas

|Método|URI|Código do Status|Resposta|
|--------|--------|--------|
|POST|`http://127.0.0.1:5000/api/v1/rooms`|201|Nova sala criada com sucesso.|
|PUT|`http://127.0.0.1:5000/api/v1/rooms/<int:room_id>`|200|Sala atualizado com sucesso.|
|DELETE|`http://127.0.0.1:5000/api/v1/rooms/<int:room_id>`|204|Sala deletado com sucesso.|


### API Agendamentos

|Método|URI|Código do Status|Resposta|
|--------|--------|--------|
|POST|`http://127.0.0.1:5000/api/v1/schedules`|201|Agendamento criado com sucesso.|
|PUT|`http://127.0.0.1:5000/api/v1/schedules/<int:scheduling_id>`|200|Agendamento atualizado com sucesso.|
|DELETE|`http://127.0.0.1:5000/api/v1/schedules/<int:scheduling_id>`|204|Agendamento deletado com sucesso.|


### API Listar e Filtrar Agendamentos

|Método|URI|Código do Status|Resposta|
|--------|--------|--------|
|GET|`http://127.0.0.1:5000/api/v1/schedules`|200|Lista todos os Agendamentos.|
|GET|`http://127.0.0.1:5000/api/v1/schedules?date=01/03/2019&room_number=10`|200|Lista e Filtra os Agendamentos por Data e Sala.|


## Cobertura dos testes


## LICENSE

