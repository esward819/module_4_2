from django.test import TestCase
from app import models
class TestSong(TestCase):
    def test_can_create_song(self):
        songs = models.create_song(
            "Break Stuff",
            "Limp Biskit",
            "Nu-Metal",
            "Significant Other",
        )
        self.assertEqual(songs.song_name, "Break Stuff")
        self.assertEqual(songs.artist_name, "Limp Biskit")
        self.assertEqual(songs.genre_name, "Nu-Metal")
        self.assertEqual(songs.album, "Significant Other")
    
    
    def test_can_view_all_songs(self):
        songs_data = [
            {
                "Song": "Break Stuff",
                "Artist": "Limp Biskit",
                "Genre": "Nu-Metal",
                "Album": "Significant Other",
            },
            {
                "Song": "Better Off (Dying)",
                "Artist": "Lil Peep",
                "Genre": "Rap",
                "Album": "Come Over When You're Sober Pt. 1",
            },
            {
                "Song": "Japan",
                "Artist": "Yot Club",
                "Genre": "Indie-Punk",
                "Album": "Japan",
            },
        ]
        for song_data in songs_data:
            models.create_song(
                song_data["Song"],
                song_data["Artist"],
                song_data["Genre"],
                song_data["Album"],
            )
        songs = models.all_songs()
        self.assertEqual(len(songs), len(songs_data))
        songs_data = sorted(songs_data, key=lambda c: c["Song"])
        songs = sorted(songs, key=lambda c: c.song_name)
        for data, songs in zip(songs_data, songs):
            self.assertEqual(data["Song"], songs.song_name)
            self.assertEqual(data["Artist"], songs.artist_name)
            self.assertEqual(data["Genre"], songs.genre_name)
            self.assertEqual(data["Album"], songs.album)

    
    def test_can_view_song_by_name(self):
        songs_data = [
            {
                "Song": "Break Stuff",
                "Artist": "Limp Biskit",
                "Genre": "Nu-Metal",
                "Album": "Significant Other",
            },
            {
                "Song": "Better Off (Dying)",
                "Artist": "Lil Peep",
                "Genre": "Rap",
                "Album": "Come Over When You're Sober Pt. 1",
            },
            {
                "Song": "Japan",
                "Artist": "Yot Club",
                "Genre": "Indie-Punk",
                "Album": "Japan",
            },
        ]

        for song_data in songs_data:
            models.create_song(
                song_data["Song"],
                song_data["Artist"],
                song_data["Genre"],
                song_data["Album"],
            )

        song = models.find_song_by_name("Break Stuff")

        self.assertEqual(song.song_name, "Break Stuff")




    def test_can_update_songs_artist(self):
        songs_data = [
            {
                "Song": "Break Stuff",
                "Artist": "Limp Biskit",
                "Genre": "Nu-Metal",
                "Album": "Significant Other",
            },
            {
                "Song": "Better Off (Dying)",
                "Artist": "Lil Peep",
                "Genre": "Rap",
                "Album": "Come Over When You're Sober Pt. 1",
            },
            {
                "Song": "Japan",
                "Artist": "Yot Club",
                "Genre": "Indie Punk",
                "Album": "Japan",
            },
        ]
        for song_data in songs_data:
            models.create_song(
                song_data["Song"],
                song_data["Artist"],
                song_data["Genre"],
                song_data["Album"],
            )
        models.update(1, "Baby Keem")
        self.assertEqual(
            models.find_song_by_name("Break Stuff").artist_name, "Baby Keem"
        )


    def test_can_delete(self):
        songs_data = [
            {
                "Song": "Break Stuff",
                "Artist": "Limp Biskit",
                "Genre": "Nu-Metal",
                "Album": "Significant Other",
            },
            {
                "Song": "Better Off (Dying)",
                "Artist": "Lil Peep",
                "Genre": "Rap",
                "Album": "Come Over When You're Sober Pt. 1",
            },
            {
                "Song": "Japan",
                "Artist": "Yot Club",
                "Genre": "Indie Punk",
                "Album": "Japan",
            },
        ]
        for song_data in songs_data:
            models.create_song(
                song_data["Song"],
                song_data["Artist"],
                song_data["Genre"],
                song_data["Album"],
            )
        models.delete(2)
        self.assertEqual(len(models.all_songs()), 2)