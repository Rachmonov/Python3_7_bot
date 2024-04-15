# Generated by Django 5.0.3 on 2024-04-01 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfolder', '0003_maxsulot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Savdo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.IntegerField()),
                ('number', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfolder.maxsulot')),
            ],
        ),
    ]