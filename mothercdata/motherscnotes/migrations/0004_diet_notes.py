# Generated by Django 2.0.6 on 2018-08-05 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motherscnotes', '0003_auto_20180707_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]