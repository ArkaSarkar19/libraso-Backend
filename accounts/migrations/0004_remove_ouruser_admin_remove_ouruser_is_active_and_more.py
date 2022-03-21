# Generated by Django 4.0.3 on 2022-03-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_ouruser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ouruser',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='ouruser',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='ouruser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff status'),
        ),
    ]