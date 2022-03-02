class User:
    def __init__(self, json):
        self.name = json['display_name']
        self.url = json['external_urls']['spotify']
