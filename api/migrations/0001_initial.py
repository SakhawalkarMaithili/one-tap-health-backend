# Generated by Django 3.2.5 on 2021-11-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remind_date', models.DateTimeField()),
            ],
            options={
                'ordering': ['-remind_date'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.TextField()),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
