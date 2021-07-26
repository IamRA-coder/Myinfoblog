# Generated by Django 3.2.3 on 2021-07-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpostapp', '0012_auto_20210726_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
