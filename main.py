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
        playlist_input = QLineEdit()
        seldir_btn = QPushButton("Select save directory")
        add_btn = QPushButton("Add Playlist")
        sync_btn = QPushButton("Sync playlist")

        self.pbarlabel.setMinimumWidth(200)
        seldir_btn.clicked.connect(self.pick_dir)

        sync_btn.clicked.connect(self.syncbtn_click)
        sync_btn.setMaximumWidth(100)
        sync_btn.setMaximumHeight(40)

        grid.addWidget(titlelable, 0, 0)

        grid.addWidget(playlist_input, 1, 0)
        grid.addWidget(add_btn, 1, 1)

        grid.addWidget(seldir_btn, 2, 1)

        grid.addWidget(sync_btn, 3, 0, 3, 1)

        grid.addWidget(self.pbar, 4, 0, 4 ,1)
        grid.addWidget(self.pbarlabel, 4, 1, 4 ,1)

        self.resize(480, 270)
        self.setWindowTitle('Yt-Playlist-downloader')
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.show()

    def pick_dir(self):
        self.savepath = QFileDialog.getExistingDirectory(self, "Select Folder")

    def syncbtn_click(self):
        Thread(target=down(self, self.config["savepath"]).main, daemon=True).start()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
