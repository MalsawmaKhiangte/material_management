# Generated by Django 3.1.3 on 2020-11-30 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201129_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('', '--------'), ('Aizawl', 'Aizawl'), ('Lunglei', 'Lunglei')], default=0, max_length=20),
            preserve_default=False,
        ),
    ]
