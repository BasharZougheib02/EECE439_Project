# Generated by Django 4.2.5 on 2023-10-07 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactlist',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
