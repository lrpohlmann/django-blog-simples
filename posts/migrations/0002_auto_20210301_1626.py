# Generated by Django 3.1.4 on 2021-03-01 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ['-data_criacao']},
        ),
    ]
