from django.db import models

# Create your models here.


class Departamento(models.Model):
    nome = models.CharField(max_length=70)

    def __str__(self):
        return self.nome

class CPF(models.Model):
    numero = models.CharField(max_length=15)
    data_exp = models.TimeField(auto_now=False)

    def __str__(self):
        return self.numero

class Cliente(models.Model):
    nome = models.CharField(max_length=70, blank=False, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=True, default=0.0)
    idade = models.IntegerField(default=0)
    email = models.EmailField(default='mail@mail.com')
    cpf = models.OneToOneField(CPF, null=True, on_delete=models.CASCADE)
    departamentos = models.ManyToManyField(Departamento, blank=True, default=None)
    def __str__(self):
        return self.nome


class Telefone(models.Model):
    numero = models.CharField(max_length=20, default='00000000000')
    descricao = models.CharField(max_length=30, default='Numero de telefone')
    # Relacionamento 1:N
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=0)

    def __srt__(self):
        return self.descricao
    
