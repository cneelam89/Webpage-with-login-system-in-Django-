# Generated by Django 4.0.4 on 2022-05-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellNee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
