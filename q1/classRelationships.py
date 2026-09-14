class Song:
    """Represents an individual song (the 'Many' side)."""
    
    def __init__(self, song_name, genre, duration, album):
        self.song_name = song_name
        self.genre = genre
        self.__duration = duration
        self.album = album

    def play_song(self):
        """UML Method: Plays the song."""
        print(f"Playing song: '{self.song_name}' ({self.genre})")

    def stop_song(self):
        """UML Method: Stops the song."""
        print(f"Stopped song: '{self.song_name}'")

    def set_volume(self, volume):
        """UML Method: Sets the playback volume."""
        print(f"Volume set to {volume}% for '{self.song_name}'")

class Artist:
    """Represents a music artist or band (the 'One' side holding multiple songs)."""
    
    def __init__(self, artist_name, no_of_members, origin, is_active, total_albums_released):
        self.artist_name = artist_name
        self.no_of_members = no_of_members
        self.origin = origin
        self.is_active = is_active
        self.total_albums_released = total_albums_released
        
        self.songs = []

    def add_song(self, song_reference):
        """Method to append an actual Song object into the artist's collection."""
        self.songs.append(song_reference)

    def add_member(self, member_name):
        """UML Method: Adds a member to the band/artist."""
        print(f"[Artist Method] Added member '{member_name}' to {self.artist_name}.")

    def release_album(self, album_name):
        """UML Method: Releases an album."""
        print(f"[Artist Method] {self.artist_name} released a new album: {album_name}")

    def create_song(self, song_name):
        """UML Method: Creates a song."""
        print(f"[Artist Method] {self.artist_name} created a new song: {song_name}")

band_artist = Artist(
    artist_name="IV of Spades", 
    no_of_members=4, 
    origin="Mandaluyong, Philippines", 
    is_active=True, 
    total_albums_released="2 Studio Album"
)

song_1 = Song("Captivated", "Alternative Rock/Funk-Pop", 220, "Single")
song_2 = Song("Dulo Ng Hangganan", "Alternative Rock", 328, "ClapClapClap!")
song_3 = Song("Hey Barbara", "Retro Rock", 230, "Single")

band_artist.add_song(song_1)
band_artist.add_song(song_2)
band_artist.add_song(song_3)

print(f"Artist / Band: {band_artist.artist_name} ({band_artist.origin})")
print(f"Total Albums Released: {band_artist.total_albums_released}")
print("-" * 65)
print("Associated Songs (Accessed via object references through a loop):")

for song in band_artist.songs:
    print(f" > Song: {song.song_name} | Genre: {song.genre} | Album: {song.album}")

print("-" * 65)

band_artist.add_member("Zild Benitez")
band_artist.release_album("ClapClapClap!")
