# Generated by Django 2.2.5 on 2019-09-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('city', '0005_auto_20190905_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='city_id',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='street_id',
        ),
        migrations.AddField(
            model_name='shop',
            name='city_name',
            field=models.CharField(db_index=True, default='', max_length=256),
        ),
        migrations.AddField(
            model_name='shop',
            name='street_name',
            field=models.CharField(db_index=True, default='', max_length=256),
        ),
    ]
