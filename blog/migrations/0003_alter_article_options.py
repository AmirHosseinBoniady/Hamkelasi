# Generated by Django 4.1.1 on 2022-10-05 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_rename_published_article_publish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'مقالات'},
        ),
    ]