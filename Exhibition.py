class Exhibition:
    def __init__(self, start_date, end_date, location):
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        
    def get_duration(self):
        return f"Start Date: {self.start_date}, End Date: {self.end_date}"

    def get_location(self):
        return f"Location: {self.location}"
