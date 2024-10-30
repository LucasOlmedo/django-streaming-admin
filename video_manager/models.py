from django.db import models
from django.utils import timezone
from django.forms import ValidationError

class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    thumbnail = models.ImageField(upload_to='thumbnails/', verbose_name='Thumbnail', null=True, blank=True)
    video_file = models.FileField(upload_to='video_files/', verbose_name='Arquivo de vídeo', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug')
    published_at = models.DateTimeField(verbose_name='Data de publicação', editable=False, null=True, blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Publicado?')
    likes = models.IntegerField(default=0, null=True, blank=True, verbose_name='Curtidas', editable=False)
    views = models.IntegerField(default=0, null=True, blank=True, verbose_name='Visualizações', editable=False)
    tags = models.ManyToManyField('Tag', verbose_name='Tags')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Autor', default=1, editable=False)

    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()

        super(Video, self).save(*args, **kwargs)

    def clean(self):
        if self.is_published and not self.thumbnail and not self.video_file:
            raise ValidationError('Vídeos publicados devem ter uma thumbnail e um arquivo de vídeo.')

        return super().clean()

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
