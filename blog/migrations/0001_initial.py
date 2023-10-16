# Generated by Django 4.2.6 on 2023-10-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_image', models.ImageField(upload_to='blog_images/')),
                ('event_text', models.CharField(max_length=300)),
            ],
        ),
    ]