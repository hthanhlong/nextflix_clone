# Generated by Django 5.0.2 on 2024-03-03 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_role_user_role_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.CharField(default='hello', max_length=50),
        ),
    ]
