# Generated by Django 3.2.4 on 2021-06-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpostapp', '0005_comment_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('messages', models.TextField()),
            ],
        ),
    ]
