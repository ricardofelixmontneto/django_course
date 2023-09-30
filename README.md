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

# URL Regex
O URL resolution do Django também trabalha com regex e é interessante para evitar comportamentos não desejados ao chamar urls

# Arquitetura Django
O Jungle utiliza a arquitetura MVT(model view template) como base, se compararmos com MVC(model view controller) a view tem o papel do controller




