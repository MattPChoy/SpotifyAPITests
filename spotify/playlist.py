from .spotify import Spotify # Class import

class Playlist:
    def __init__(self, playlist_id, spotify):
        self.spotify = spotify
        self.playlist_id = playlist_id

        self.__get_json_data__()
        self.__parse_json_data__()

    def __get_json_data__(self):
        assert self.spotify is not None, "Spotify object not defined (is None)"
        assert self.playlist_id is not None, "Playlist ID is None"

        self.json = self.spotify.sp.user_playlist(
            user="",
            playlist_id=self.playlist_id
        )

    def __parse_json_data__(self):
        self.collaborative = self.json['collaborative']
        self.description = self.json['description']
        self.num_followers = self.json['followers']['total']
        self.name = self.json['name']
        pass
