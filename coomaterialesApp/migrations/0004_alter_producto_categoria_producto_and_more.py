# Generated by Django 4.0.6 on 2022-08-05 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coomaterialesApp', '0003_alter_producto_fabricante_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria_producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categoria', to='coomaterialesApp.categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fabricante_producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fabricante', to='coomaterialesApp.fabricante'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='proveedor_producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proveedor', to='coomaterialesApp.proveedor'),
        ),
    ]
