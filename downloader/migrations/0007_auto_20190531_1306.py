# Generated by Django 2.2.1 on 2019-05-31 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0006_auto_20190531_1302'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='History',
            new_name='Request',
        ),
    ]
