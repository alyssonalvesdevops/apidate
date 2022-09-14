## API Date

API simples em python que retorna hora por timezona e aplica observabilidade com a ElasticStack.

### Tecnologias
- Docker
- Docker Compose
- Python
- ElasticStack
- API Rest Terceiro
- 
### Guia de implantação

Para execução você vai precisar do docker, docker-compose e ElasticStack qualquer versão com a extensão de APM habilitada.
Seguir os seguinte passos;

- Modifique o nome do arquivo `env-exemplo` para `.env`
- Rodar o comando `docker-compose up`(adicione o `-d` para liberar o terminal) 

### Guia de uso

Execute uma resquest para o host `http://localhost/` com o header `timezone`, por exemplo;
usando o curl;

    curl --request GET 'http://localhost/' --header 'timezone: America/Fortaleza'




