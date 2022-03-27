# Generated by Django 4.0.3 on 2022-03-27 16:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(default='Consultation', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('salary', models.IntegerField(validators=[django.core.validators.MinValueValidator(700), django.core.validators.MaxValueValidator(1500)])),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
                'ordering': ('date', 'time'),
            },
        ),
    ]
