# Generated by Django 2.2.1 on 2019-05-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190513_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.CharField(blank=True, max_length=31, null=True, verbose_name='親'),
        ),
    ]
