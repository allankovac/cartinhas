# Generated by Django 4.2.2 on 2023-06-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_jogador'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='reserva',
            field=models.BooleanField(default=False),
        ),
    ]