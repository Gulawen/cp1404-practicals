"""
Name:Jihui Wen
Date:2020/1/15
Brief Project Description:This programme allows you to manage your journey with GUI. When runing this programe, data file is loaded first and main graphic interface is genenrated. You can add new movie, mark movie watched or not and sort movies in desired order. After exiting the programe, any update of movies information will be stored into corresponding data file.
GitHub URL:https://github.com/JCUS-CP1404/assignment-02-Gulawen
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from movie import Movie
from moviecollection import MovieCollection

WELCOME = "Movies to watch 2.0 - by Jihui Wen"
SPINNER_DICT = dict({"Watched": "is_watched", "Title": "title", "Year": "year", "Category": "category"})
DATA_PATH = "movies.csv"
BUTTON_COLOR = [0.5, 0.5, 1, 1]


class MoviesToWatchApp(App):
    """GUI version of Movie to watch App."""

    def __init__(self, **kwargs):
        """
        Construct main app.
        """
        super().__init__(**kwargs)
        # basic properties for text in dict
        self.text_attr = SPINNER_DICT
        self.sort_methods = list(self.text_attr.keys())
        self.sort_current = self.sort_methods[0]
        # load movies data and store it into property movies.
        self.movies = MovieCollection()
        self.movies.load_movies(DATA_PATH)
        # create property programme_message.
        self.programme_message = WELCOME
        Window.size = (900, 600)

    def build(self):
        """
        Build the Kivy GUI.
        """
        self.title = "Movies to watch"
        self.root = Builder.load_file("app.kv")
        # update upper label, lower label and buttons.
        self.update_all()

        return self.root

    def change_state(self, text):
        """
        Handle change of spinner selection, sort movies by selected sort_method.
        """
        attr = self.text_attr[text]
        self.movies.sort(attr)
        # only updating buttons is needed here
        self.update_buttons()

    def press_add(self):
        """
        Handle press of add movie button.
        """
        # get contents of text fields
        title = self.root.ids.title.text
        year = self.root.ids.year.text
        category = self.root.ids.category.text

        if (title == "") | (year == "") | (category == ""):
            # one textfield is empty
            self.programme_message = "All fields must be completed."
            self.update_lower()
        else:
            try:
                year = int(year)
                if year < 1:
                    # year is less than 1
                    self.programme_message = "Year must be > 0."
                    self.update_lower()
                else:
                    # add movie
                    movie = Movie(title, year, category)
                    self.movies.add_movie(movie)

                    # update upper label, lower label and buttons
                    self.update_all()
            except ValueError:
                # year is not a number
                self.programme_message = "Please enter a valid number."
                self.update_lower()

    def press_clear(self):
        """
        Handle press of Clear Button.
        """
        self.root.ids.title.text = ""
        self.root.ids.year.text = ""
        self.root.ids.category.text = ""

    def press_movie(self, instance):
        """
        Handle press of movie button.
        """
        i = int(instance.id)
        movie = self.movies.movies[i]
        # switched between watched and unwatched.
        if movie.is_watched:
            movie.unwatched()
            self.programme_message = "You need to watched {}.".format(movie.title)
        else:
            movie.watched()
            self.programme_message = "You have watched {}.".format(movie.title)
        # update upper label, lower label and buttons
        self.update_all()

    def update_buttons(self):
        """
        Clear all buttons first.
        Create buttons in the GUI according to movies.
        """
        self.root.ids.movies_press.clear_widgets()
        for i, movie in enumerate(self.movies.movies):
            temp_button = Button(id=str(i))
            temp_button.bind(on_release=self.press_movie)
            # get information of thee and print it on corresponding button.
            title = movie.title
            year = movie.year
            category = movie.category

            if movie.is_watched:
                watched = " (watched)"
                temp_button.background_color = [1, 1, 1, 1]
            else:
                watched = ""
                temp_button.background_color = BUTTON_COLOR
            text = "{} from {},  {} {}".format(title, year, category, watched)
            temp_button.text = text
            # add button to movies_press
            self.root.ids.movies_press.add_widget(temp_button)

    def update_upper(self):
        """
        Update the upper message of label.
        """
        self.root.ids.upper_message.text = "To watch: {}  Watched: {}".format(self.movies.num_unwatched(),
                                                                              self.movies.num_watched())

    def update_lower(self):
        """
        Update the lower message of label.
        """
        self.root.ids.lower_message.text = self.programme_message

    def update_all(self):
        """
        Update all infomation concerning the movies in the GUI.
        """
        self.update_buttons()
        self.update_upper()
        self.update_lower()

    def on_stop(self):
        """
        Run when the app exits.
        """
        self.movies.save_movies(DATA_PATH)


if __name__ == '__main__':
    MoviesToWatchApp().run()
