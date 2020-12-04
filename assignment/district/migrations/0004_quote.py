# Generated by Django 3.1.3 on 2020-12-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0003_auto_20201201_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('quantity', models.CharField(max_length=10)),
                ('For_District', models.CharField(max_length=30)),
                ('supplier', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
            ],
        ),
    ]
