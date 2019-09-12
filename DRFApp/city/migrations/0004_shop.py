# Generated by Django 2.2.5 on 2019-09-04 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('city', '0003_auto_20190904_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256)),
                ('building', models.CharField(max_length=64)),
                ('work_from', models.TimeField(blank=True)),
                ('work_to', models.TimeField(blank=True)),
                ('city_id',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='city.City')),
                ('street_id',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='city.Street')),
            ],
        ),
    ]
