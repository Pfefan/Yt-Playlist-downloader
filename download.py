import os
from threading import Thread

from pytube import Playlist


class down():
    def __init__(self, _GUI, savepath_) -> None:
        self.GUI = _GUI
        self.path = savepath_
        self.invalid_characters = '\/:*?"<>|'

    def main(self):
        if not os.path.exists("playlists.txt"):
            open("playlists.txt", "w+").close()
        self.download()

    def download(self):
        """Downloads a given songs in a List of Playlists"""
        urls = []
        with open("playlists.txt", "r", encoding="utf8") as pfile:
            urls = pfile.readlines()
            pfile.close()

        for url in urls:
            counter = 0
            p = Playlist(url)
            self.GUI.pbar.setValue(0)
            self.GUI.pbar.setMaximum(len(p.videos))
            print(self.path + "\\" + p.title)

            if not os.path.exists(self.path + "\\" + p.title):       # creates playlist dir if it doesnt exist
                os.mkdir(os.path.join(self.path, p.title))
            files = os.listdir(os.path.join(self.path, p.title))

            self.GUI.pbarlabel.setText(f'Syncing: {p.title}')

            for video in p.videos:
                self.GUI.pbarlabel.setText(f'Syncing: {p.title} {counter}/{len(p.videos)}')
                self.GUI.pbar.setValue(counter)

                for char in self.invalid_characters: video.title =  video.title.replace(char, "") # refactore video title so no files will be save with invalid strings
                file = video.title + ".mp3"
                if file not in files:       #checks if video is already download so it doesnt have to repeat it
                    audio = video.streams.filter(only_audio=True).first()
                    out_file = audio.download(output_path=os.path.join(self.path, p.title))
                    new_file = os.path.join(self.path, p.title, file)
                    os.rename(out_file, new_file)
                counter += 1

        self.GUI.pbarlabel.setText(f'Finished Syncing')
        self.GUI.pbar.setValue(0)
