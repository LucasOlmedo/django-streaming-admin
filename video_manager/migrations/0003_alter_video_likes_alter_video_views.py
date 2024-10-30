# Generated by Django 5.1.2 on 2024-10-30 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0002_alter_video_likes_alter_video_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]