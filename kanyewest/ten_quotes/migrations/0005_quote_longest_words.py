# Generated by Django 4.0.3 on 2022-03-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ten_quotes', '0004_quote_average_len'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='longest_words',
            field=models.TextField(null=True, verbose_name='Три длиннейших слова'),
        ),
    ]
