# Generated by Django 3.0.6 on 2020-05-28 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_auto_20200527_1554'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shor_name')},
        ),
    ]
