# Generated by Django 3.2.8 on 2022-03-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Usuario',
            field=models.CharField(help_text='Verga', max_length=50, verbose_name='usuario'),
        ),
    ]
