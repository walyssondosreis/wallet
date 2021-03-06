# Generated by Django 3.2.2 on 2021-05-14 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alvo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('alvo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alvo.alvo')),
                ('modelo', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('cod_barra', models.CharField(max_length=255)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=8)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data_validade', models.DateField()),
                ('data_fabricacao', models.DateField()),
                ('imagem', models.CharField(max_length=255)),
            ],
            bases=('alvo.alvo',),
        ),
    ]
