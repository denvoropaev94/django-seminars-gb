# Generated by Django 4.2.6 on 2023-10-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sem2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savecoin',
            name='coin_variant',
            field=models.CharField(choices=[('О', 'орел'), ('Р', 'решка')], max_length=1),
        ),
    ]