# Generated by Django 5.0.2 on 2024-03-03 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_role_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role_id',
            new_name='role',
        ),
    ]