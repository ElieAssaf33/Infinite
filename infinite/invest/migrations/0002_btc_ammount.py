# Generated by Django 5.0.2 on 2024-02-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='btc',
            name='ammount',
            field=models.FloatField(null=True),
        ),
    ]
