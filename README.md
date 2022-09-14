## API Date

API simples em python que retorna hora por timezona e aplica observabilidade com a ElasticStack.

### Tecnologias
- Docker
- Docker Compose
- Python
- Flask
- Gunicorn
- ElasticStack
- API Rest Terceiro

### Guia de implantação

Para execução você vai precisar do [docker](https://docs.docker.com/engine/install/), [docker-compose](https://docs.docker.com/compose/install/) e [ElasticStack](https://www.elastic.co/pt/downloads/) qualquer versão com a extensão de APM habilitada.
Seguir os seguinte passos;

- Modifique o nome do arquivo `env-exemplo` para `.env`
- Rodar o comando `docker-compose up`(adicione o `-d` para liberar o terminal) 

### Guia de uso

Execute uma resquest para o host `http://localhost/` com o header `timezone`, por exemplo;
usando o curl;

    curl --request GET 'http://localhost/' --header 'timezone: America/Fortaleza'




