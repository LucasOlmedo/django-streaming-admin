from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    thumbnail = models.ImageField(upload_to='thumbnails/', verbose_name='Thumbnail')
    video_file = models.FileField(upload_to='video_files/', verbose_name='Arquivo de vídeo')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug')
    published_date = models.DateTimeField(verbose_name='Data de publicação')
    is_published = models.BooleanField(default=False, verbose_name='Publicado?')
    likes = models.IntegerField(default=0, null=True, blank=True, verbose_name='Título')
    views = models.IntegerField(default=0, null=True, blank=True, verbose_name='Visualizações')
    
    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'

    def __str__(self):
        return self.title