from django.db import models

# Create your models here.

class Quote(models.Model):
    kanye_quote = models.TextField('Цитата Kanye', unique=True, null=True)
    letters_amount = models.IntegerField('Количество букв в цитате', null=True)
    vowels = models.IntegerField('Количество гласных', null=True)
    consonants = models.IntegerField('Количество согласных', null=True)
    # repeated_letters = models.TextField('Количество одинаковых букв', null=True)
    # average_len = models.IntegerField('Средняя длинна слов', null=True)
    # longest_words = models.TextField('Три длиннейших слова', null=True)

    def __str__(self):
        return (str(self.kanye_quote))

    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'