# Generated by Django 2.1.5 on 2019-04-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190316_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
