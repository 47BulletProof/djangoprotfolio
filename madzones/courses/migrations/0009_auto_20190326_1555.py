# Generated by Django 2.1.7 on 2019-03-26 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20190326_1550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'parent'},
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('parent', 'slug')},
        ),
    ]
