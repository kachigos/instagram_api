# Generated by Django 4.1.4 on 2022-12-26 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0002_rename_follower_follow_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follow',
            new_name='user',
        ),
    ]
