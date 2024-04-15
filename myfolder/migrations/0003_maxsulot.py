# Generated by Django 5.0.3 on 2024-03-28 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfolder', '0002_alter_users_fam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maxsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
                ('narxi', models.FloatField()),
                ('rasm_url', models.CharField(max_length=500)),
                ('turi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfolder.turlar')),
            ],
        ),
    ]
