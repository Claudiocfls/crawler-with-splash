# crawler-with-splash

Crawler baseado no framework Scrapy com download middlewares customizados.

Esse crawler utiliza o Splash para renderizar páginas com Javascript.

As páginas acessadas serão salvas em um banco de dados e para executar o projeto é necessário configurar esse acesso com as credenciais corretas.

No arquivo docker-compose.yml existe algumas variáveis que também devem ser editadas para que o crawler seja iniciado corretamente.

Para executar o crawler basta executar o seguinte comando na raiz do projeto:

docker-compose up --build