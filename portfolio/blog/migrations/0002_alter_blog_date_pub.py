# Generated by Django 3.2.12 on 2022-02-20 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_pub',
            field=models.DateField(default=datetime.date(2022, 2, 20)),
        ),
    ]