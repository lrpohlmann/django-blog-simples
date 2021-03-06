# Generated by Django 3.1.4 on 2020-12-26 01:51

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
            name='AssuntoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=100)),
                ('corpo', models.TextField(max_length=2000)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_alteracao', models.DateField(auto_now=True)),
                ('imagem', models.ImageField(upload_to='post/')),
                ('assunto', models.ManyToManyField(to='posts.AssuntoModel')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ComentarioModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corpo', models.TextField(max_length=300)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.postmodel')),
            ],
        ),
    ]
