# Generated by Django 4.0.4 on 2022-05-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
