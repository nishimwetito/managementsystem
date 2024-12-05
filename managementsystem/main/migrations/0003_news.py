# Generated by Django 5.1.3 on 2024-11-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_galleryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='news/')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]