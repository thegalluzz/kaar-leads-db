# Generated by Django 3.2.9 on 2022-04-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_leadads_leadmsn_leadwebsite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadads',
            name='created_time',
            field=models.CharField(max_length=250),
        ),
    ]
