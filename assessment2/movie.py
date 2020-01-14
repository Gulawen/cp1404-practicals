class Movie:
    def __init__(self, title="", category="", year=0, movie_to_watch=""):
        """Determine items a movie would help"""
        self.category = category
        self.title = title
        self.year = year
        self.movie_to_watch = movie_to_watch

    def __str__(self):
        """Display an announcement when a movie is inputed"""
        if self.movie_to_watch == "w":
            movie_to_watch ="wathced"
            return ("You have already watched {}".format(self.title))

        else:
            movie_to_watch = "u"
            return ("{} from {} watched ".format(self.title, self.year))


    def mark_watched(self):
        """Mark the movie watched"""
        self.movie_to_watch = 'w'
        return self.movie_to_watch

