from django.contrib import admin
from .models import (Cliente, 
                     Telefone, 
                     CPF,
                     Departamento)


# Register your models here.

# Essa linha registra o model no Admin do Django, podemos acessar via navegador em http://127.0.0.1:8000/admin
admin.site.register(Cliente)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)