# Generated by Django 4.1.1 on 2022-10-05 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=20, verbose_name='عنوان'),
        ),
    ]