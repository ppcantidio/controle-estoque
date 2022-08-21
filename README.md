# controle-estoque

Camadas:

routes: controla entrada e saida de dados(valida entrada e organiza a saida e apresentacao atraves da camada de schemas)

service: camada que controla as regras de negocio e invoca operacoes de banco de dados da camada db

schemas: armazena padronizacoes de entrada e saida de dados

db: armazena tabelas e suas respectivas funcoes

utils: armazena funcoes de utilidade, funcoes de erro, logis, redis cache
