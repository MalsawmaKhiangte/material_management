# Generated by Django 3.1.3 on 2020-12-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0009_remove_quote_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='email',
            new_name='supplier_email',
        ),
        migrations.AddField(
            model_name='quote',
            name='board_email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]