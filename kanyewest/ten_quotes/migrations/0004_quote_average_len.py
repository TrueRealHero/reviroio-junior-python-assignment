# Generated by Django 4.0.3 on 2022-03-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ten_quotes', '0003_quote_repeated_letters'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='average_len',
            field=models.IntegerField(null=True, verbose_name='Средняя длинна слов'),
        ),
    ]
