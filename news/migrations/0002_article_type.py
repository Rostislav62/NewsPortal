# Generated by Django 4.2.14 on 2024-09-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.BooleanField(default=False),
        ),
    ]
