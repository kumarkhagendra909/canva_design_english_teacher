# Generated by Django 4.2.7 on 2023-11-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_aboutussection'),
    ]

    operations = [
        migrations.CreateModel(
            name='experienceandeducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(max_length=4)),
                ('work_role', models.CharField(max_length=50)),
                ('work_place', models.CharField(max_length=100)),
                ('work_description', models.CharField(max_length=500)),
            ],
        ),
    ]
