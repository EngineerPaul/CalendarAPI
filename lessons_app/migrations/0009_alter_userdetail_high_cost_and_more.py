# Generated by Django 4.0.3 on 2022-04-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons_app', '0008_userdetail_alias_userdetail_discord_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='high_cost',
            field=models.IntegerField(blank=True, default=1300, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='usual_cost',
            field=models.IntegerField(blank=True, default=1000, null=True),
        ),
    ]
