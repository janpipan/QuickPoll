# Generated by Django 3.2.9 on 2021-12-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20211120_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
