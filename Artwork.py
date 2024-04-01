class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.location = location
        
    def get_info(self):
        return f"Title: {self.title}, Artist: {self.artist}, Location: {self.location}"
