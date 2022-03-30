# Generated by Django 4.0.3 on 2022-03-30 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='salary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='theme',
            field=models.CharField(blank=True, default='Consultation', max_length=100, null=True),
        ),
    ]
