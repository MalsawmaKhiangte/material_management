# Generated by Django 3.1.3 on 2020-12-03 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0011_district_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
