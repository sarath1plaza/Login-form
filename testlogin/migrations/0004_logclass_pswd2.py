# Generated by Django 2.2.7 on 2019-11-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testlogin', '0003_auto_20191109_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='logclass',
            name='pswd2',
            field=models.TextField(default=45, max_length=20),
            preserve_default=False,
        ),
    ]
