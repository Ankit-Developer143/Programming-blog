# Generated by Django 3.1.1 on 2020-09-18 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.CharField(default='', max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]