# Generated by Django 3.1.3 on 2020-11-30 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0007_auto_20201130_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='idle',
        ),
        migrations.DeleteModel(
            name='District',
        ),
    ]