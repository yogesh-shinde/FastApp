# Generated by Django 2.2.7 on 2020-11-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
