from .artist import Artist

class Song():
    def __init__(self, json):
        self.json = json
        self.added_at = self.json['added_at'] # TODO: Convert this to date obj?
        # self.added_by = User(json['added_by'])
        self.artists = []
        self.__get_artists__()

        # Track details
        self.duration_ms = self.json['track']['duration_ms']
        self.explicit = self.json['track']['explicit']
        self.name = self.json['track']['name']
        self.id = self.json['track']['id']

    def __get_artists__(self):
        # JSON list of all artists attributed to a song
        self.json_artists = self.json['track']['artists']
        for json_a in self.json_artists:
            self.artists.append(Artist(json_a))

    def __str__(self):
        artist_names = ", ".join([str(s.name) for s in self.artists])
        return f"{self.name} by {artist_names}"
