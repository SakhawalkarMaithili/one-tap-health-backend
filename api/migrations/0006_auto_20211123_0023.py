# Generated by Django 3.2.5 on 2021-11-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_reminder_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='doctor',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='emergency',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
