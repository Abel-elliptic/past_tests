# Generated by Django 2.2.1 on 2019-05-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_university_subject_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Univ_detail',
        ),
        migrations.DeleteModel(
            name='University',
        ),
        migrations.RemoveField(
            model_name='category',
            name='child',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.AddField(
            model_name='category',
            name='department',
            field=models.CharField(default=1, max_length=31, verbose_name='学部名'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=31, verbose_name='大学名'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='school_year',
            field=models.IntegerField(default=3, verbose_name='学年'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='subject_name',
            field=models.CharField(default=1, max_length=31, verbose_name='学科名'),
            preserve_default=False,
        ),
    ]