import spotipy
from spotify.oauth2
from secrets import Secrets

spotify_secrets = Secrets("secrets/spotify_tokens.txt")
client_id, client_secret = spotify_secrets.get_secrets()[:2]

sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri="http://localhost:8080",
            scope="user-library-read"
        )
    )
