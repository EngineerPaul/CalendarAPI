# Generated by Django 4.0.3 on 2022-04-08 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons_app', '0006_rename_telegram_acc_userdetail_telegram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='theme',
        ),
    ]
