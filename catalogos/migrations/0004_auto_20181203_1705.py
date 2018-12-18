# Generated by Django 2.1.3 on 2018-12-03 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0003_auto_20181203_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='ag_cruda_recibida',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='ag_tratada_despachada',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='consumo_cloro',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='consumo_sulfato',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='cruda',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(help_text='Descripción de la categoría', max_length=100),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='hr_servidas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='hr_sin_servicio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='tratada',
            field=models.IntegerField(),
        ),
    ]
