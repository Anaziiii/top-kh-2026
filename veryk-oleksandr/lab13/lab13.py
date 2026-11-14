
from abc import ABC, abstractmethod


class MediaProvider(ABC):
    @abstractmethod
    def get_media_info(self):
        pass


class ExternalMovieAPI:
    def fetch_movie_data(self):
        return {
            "name": "Interstellar",
            "release_year": 2014
        }


class MovieAdapter(MediaProvider):
    def __init__(self, external_api):
        self.external_api = external_api

    def get_media_info(self):
        data = self.external_api.fetch_movie_data()

        return {
            "title": data["name"],
            "year": data["release_year"]
        }


def show_media(provider):
    media = provider.get_media_info()

    print(f"Назва: {media['title']}")
    print(f"Рік виходу: {media['year']}")



external_api = ExternalMovieAPI()
adapter = MovieAdapter(external_api)

show_media(adapter)
