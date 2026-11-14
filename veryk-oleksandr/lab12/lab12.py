
from abc import ABC, abstractmethod


class MediaContent(ABC):
    @abstractmethod
    def get_info(self):
        pass


class ContentView(ABC):
    @abstractmethod
    def display(self, content):
        pass


class Movie(MediaContent):
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def get_info(self):
        return f"Фільм: {self.title}, {self.year}"


class MovieView(ContentView):
    def display(self, content):
        print(f"[КІНО] {content.get_info()}")


class TVShow(MediaContent):
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def get_info(self):
        return f"Серіал: {self.title}, {self.year}"


class TVShowView(ContentView):
    def display(self, content):
        print(f"[СЕРІАЛ] {content.get_info()}")


class MediaFactory(ABC):
    @abstractmethod
    def create_content(self, title, year):
        pass

    @abstractmethod
    def create_view(self):
        pass


class MovieFactory(MediaFactory):
    def create_content(self, title, year):
        return Movie(title, year)

    def create_view(self):
        return MovieView()


class TVShowFactory(MediaFactory):
    def create_content(self, title, year):
        return TVShow(title, year)

    def create_view(self):
        return TVShowView()


def show_media(factory, title, year):
    content = factory.create_content(title, year)
    view = factory.create_view()
    view.display(content)


movie_factory = MovieFactory()
show_media(movie_factory, "Inception", 2010)

series_factory = TVShowFactory()
show_media(series_factory, "Breaking Bad", 2008)
