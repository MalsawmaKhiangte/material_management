# Generated by Django 3.1.3 on 2020-12-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0012_auto_20201202_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='aizawl',
            name='send_to',
            field=models.CharField(blank=True, choices=[('', '--------'), ('Aizawl', 'Aizawl'), ('Lunglei', 'Lunglei')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lunglei',
            name='send_to',
            field=models.CharField(blank=True, choices=[('', '--------'), ('Aizawl', 'Aizawl'), ('Lunglei', 'Lunglei')], max_length=20, null=True),
        ),
    ]
