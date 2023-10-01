# Generated by Django 4.2.5 on 2023-09-30 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_telefone_cliente_alter_cliente_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('data_exp', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cpf'),
        ),
    ]
