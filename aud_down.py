from pytube import YouTube, Playlist
import os

class aud_down():
    def __init__(self) -> None:
        pass
    def main(self):
        p = Playlist("https://www.youtube.com/playlist?list=PLFRyiHPm85KLKGV6_Xml0xNGSuj1yyVrL")
        print(f'Downloading: {p.title}')
        for video in p.videos:
            audio = video.streams.filter(only_audio=True).first()
            out_file = audio.download(output_path=f"out_aud/{p.title}")
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
