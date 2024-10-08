# Generated by Django 5.1.1 on 2024-09-06 03:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pais_origen', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='auto',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='modelo',
            name='marca',
        ),
        migrations.AddField(
            model_name='auto',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='autos.cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modelo',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='autos.cliente'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
    ]
