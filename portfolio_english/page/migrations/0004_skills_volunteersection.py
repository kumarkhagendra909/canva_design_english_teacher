# Generated by Django 4.2.7 on 2023-11-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_experienceandeducation'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_point1', models.CharField(max_length=100)),
                ('classroom_point2', models.CharField(max_length=100)),
                ('module_design_point1', models.CharField(max_length=100)),
                ('module_design_point2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='volunteersection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer_place', models.CharField(max_length=100)),
                ('volunteer_description', models.CharField(max_length=1000)),
            ],
        ),
    ]
