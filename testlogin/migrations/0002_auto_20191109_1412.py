# Generated by Django 2.2.7 on 2019-11-09 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testlogin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='pswd',
            new_name='pswd1',
        ),
    ]
