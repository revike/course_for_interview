# Generated by Django 3.2 on 2021-04-21 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_alter_gooditem_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gooditem',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Изменено'),
        ),
    ]