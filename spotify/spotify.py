import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secrets import Secrets

class Spotify:
    def __init__(self, secrets_fp):
        """
        Creates a new wrapper object for the Spotipy API which is a wrapper
        for the spotify web API
        @param secrets_fp: Filepath to the secrets file containing the
                            client_id and client_secret strings.
        """
        spotify_secrets = Secrets(secrets_fp)
        client_id, client_secret = spotify_secrets.get_secrets()[:2]

        self.sp = spotipy.Spotify(
                auth_manager=SpotifyOAuth(
                    client_id=client_id,
                    client_secret=client_secret,
                    redirect_uri="http://localhost:8080",
                    scope="user-library-read"
                )
            )

    def __get_sp__(self):
        """
        Return the spotipy object for debugging
        """
        return self.sp

    def get_playlist_ids(self,username,playlist_id):
        r = self.sp.user_playlist_tracks(username,playlist_id,limit=10,offset=1)

        tracks = r['tracks']['items']
        num_tracks = 0

        for t in tracks:
            song_name = t['track']['name']
            artists = []
            for a in t['track']['artists']:
                artists.append(a['name'])

            print(f"{song_name} - {artists}")
            num_tracks += 1
        print(f"{num_tracks} tracks found")

    def get_song_data(song_json):
        return None

    def get_playlist_obj(self, playlist_url):
        return None
