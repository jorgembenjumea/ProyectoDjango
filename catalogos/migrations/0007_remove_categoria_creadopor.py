# Generated by Django 2.1.3 on 2018-12-10 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0006_categoria_creadopor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='creadopor',
        ),
    ]