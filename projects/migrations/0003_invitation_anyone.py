# Generated by Django 3.2 on 2021-05-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210505_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='anyone',
            field=models.BooleanField(default=False),
        ),
    ]
