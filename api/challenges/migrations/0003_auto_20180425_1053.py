# Generated by Django 2.0.4 on 2018-04-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_auto_20180425_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='tags',
            field=models.ManyToManyField(blank=None, to='api.Tag'),
        ),
    ]
