# Generated by Django 3.2.9 on 2022-04-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20220413_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogLead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateTimeField(auto_now_add=True)),
                ('exeption_origin', models.CharField(max_length=250)),
                ('log_exeption', models.TextField(max_length=2000)),
            ],
        ),
    ]