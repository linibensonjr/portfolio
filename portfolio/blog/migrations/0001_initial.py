# Generated by Django 3.2.12 on 2022-02-20 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('episode', models.IntegerField()),
                ('date_pub', models.DateField(default=datetime.datetime(2022, 2, 20, 22, 24, 27, 8365))),
                ('post', models.TextField()),
            ],
        ),
    ]
