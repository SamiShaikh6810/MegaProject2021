# Generated by Django 3.1.12 on 2021-06-20 20:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('blog_slug', models.SlugField(max_length=300, unique=True)),
                ('category', models.CharField(default='', max_length=50)),
                ('sub_category', models.CharField(default='', max_length=50)),
                ('discription', models.CharField(max_length=700)),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField(default=datetime.datetime(2021, 6, 20, 20, 15, 26, 921698, tzinfo=utc))),
                ('cover_image', models.ImageField(default='', upload_to='blog/cover_images')),
                ('autor', models.CharField(max_length=100)),
            ],
        ),
    ]
