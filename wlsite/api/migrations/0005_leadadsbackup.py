# Generated by Django 3.2.9 on 2022-04-13 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_leadads_created_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadAdsBackup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leadads_backup', models.TextField(max_length=2000)),
            ],
        ),
    ]
