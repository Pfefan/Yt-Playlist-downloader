import json
import os
import sys
from threading import Thread

from PyQt6 import QtGui
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from download import down


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.config = {}
        if not os.path.exists("config.conf"):
            config = {
                "savepath" : f"{os.getcwd()}\\download"
            }
            with open("config.conf", "w+") as file:
                json.dump(config, file)

        with open("config.conf", "r") as file:
            self.config = json.load(file)

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        titlelable = QLabel("YouTube Playlist Sync by Pfefan")
        self.pbarlabel = QLabel("Progress...")
        self.pbar = QProgressBar()
        self.playlist_input = QLineEdit()
        seldir_btn = QPushButton("Select save directory")
        add_btn = QPushButton("Add Playlist")
        sync_btn = QPushButton("Sync playlist")

        titlelable.setFont(QFont('Comic Sans MS', 15))
        self.pbarlabel.setMinimumWidth(200)
        
        add_btn.clicked.connect(self.add_playlist)
        seldir_btn.clicked.connect(self.pick_dir)
        sync_btn.clicked.connect(self.syncbtn_click)

        grid.addWidget(titlelable, 0, 0)

        grid.addWidget(self.playlist_input, 1, 0)
        grid.addWidget(add_btn, 1, 1)

        grid.addWidget(seldir_btn, 2, 1)

        grid.addWidget(sync_btn, 3, 1)

        grid.addWidget(self.pbar, 4, 0, 4, 1)
        grid.addWidget(self.pbarlabel, 4, 1, 4, 1)


        self.setStyleSheet("background-color: #d3d2db")
        self.resize(480, 270)
        self.setWindowTitle('Yt-Playlist-downloader')
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.show()

    def pick_dir(self):
        self.config["savepath"] = QFileDialog.getExistingDirectory(self, "Select Folder")
        with open("config.conf", "w+") as file:
                json.dump(self.config, file)

    def syncbtn_click(self):
        Thread(target=down(self, self.config["savepath"]).main, daemon=True).start()

    def add_playlist(self):
        if not os.path.exists("playlists.txt"):
            open("playlists.txt", "w+").close()

        with open("playlists.txt", "r", encoding="utf8") as readfile:
            filecontent = readfile.readlines()

        with open("playlists.txt", "a", encoding="utf8") as appendfile:
            content = self.playlist_input.text()
            if content not in filecontent and content + "\n" not in filecontent:
                appendfile.write(content + "\n")
                self.playlist_input.setText("")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
