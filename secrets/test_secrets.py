from secrets import Secrets

sec = Secrets("spotify_tokens.txt")
secret_contents = sec.get_secrets()
