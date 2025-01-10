from django.db import models



class Index(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    images = models.ImageField(upload_to = 'ins_images', blank = True, null = True, verbose_name = 'Изображение')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'статью'
        verbose_name_plural = 'Статьи'


    def __str__(self):
        return self.name



class Accord(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Загаловок')
    text = models.TextField(verbose_name = 'Текст аккордиона')

    class Meta:
        verbose_name = 'текст аккордиона'
        verbose_name_plural = 'Тексты аккордиона'

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Загаловок')
    text = models.TextField(verbose_name = 'Текст')

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Тексты'

    def __str__(self):
        return self.name



class Carousel(models.Model):
    images = models.ImageField(upload_to = 'ins_images', blank = True, null = True, verbose_name = 'Изображение в карусели:')
    text = models.TextField(verbose_name='Текст в карусели:')

    class Meta:
        verbose_name = 'анонс'
        verbose_name_plural = 'Анонсы'


    def __str__(self):
        return self.text