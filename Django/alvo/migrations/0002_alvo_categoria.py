# Generated by Django 3.2.2 on 2021-05-14 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('alvo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alvo',
            name='categoria',
            field=models.ManyToManyField(to='categoria.Categoria'),
        ),
    ]
