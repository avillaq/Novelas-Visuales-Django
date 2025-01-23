# Generated by Django 5.0.2 on 2025-01-20 05:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VNDisplay', '0011_alter_postdetail_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_url',
            new_name='cover_url',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='publicaction_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='synopsis',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='id_post',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='screenshot_urls',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='specifications',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='update_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PostDetail',
        ),
    ]
