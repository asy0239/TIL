# Generated by Django 2.2.1 on 2019-06-18 01:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follow',
            field=models.ManyToManyField(related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]