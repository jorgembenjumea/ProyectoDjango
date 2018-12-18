# Generated by Django 2.1.3 on 2018-12-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0009_auto_20181210_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procesosplanta',
            name='alcalinidad_sal_tq_distribucion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='cloro_res_sal_sedimentadores',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='cloro_res_sal_tq_distribucion',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='color_sal_sedimentadores',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='color_sal_tq_distribucion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='hora',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='ph_ag_cruda',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='ph_sal_tq_desinfeccion',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='ph_sal_tq_distribucion',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='temperatura_ag_cruda',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='temperatura_sal_tq_distribucion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='turbiedad_ag_cruda',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='turbiedad_sal_sedimentadores',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='turbiedad_sal_tq_desinfeccion',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='procesosplanta',
            name='turbiedad_sal_tq_distribucion',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
