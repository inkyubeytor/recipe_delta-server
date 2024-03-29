class Recipe:
    def __init__(self, details: dict):
        self.name = details.get('name')
        self.ingredients = details.get('ingredients')
        self.time = details.get('time')
        self.image = details.get('image')
        self.desc = details.get('desc')
        self.rating = details.get('rating')
        self.url = details.get('url')
        self.source = details.get('source')

    def to_dict(self):
        return {
                'name' : self.name,
                'ingredients' : self.ingredients,
                'time' : self.time,
                'image' : self.image,
                'desc' : self.desc,
                'rating' : self.rating,
                'url' : self.url,
                'source' : self.source
                }
