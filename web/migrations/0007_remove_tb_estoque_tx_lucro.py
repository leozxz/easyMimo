# Generated by Django 3.1.4 on 2020-12-08 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20201208_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_estoque',
            name='tx_lucro',
        ),
    ]
