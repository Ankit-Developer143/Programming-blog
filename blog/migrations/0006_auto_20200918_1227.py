# Generated by Django 3.1.1 on 2020-09-18 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200918_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.TextField(default='', max_length=2000),
        ),
    ]