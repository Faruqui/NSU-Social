# Generated by Django 2.1.5 on 2019-04-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_profile_nsu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
