# Generated by Django 2.1.5 on 2019-04-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_student_date_registered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]