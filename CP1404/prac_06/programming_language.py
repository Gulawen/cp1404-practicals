class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Constructor that takes in parameters and create object"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """return the detail of the language"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Judge if language is dynamic."""
        return self.typing == "Dynamic"


def test():
    """To check with python"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    print(python)


if __name__ == "__main__":
    test()
