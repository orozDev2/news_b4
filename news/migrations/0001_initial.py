# Generated by Django 5.0.2 on 2024-02-19 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='заголовок')),
                ('description', models.CharField(max_length=250, verbose_name='краткое описание')),
                ('content', models.TextField(verbose_name='контент')),
                ('date', models.DateTimeField(verbose_name='дата добавление')),
                ('is_published', models.BooleanField(default=True, verbose_name='публичность')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
            },
        ),
    ]
