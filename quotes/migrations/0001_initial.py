# Generated by Django 4.0.3 on 2022-06-23 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name': 'Étiquete Proverbes & Citations',
                'verbose_name_plural': 'Étiquetes Proverbes & Citations',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(verbose_name='Contenu')),
                ('author', models.CharField(max_length=150, verbose_name='Auteur')),
                ('author_slug', models.SlugField()),
                ('fetched', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(blank=True, related_name='quotes', to='quotes.quotetag', verbose_name='Étiquete')),
            ],
            options={
                'verbose_name': 'Proverb ou Citation',
                'verbose_name_plural': 'Proverbs ou Citations',
            },
        ),
    ]
