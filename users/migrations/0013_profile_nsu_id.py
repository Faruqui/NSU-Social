# Generated by Django 2.1.5 on 2019-04-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nsu_id',
            field=models.IntegerField(null=True),
        ),
    ]
