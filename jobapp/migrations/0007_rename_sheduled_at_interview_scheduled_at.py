# Generated by Django 5.2.3 on 2025-06-26 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_job_tags_interview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview',
            old_name='sheduled_at',
            new_name='scheduled_at',
        ),
    ]
