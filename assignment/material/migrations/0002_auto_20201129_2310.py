# Generated by Django 3.1.3 on 2020-11-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='depreciation_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='extra_expense_on',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
