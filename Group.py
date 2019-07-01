class group:
    def __init__(self, isLocal, patentname, airport_radius, lat, lng):
        self.isLocal = isLocal
        self.patentname = patentname
        self.airport_radius = airport_radius
        self.lat = lat
        self.lng = lng
        
    def get_name(self):
        return self.patentname
    
    def get_coordinates(self):
        return (self.lat, self.lng)
    
    def get_airport_radius(self):
        return self.airport_radius
        
    