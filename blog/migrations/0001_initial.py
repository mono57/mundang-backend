# Generated by Django 4.0.3 on 2022-07-06 20:41

import blog.models
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nom')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Icone')),
                ('badge_color', models.CharField(blank=True, max_length=10, verbose_name='Couleur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nom')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Icone')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(blank=True, max_length=255)),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Titre')),
                ('cover_image', models.ImageField(upload_to=blog.models.post_images, verbose_name='Image de couverture')),
                ('summary', models.CharField(max_length=120, verbose_name='Resumé')),
                ('content', ckeditor.fields.RichTextField()),
                ('published_on', models.DateTimeField(blank=True, null=True)),
                ('published', models.BooleanField(default=True, verbose_name='Publié')),
                ('visibled', models.BooleanField(default=True, verbose_name='Visible')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.postcategory')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.posttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
