# Generated by Django 4.2.4 on 2023-09-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='src_news',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]
