# Generated by Django 3.2.9 on 2022-04-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220413_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadbackup',
            name='leadbackup_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
