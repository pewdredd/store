# Generated by Django 4.2.7 on 2023-12-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_emailverification'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified_email',
            field=models.BooleanField(default=False),
        ),
    ]