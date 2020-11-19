# Generated by Django 3.1.3 on 2020-11-19 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id_vendedor', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome_vendedor', models.CharField(max_length=200)),
                ('login_vendedor', models.CharField(max_length=100)),
                ('email_vendedor', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome_produto', models.CharField(max_length=100)),
                ('qtd_estoque', models.IntegerField()),
                ('preco', models.FloatField()),
                ('ativo', models.BooleanField(default=True)),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]