# Generated by Django 5.0.2 on 2024-03-04 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_user_is_authenticated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp_code',
            field=models.CharField(blank=True, default='123456', max_length=6, null=True),
        ),
    ]
