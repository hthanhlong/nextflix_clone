# Generated by Django 5.0.2 on 2024-03-03 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role',
            new_name='role_id',
        ),
    ]