# Generated by Django 2.1.7 on 2019-03-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='explanation',
            field=models.TextField(default='', max_length=500),
        ),
    ]
