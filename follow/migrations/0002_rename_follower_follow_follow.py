# Generated by Django 4.1.4 on 2022-12-26 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follower',
            new_name='follow',
        ),
    ]
