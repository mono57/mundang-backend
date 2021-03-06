# Generated by Django 4.0.3 on 2022-07-06 21:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(max_length=120, verbose_name='Resumé'),
        ),
    ]
