# Generated by Django 4.2.6 on 2023-10-16 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sem2', '0002_alter_savecoin_coin_variant'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='savecoin',
            options={'ordering': ['-date']},
        ),
    ]
