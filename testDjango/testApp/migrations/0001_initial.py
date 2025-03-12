# Generated by Django 5.1.7 on 2025-03-12 08:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testAppVariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='apps/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('A1', 'APP1'), ('A2', 'APP2'), ('A3', 'APP3'), ('A4', 'APP4'), ('A5', 'APP5')], max_length=2)),
            ],
        ),
    ]
