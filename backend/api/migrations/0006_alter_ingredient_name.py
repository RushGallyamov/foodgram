# Generated by Django 3.2.13 on 2022-05-01 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20220430_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]