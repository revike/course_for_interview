# Generated by Django 3.2 on 2021-04-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gooditem',
            name='modified_at',
            field=models.DateTimeField(verbose_name='Изменено'),
        ),
    ]