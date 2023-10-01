"""
URL configuration for djangoCourse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from .views import home
from clientes.views import (clientes, 
                            cliente_detalhe, 
                            cliente_por_nome)

from django.conf import settings
from django.conf.urls.static import static

# O url resolution lê essa lista em ordem crescente de índice
urlpatterns = [
    re_path('^$', home, name='home'), # ^$ força que a url comece e termine vazia
    re_path('^clientes/$', clientes, name='clientes'),
    re_path('^cliente/(?P<id>\d{1,3})$', cliente_detalhe, name='cliente_detalhe'), # P no regex significa Parameter
    re_path('^cliente/(?P<nome>\w+)', cliente_por_nome, name='cliente_por_nome'),
    path('admin/', admin.site.urls), # antigamente o django utilizava url() ao invés de path() como padrão e sempre aceitava regex
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
