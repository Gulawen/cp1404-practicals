
class Movie:
    def __init__(self, title="", year=0, category="", is_watched=False):
        self.category = category
        self.title = title
        self.year = year
        self.is_watched = is_watched

    def __str__(self):
        if self.is_watched:
            watched = "w"
        else:
            watched = "u"
        return "{0} {1} {2} {3}".format(self.title, self.year, self.category, watched)

    def watched(self):
        self.is_watched = True

    def unwatched(self):
        self.is_watched = False
