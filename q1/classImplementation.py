class Songs:
    def __init__(self, songName, genre, duration, album, artist):
        self.songName = songName
        self.genre = genre
        self.__duration = duration
        self.album = album
        self.artist = artist

    def change_duration(self, new_duration):
        if new_duration > 0:
            self.__duration = new_duration
        else:
            print("Duration must be greater than zero.")

    def get_duration(self):
        return self.__duration

    def get_song_info(self):
        return f"{self.songName} - {self.artist} ({self.genre}), {self.__duration} seconds"


object1 = Songs(
    "Why'd You Only Call Me When You're High?",
    "Alternative Rock",
    161,
    "AM",
    "Arctic Monkeys"
)

object2 = Songs(
    "Dulo Ng Hangganan",
    "Alternative Rock",
    328,
    "CLAPCLAPCLAP!",
    "IV of Spades"
)


print("Before:")
print("Object 1:", object1.get_song_info())
print("Object 2:", object2.get_song_info())

print("\nChanging Object 1 duration...")
object1.change_duration(300)

print("After:")
print("Object 1:", object1.get_song_info())
print("Object 2:", object2.get_song_info())
