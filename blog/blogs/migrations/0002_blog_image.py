# Generated by Django 3.1.6 on 2021-02-19 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='static/img/', upload_to='static/img/'),
            preserve_default=False,
        ),
    ]
