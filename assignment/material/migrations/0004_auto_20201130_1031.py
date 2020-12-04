# Generated by Django 3.1.3 on 2020-11-30 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0003_auto_20201130_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='code',
        ),
        migrations.AddField(
            model_name='material',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_district', to='material.district'),
        ),
    ]
