# Generated by Django 3.2.8 on 2021-10-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='foto',
            field=models.ImageField(upload_to='imagens', verbose_name='foto'),
        ),
    ]
