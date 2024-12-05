# Generated by Django 5.1.3 on 2024-11-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('preacher', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='sermon_thumbnails/')),
                ('written_sermon_url', models.URLField(blank=True, null=True)),
                ('video_url', models.URLField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
