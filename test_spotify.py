import os
from spotify import Spotify, Playlist

spotify = Spotify("secrets/secret_tokens/spotify_tokens.txt")
EVERYTHING_PLAYLIST_ID = "7ftFSJSeTn8chfhgryUSq0"
CHILL_WORSHIP_PLAYLIST_ID = "58uCUH3N5BvjuYSZud5LiK"
# DEFAULT_PLAYLIST_7_PLAYLIST_ID = "7ftFSJSeTn8chfhgryUSq0"
# ESABEL = "4rfioefflXDlvq5Lc0HhRm"
# spotify.get_playlist_ids("matthewpchoy", ESABEL)

playlist = Playlist(playlist_id=CHILL_WORSHIP_PLAYLIST_ID, spotify=spotify)
