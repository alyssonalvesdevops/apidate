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


### Observabilidade

Para monitorar a Saúde do serviços basta acessar a URL do Elastic, fazer o login e senha e ir em Observabilidade > APM > apidate

<img src="https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/bltcaa68210be0c357f/618ac4f194e50d5a6380207d/screenshot-apm-deploy-with-confidence.png">


