# Generated by Django 2.2.1 on 2019-05-24 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='use',
            new_name='user',
        ),
    ]