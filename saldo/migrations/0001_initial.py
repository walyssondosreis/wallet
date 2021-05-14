# Generated by Django 3.2.2 on 2021-05-14 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Saldo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo_atual', models.DecimalField(decimal_places=2, max_digits=8)),
                ('saldo_mensal', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
