import os
from threading import Thread

from pytube import Playlist


class aud_down():
    def __init__(self) -> None:
        pass

    def main(self):
        print(os.path.exists("playlists.txt"))
        if not os.path.exists("playlists.txt"):
            open("playlists.txt", "w+").close()
        self.download()

    def download(self):
        """Downloads a given songs in a List of Playlists"""
        urls = []
        with open("playlists.txt", "r", encoding="utf8") as file:
            urls = file.readlines()

        for url in urls:
            counter = 1
            p = Playlist(url)
            print(f'Downloading: {p.title}', end="\r")
            for video in p.videos:
                print(f'Downloading: {p.title} {counter}/{len(p.videos)}', end="\r")
                audio = video.streams.filter(only_audio=True).first()
                out_file = audio.download(output_path=f"out_aud/{p.title}")
                base = os.path.splitext(out_file)[0]
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                counter += 1
