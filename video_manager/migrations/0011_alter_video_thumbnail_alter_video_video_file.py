# Generated by Django 5.1.2 on 2024-10-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0010_alter_video_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='media/thumbnails/', verbose_name='Thumbnail'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(null=True, upload_to='media/video_files/', verbose_name='Arquivo de vídeo'),
        ),
    ]
