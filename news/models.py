from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


class News(models.Model):

    class Meta:
        verbose_name = 'новость '
        verbose_name_plural = 'новости'

    name = models.CharField(max_length=100, verbose_name='заголовок')
    image = models.ImageField(verbose_name='изображение', upload_to='news_images/', null=True)
    description = models.CharField(max_length=250, verbose_name='краткое описание')
    content = models.TextField(verbose_name='контент')
    date = models.DateTimeField(verbose_name='дата добавление', auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='публичность')
    category = models.ForeignKey('news.Category', on_delete=models.PROTECT, related_name='news', verbose_name='категория')
    tags = models.ManyToManyField('news.Tag', related_name='news', verbose_name='теги', blank=True)

    def __str__(self):
        return f'{self.name} - {self.date}'


class Category(models.Model):

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField(verbose_name='название', max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class AdditionalNewsInfo(models.Model):

    class Meta:
        verbose_name = 'допалнительная информация новости'
        verbose_name_plural = 'допалнительная информация новостей'

    news = models.OneToOneField('news.News', on_delete=models.CASCADE, related_name='info', verbose_name='новость')
    link = models.URLField(verbose_name='ссылка')
    # email = models.CharField(validators=[RegexValidator(r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', message='Введите корректную эл. почту.')]) # models.EmailField()
    # json_field = models.JSONField()
    email = models.EmailField(verbose_name='эл. почта')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='оценка')

    def __str__(self):
        return f'{self.news}'


class Tag(models.Model):

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    name = models.CharField(verbose_name='название', max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'

# Create your models here.
