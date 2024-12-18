# Generated by Django 5.1.3 on 2024-11-24 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_remove_feedback_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='ootd_photo',
            field=models.ImageField(blank=True, null=True, upload_to='feedback_photos/'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='temperature_level',
            field=models.IntegerField(blank=True, choices=[(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3'), (4, 'Level 4'), (5, 'Level 5')], null=True),
        ),
        migrations.DeleteModel(
            name='OOTD',
        ),
    ]
