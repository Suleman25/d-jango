# Generated by Django 5.1.2 on 2024-11-13 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='best_seller',
            field=models.BooleanField(default=False),
        ),
    ]
