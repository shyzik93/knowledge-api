# Generated by Django 3.2.10 on 2023-01-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name': 'Заметка', 'verbose_name_plural': 'Заметки'},
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='note',
            name='search_content',
            field=models.TextField(verbose_name='Текст для поиска'),
        ),
        migrations.AlterField(
            model_name='note',
            name='search_title',
            field=models.TextField(db_index=True, max_length=255, verbose_name='Заголовок для поиска'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Заголовок'),
        ),
    ]