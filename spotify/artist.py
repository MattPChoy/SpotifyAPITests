class Artist:
    def __init__(self, json):
        """
        Create artist class using the JSON data collected from the spotify API.
        """
        self.json = json # The data used to populate class data.
        self.link = json['external_urls']['spotify']
        self.id = json['id']
        self.name = json['name']
        self.uri = json['uri']

    def __str__(self):
        return f"{self.name} ({self.id})"
