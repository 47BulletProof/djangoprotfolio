# Generated by Django 2.1.7 on 2019-03-26 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_subcourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcourse',
            name='Child',
        ),
        migrations.DeleteModel(
            name='SubCourse',
        ),
    ]
