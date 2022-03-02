class Song():
    def __init__(self, json):
        self.added_at = json['added_at']
        # self.added_by = User(json['added_by'])
        self.artists = []
        # self.artists = [] using json['track'][artists]

        # Track details
        self.duration_ms = json['track']['duration_ms']
        self.explicit = json['track']['explicit']
        self.name = json['track']['name']
        self.id = json['track']['id']

    def __str__(self):
        return f"{self.name} by {self.artists} ({self.id})"
