# Generated by Django 2.2.1 on 2019-05-14 10:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20190514_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Univ_detail',
            fields=[
                ('department_name', models.CharField(max_length=31, verbose_name='学部名')),
                ('subject_name', models.CharField(max_length=31, verbose_name='学科名')),
                ('school_year', models.IntegerField(verbose_name='学年')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, verbose_name='大学名')),
                ('department', models.CharField(max_length=31, verbose_name='学部名')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='department',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='school_year',
        ),
        migrations.RemoveField(
            model_name='category',
            name='subject_name',
        ),
        migrations.AddField(
            model_name='category',
            name='child',
            field=models.CharField(default=1, max_length=31, verbose_name='子'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.CharField(blank=True, max_length=31, verbose_name='親'),
        ),
    ]
