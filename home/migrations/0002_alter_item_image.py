# Generated by Django 4.0.3 on 2022-12-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FilePathField(path='home/static/img'),
        ),
    ]
