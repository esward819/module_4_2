# Generated by Django 3.2.7 on 2021-10-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.TextField()),
                ('artist_name', models.TextField()),
                ('genre_name', models.TextField()),
                ('album', models.TextField()),
            ],
        ),
    ]