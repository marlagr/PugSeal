# Generated by Django 3.1.1 on 2020-11-29 19:28

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telefono', models.CharField(max_length=255)),
                ('rol', models.CharField(default=' ', max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id_hotel', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(default='', max_length=255)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(default='', max_length=255, unique=True)),
                ('nombre_proveedor', models.CharField(default='', max_length=255)),
                ('email', models.CharField(default='', max_length=255, null=True)),
                ('telefono', models.CharField(max_length=10)),
                ('fechaAlianza', models.DateField(default=datetime.date.today)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id_ubicacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requisicion',
            fields=[
                ('id_requisicion', models.AutoField(primary_key=True, serialize=False)),
                ('concepto', models.CharField(max_length=255)),
                ('enlace_concepto', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('justificacion', models.TextField(blank=True, max_length=500, null=True)),
                ('cantidad', models.IntegerField(default=1)),
                ('costo', models.FloatField(default=0)),
                ('categoria', models.CharField(blank=True, default='', max_length=255)),
                ('fecha_creacion', models.DateField(default=django.utils.timezone.now)),
                ('fecha_estimada', models.DateField(blank=True, null=True)),
                ('fecha_entrega', models.DateField(blank=True, null=True)),
                ('aprobacion_auditor', models.BooleanField(default=False)),
                ('aprobacion_director_gral', models.BooleanField(default=False)),
                ('proveedor', models.CharField(blank=True, max_length=255, null=True)),
                ('metodo_de_pago', models.CharField(blank=True, max_length=255, null=True)),
                ('observaciones', models.TextField(blank=True, default='', null=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('id_hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pugsealapp.hotel')),
                ('id_solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='solicitante', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Requisiciones',
            },
        ),
        migrations.CreateModel(
            name='Mantenimiento_Preventivo',
            fields=[
                ('id_mantprev', models.AutoField(primary_key=True, serialize=False)),
                ('actividad', models.CharField(max_length=255)),
                ('cotizacion', models.FloatField(default=0)),
                ('frecuencia_anual', models.IntegerField(default=0)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('aprobado', models.BooleanField(default=False)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('duracion_horas', models.FloatField(blank=True, default=0, null=True)),
                ('fecha_terminacion', models.DateField(blank=True, null=True)),
                ('comentarios_encargado', models.CharField(blank=True, max_length=1000, null=True)),
                ('comentarios_supervisor', models.CharField(blank=True, max_length=1000, null=True)),
                ('comentarios_auditor', models.CharField(blank=True, max_length=1000, null=True)),
                ('id_auditor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auditor', to=settings.AUTH_USER_MODEL)),
                ('id_categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pugsealapp.categoria')),
                ('id_empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empleado', to=settings.AUTH_USER_MODEL)),
                ('id_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pugsealapp.proveedor')),
                ('id_supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervisor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Solicitudes de Mantenimiento Preventivo',
            },
        ),
        migrations.CreateModel(
            name='Mantenimiento_Correctivo',
            fields=[
                ('id_mantcor', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_solicitud', models.DateField(default=django.utils.timezone.now)),
                ('semana', models.IntegerField(default=0)),
                ('descripcion_problema', models.CharField(max_length=255)),
                ('costo_trabajo', models.FloatField(blank=True, default=0, null=True)),
                ('costo_material', models.FloatField(blank=True, default=0, null=True)),
                ('horas_trabajo', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('fecha_finalizacion', models.DateField(blank=True, null=True)),
                ('comentario_supervisor', models.TextField(blank=True, max_length=500, null=True)),
                ('calif_calidad', models.IntegerField(blank=True, default=1, null=True)),
                ('calif_terminacion', models.IntegerField(blank=True, default=1, null=True)),
                ('calif_limpieza', models.IntegerField(blank=True, default=1, null=True)),
                ('calif_totalidad', models.IntegerField(blank=True, default=1, null=True)),
                ('finalizada', models.BooleanField(default=False)),
                ('estado', models.CharField(blank=True, default='', max_length=255)),
                ('id_area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pugsealapp.area')),
                ('id_categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pugsealapp.categoria')),
                ('id_encargado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='encargado_correctivo', to=settings.AUTH_USER_MODEL)),
                ('id_hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pugsealapp.hotel')),
                ('id_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pugsealapp.proveedor')),
                ('id_solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='encargado_solicitud', to=settings.AUTH_USER_MODEL)),
                ('id_supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervisor_correctivo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Solicitudes de Mantenimiento Correctivo',
            },
        ),
        migrations.CreateModel(
            name='Bitacora_Mediciones',
            fields=[
                ('id_medicion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('cloro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('porcentaje_nivel_agua', models.DecimalField(decimal_places=2, max_digits=10)),
                ('porcentaje_gas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('luz', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lectura', models.DecimalField(decimal_places=2, max_digits=10)),
                ('presion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_alberca_jacuzzi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_caldera', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observaciones', models.CharField(default='', max_length=255, unique=True)),
                ('auditor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auditor_name', to=settings.AUTH_USER_MODEL)),
                ('responsable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsable_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bitácora Mediciones',
            },
        ),
    ]