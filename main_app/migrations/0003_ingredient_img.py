# Generated by Django 3.2.4 on 2021-07-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_ramen_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='img',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]