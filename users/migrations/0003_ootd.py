# Generated by Django 5.1.3 on 2024-11-24 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_conditionactivity'),
    ]

    operations = [
        migrations.CreateModel(
            name='OOTD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ootd_photos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ootds', to='users.userprofile')),
            ],
        ),
    ]
