# Generated by Django 3.1.3 on 2020-12-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0004_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='msg',
            field=models.TextField(blank=True, null=True),
        ),
    ]
