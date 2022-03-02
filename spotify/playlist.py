from .spotify import Spotify # Class import
from .song import Song # Class import

class Playlist:
    def __init__(self, playlist_id, spotify):
        """
        Create an instance of the Playlist class that contains information
        parsed from the web API (which returns a JSON object.)

        @param playlist_id: Spotify's unique identifier for a playlist
        @param spotify: Spotify object, which contains auth information
        """
        self.spotify = spotify
        self.playlist_id = playlist_id

        self.__get_json_data__()
        self.__parse_json_data__()

    def __get_json_data__(self):
        """
        Obtain the JSON data from the web
        """
        assert self.spotify is not None, "Spotify object not defined (is None)"
        assert self.playlist_id is not None, "Playlist ID is None"

        self.json = self.spotify.sp.user_playlist(
            user="",
            playlist_id=self.playlist_id
        )

    def __parse_playlist_songs__(self):
        self.json_tracks = self.json['tracks']['items']
        for track in self.json_tracks:
            self.songs.append(Song(json=track))

    def __parse_json_data__(self):
        self.collaborative = self.json['collaborative']
        self.description = self.json['description']
        self.num_followers = self.json['followers']['total']
        self.name = self.json['name']
        # self.owner =
        self.songs = []
        self.__parse_playlist_songs__() # This updates self.songs

    def __str__(self):
        return f""
