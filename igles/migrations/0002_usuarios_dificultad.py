# Generated by Django 4.1.2 on 2022-10-24 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='dificultad',
            field=models.CharField(choices=[('1', 'Beginner'), ('2', 'Intermediate')], default='1', max_length=25),
        ),
    ]
