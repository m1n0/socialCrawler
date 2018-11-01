class Person:
    def __init__(self, link, id, picture):
        self.link = link
        self.id = id
        self.picture = picture

    def __str__(self):
        return "ID: {}, link: {}, picture: {}\n".format(
            self.id,
            self.link,
            self.picture
        )
