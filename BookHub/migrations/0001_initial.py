# Generated by Django 4.2.11 on 2024-10-27 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=256)),
                ('autor', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('editora', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('dataPublicacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=128)),
                ('livrosFavoritos', models.ManyToManyField(related_name='usuarios_favoritos', to='BookHub.livro')),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('conteudo', models.TextField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('de', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_enviadas', to='BookHub.usuario')),
                ('para', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_recebidas', to='BookHub.usuario')),
            ],
        ),
    ]
