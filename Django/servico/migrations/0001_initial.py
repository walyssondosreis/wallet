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
            name='Servico',
            fields=[
                ('alvo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alvo.alvo')),
                ('tipo', models.CharField(max_length=255)),
                ('tempo_estimado', models.TimeField()),
            ],
            bases=('alvo.alvo',),
        ),
    ]
