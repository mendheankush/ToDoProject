# Generated by Django 4.0.4 on 2022-11-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
