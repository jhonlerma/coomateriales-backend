# Generated by Django 4.0.6 on 2022-08-03 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_fabricante', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nit_proveedor', models.CharField(max_length=50, unique=True)),
                ('nombre_proveedor', models.CharField(max_length=40)),
                ('telefono_proveedor', models.CharField(max_length=40)),
                ('correo_proveedor', models.CharField(max_length=40, unique=True)),
                ('direccion_proveedor', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=40)),
                ('marca_producto', models.CharField(max_length=40)),
                ('precio_unit_producto', models.IntegerField()),
                ('resumen_producto', models.CharField(max_length=40)),
                ('detalle_producto', models.CharField(max_length=255)),
                ('categoria_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categoria', to='coomaterialesApp.categoria')),
                ('fabricante_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fabricante', to='coomaterialesApp.fabricante')),
                ('proveedor_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proveedor', to='coomaterialesApp.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('nombre_usuario', models.CharField(max_length=40)),
                ('apellido_usuario', models.CharField(max_length=40)),
                ('telefono_usuario', models.CharField(max_length=40)),
                ('correo_usuario', models.EmailField(max_length=256)),
                ('direccion_usuario', models.CharField(max_length=60)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
