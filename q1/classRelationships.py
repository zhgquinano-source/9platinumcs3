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

    def __init__(
        self,
        artist_name,
        no_of_members,
        origin,
        is_active,
        total_albums_released,
    ):
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
    total_albums_released="2 Studio Album",
)

song_1 = Song("Captivated", "Alternative Rock/Funk-Pop", 220, "Single")
song_2 = Song("Dulo Ng Hangganan", "Alternative Rock", 328, "ClapClapClap!")
song_3 = Song("Hey Barbara", "Retro Rock", 230, "Single")

# --- BEFORE RELATIONSHIP ---
print("--- BEFORE RELATIONSHIP ---")
print(f"Artist / Band: {band_artist.artist_name} ({band_artist.origin})")
print(f"Total Albums Released: {band_artist.total_albums_released}")
print(f"Associated Songs Count: {len(band_artist.songs)} (No association formed yet)")
print("\nIndependent Objects Created:")
print(f"- Song: {song_1.song_name} | Genre: {song_1.genre} | Duration: {song_1.duration} | Album: {song_1.album}")
print(f"- Song: {song_2.song_name} | Genre: {song_2.genre} | Duration: {song_2.duration} | Album: {song_2.album}")
print(f"- Song: {song_3.song_name} | Genre: {song_3.genre} | Duration: {song_3.duration} | Album: {song_3.album}")

# --- BUILDING RELATIONSHIP ---
print("\n--- BUILDING RELATIONSHIP ---")
print("[Assignment] Linking Song objects to the Artist's 'songs' collection...")
print("- Executing: band_artist.add_song(song_1)")
band_artist.add_song(song_1)
print("- Executing: band_artist.add_song(song_2)")
band_artist.add_song(song_2)
print("- Executing: band_artist.add_song(song_3)")
band_artist.app_song(song_3) if hasattr(band_artist, 'app_song') else band_artist.add_song(song_3)

# --- AFTER RELATIONSHIP ---
print("\n--- AFTER RELATIONSHIP ---")
print(f"Artist / Band: {band_artist.artist_name} ({band_artist.origin})")
print(f"Total Albums Released: {band_artist.total_albums_released}")
print("-" * 65)
print("Related object(s) accessed through the relationship:")
for song in band_artist.songs:
    print(f" > Song: {song.song_name} | Genre: {song.genre} | Duration: {song.duration} | Album: {song.album}")  # Fixed: song_.duration -> song.duration
print("-" * 65)

band_artist.add_member("Zild Benitez")
band_artist.release_album("ClapClapClap!")
