from django.db import models



class Index(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    images = models.ImageField(upload_to = 'ins_images', blank = True, null = True, verbose_name = 'Изображение в картах')
    text = models.TextField(verbose_name='Текст в картах')

    class Meta:
        verbose_name = 'информацию в картах'
        verbose_name_plural = 'Информация в картах'


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
        verbose_name = 'текст о нас'
        verbose_name_plural = 'Тексты о нас'

    def __str__(self):
        return self.name



class Carousel(models.Model):
    images = models.ImageField(upload_to = 'ins_images', blank = True, null = True, verbose_name = 'Изображение в карусели:')
    text = models.TextField(verbose_name='Текст в карусели:')

    class Meta:
        verbose_name = 'анонс в слайдере'
        verbose_name_plural = 'Анонсы в слайдере'


    def __str__(self):
        return self.text