# Generated by Django 4.2 on 2023-04-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_funcionario_alter_usuario_cep_alter_usuario_senha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cep',
        ),
        migrations.AddField(
            model_name='usuario',
            name='endereco',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]