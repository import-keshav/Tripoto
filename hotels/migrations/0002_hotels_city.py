# Generated by Django 2.2.3 on 2019-07-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='city',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
