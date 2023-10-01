# django_course
Repositório para o curso de django

## Iniciando um novo projeto
```$ django-admin startproject <nome_do_projeto>```

manage.py é um utilitário de linha de comando


## Criando banco de dados SQLite3
No arquivo setting.py configurar a variavel DATABASES


## Primeiro comando através do manage.py
Criar e atualizar banco de dados
$ python manage.py migrate

## Run server
$ python manage.py runserver
dessa forma podemos acessar o a url http://127.0.0.1:8000/ no navegador
Como só temos uma rota criada que é /admin no arquivo urls.py podemos chamar http://127.0.0.1:8000/admin no navegador

1. Criando um novo usuário para o Django Admin
$ python manage.py createsuperuser
user: admin
e-mail: admin@admin.com
password: @Admin123


## Django Admin
Provê interface de admin do site automática, utilizando os modelos do Django
Lê do banco de dados e trás para a interface web
Já vem com 2 models/entidades: usuários e grupos (de usuário).
A entidade usuário armazena por exemplo os usuários criados a partir do comando $ python manage.py createsuperuser

# Request Lifecycle
https://nitinnain.com/djangos-request-response-cycle/
Client -> web server (nginx/apache) -> wsgi -> url resolution(procura em urls.py) -> view (seu código python para lidar com deterinado problema, acessa models, managers e databases caso necessário)  -> cria o response com o template html -> wsgi -> 
web server (nginx/apache) -> client  

# Criando View

Criar um arquivo com nome views.py no mesmo nível que urls.py e wsig.py

Nesse arquivos serão escritas as funções de entrada a partir de uma ulr dentro de urls.py
https://docs.djangoproject.com/en/4.2/topics/class-based-views/


# URL Regex
O URL resolution do Django também trabalha com regex e é interessante para evitar comportamentos não desejados ao chamar urls

# Arquitetura Django
O Jungle utiliza a arquitetura MVT(model view template) como base, se compararmos com MVC(model view controller) a view tem o papel do controller

Para leitura: https://dev.to/kputra/rails-skinny-controller-skinny-model-5f2k
Resumo: as views tem que ser pequenas com pouca lógica e os models fazem o trabalho pesado.
"Skinhy controller(view) and fat models"

## Django Apps
Criar o módulo view na raiz do projeto é interessante apenas para armazenar views genéricas que no caso desse projeto é a home interessantes, para armazenar outras views o django utiliza apps para separar a aplicação por domínios por exemplo clientes e produto
- Os projetos Django são baseado em aplicações

Criando a app clientes $ python manage.py startapp clientes 

Sempre que criamos uma nova aplicação precisamos registrar no modulo settings.py em INSTALLED_APPS

## Models

O model mapeia as entidades do banco de dados e podemos adicionar à esses models acões.

Referências: https://docs.djangoproject.com/en/4.2/ref/models/fields/

Depois de criar um model rodar $ python manage.py makemigrations
Esse comando vai criar um arquivo de migrations(plano de criação de tabelas) dentro do app clientes/migrations/<numero_migration>_initial.py

Para criar essa model como tabela no banco de dados agora que temos um arquivo migrations criado, devemos executar o comando
$ python manage.py migrate

Para acessar o banco devemos utilizar a linha de comando do shell disponibilizada pelo Djando via manage.py
$ python manage.py shell
Então podemos acessar e manipular dados no banco através da interação com a classe model Cliente

Podemos inserir novos registros da mesma forma
$ Cliente.objects.create(nome='Maria', endereco='Rua Maria Jose - n 10')

Para realizar consulta no usuário criado
$ c = Cliente.objects.all()[0]
$ c.id # primary key incremental criada automaticamente pelo Django
$ c.nome
$ c.endereco

Dúvida: os arquivos do diretório migrations devem ser versionados ou sempre devemos executar o comando makemigrations?
Parece que prcisamos versionar esses arquivos mas ainda não entendi o motivo, pesquiar sobre.
Resposta: https://pt.stackoverflow.com/questions/452178/%C3%89-correto-versionar-os-arquivos-das-migrations-e-o-arquivo-de-configura%C3%A7%C3%A3o#:~:text=Pensando%20que%20a%20filosofia%20da,altera%C3%A7%C3%B5es%20no%20banco%20de%20dados.

Obs: sempre que houver mudança ou criação de novas models, executar os comandos:
$ python manage.py makemigrations
$ python manage.py migrate


## Personalizando Django Admin

Fonte: https://docs.djangoproject.com/en/4.2/ref/contrib/admin/


## Templates

Não é boa prática colocar cálculos complexos em template html, o ideal é calcular no backend python view ou model e retornar esses valores em variáveis para o render renderizar o template com variáveis injetadas com a notação {{ }}
Ex: {{minha_variavel}} 

O sistema de templates do Django é o Jinja, o mesmo que pode ser utilizado no Flask