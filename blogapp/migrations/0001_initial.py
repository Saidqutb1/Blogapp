# Generated by Django 5.0.4 on 2024-05-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
