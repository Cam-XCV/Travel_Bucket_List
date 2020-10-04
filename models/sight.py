class Sight:

    def __init__(self, name, country, city, id = None):
        self.name = name
        self.country = country
        self.city = city
        self.visited = False
        self.id = id

    def mark_visited(self):
        if self.visited == False:
            self.visited == True
        elif self.visited == True:
            self.visited == False

          