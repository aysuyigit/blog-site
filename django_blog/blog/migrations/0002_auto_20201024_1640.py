# Generated by Django 2.2.14 on 2020-10-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['id'], 'verbose_name_plural': 'Gönderiler'},
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
