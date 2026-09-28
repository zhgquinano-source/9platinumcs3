class Artist:
    def __init__(self, artist_name: str, origin: str, no_of_members: int):
        self.artist_name = artist_name
        self.origin = origin
        self.no_of_members = no_of_members

    def create_song(self, song_name: str, genre: str, duration: int):
        return Song(song_name, genre, duration, self)


class Song:
    def __init__(self, song_name: str, genre: str, duration: int, artist: Artist):
        self.song_name = song_name
        self.genre = genre
        self.duration = duration
        self.artist = artist

    def play_song(self):
        print("=== SONG TEST ===")
        print(f"Song Name: {self.song_name}")
        print(f"Genre: {self.genre}")
        print(f"Duration: {self.duration} seconds")
        print(f"Artist: {self.artist.artist_name}")


class CoverSong(Song):
    def __init__(self, song_name: str, genre: str, duration: int, artist: Artist, cover_artist: str, tempo_change: int):
        super().__init__(song_name, genre, duration, artist)
        self.cover_artist = cover_artist
        self.tempo_change = tempo_change

    def play_cover(self):
        print("=== COVER SONG TEST ===")
        print(f"Song Name: {self.song_name}")
        print(f"Original Artist: {self.artist.artist_name}")
        print(f"Cover Artist: {self.cover_artist}")
        print(f"Duration: {self.duration} seconds")
        print(f"Tempo Change: {self.tempo_change}")


class Album:
    def __init__(self, album_title: str):
        self.album_title = album_title
        self.tracklist = []

    def add_song(self, song: Song):
        self.tracklist.append(song)

    def display_album(self):
        print(f"Album contains {len(self.tracklist)} tracks.")
        for idx, song in enumerate(self.tracklist, 1):
            if isinstance(song, CoverSong):
                print(f"Track {idx}: {song.song_name} (Cover by {song.cover_artist})")
            else:
                print(f"Track {idx}: {song.song_name} (by {song.artist.artist_name})")


if __name__ == "__main__":
    arctic_monkeys = Artist("Arctic Monkeys", "Sheffield, England", 4)

    song1 = arctic_monkeys.create_song("Do I Wanna Know?", "Indie Rock", 266)

    cover1 = CoverSong(
        song_name="Do I Wanna Know?",
        genre="Indie Rock",
        duration=266,
        artist=arctic_monkeys,
        cover_artist="Hozier",
        tempo_change=-17
    )

    album1 = Album("AM")
    album1.add_song(song1)
    album1.add_song(cover1)

    print("=== INHERITANCE TEST ===")
    print(f"Child class: {cover1.__class__.__name__}")
    print(f"Inherited duration: {cover1.duration}")
    print(f"Inherited genre: {cover1.genre}")
    print(f"Additional attribute - tempo change: {cover1.tempo_change}")
    print()

    print("=== AGGREGATION TEST ===")
    album1.display_album()
    print()

    song1.play_song()
    print()

    cover1.play_cover()