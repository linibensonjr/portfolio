# Generated by Django 3.2.12 on 2022-02-20 21:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_date_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_pub',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
