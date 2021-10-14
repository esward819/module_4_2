from django.db import models

# Create your models here.
class Song(models.Model):
    song_name = models.TextField()
    artist_name = models.TextField()
    genre_name = models.TextField()
    album = models.TextField()

def create_song(name, artist, genre, album):
    songs = Song(song_name=name, artist_name=artist, genre_name=genre, album=album)
    songs.save()
    return songs

def all_songs():
    return Song.objects.all()

def find_song_by_name(name):
    try: 
        return Song.objects.get(song_name=name)
    except:
        return None


def update(id, new_artist):
    song=Song.objects.get(id=id)
    song.artist_name=new_artist
    song.save()

def delete(id):
    song = Song.objects.get(id=id)
    song.delete()

