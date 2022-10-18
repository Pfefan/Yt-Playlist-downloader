import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from aud_down import aud_down


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        sync_btn = QPushButton("Download / Sync playlist")
        sync_btn.setMaximumHeight(50)
        sync_btn.setMaximumWidth(150)
        sync_btn.clicked.connect(self.syncbtn_click)

        grid.addWidget(sync_btn)

        self.resize(640, 360)
        self.setWindowTitle('Yt-Playlist-downloader')
        self.show()

    def syncbtn_click(self):
        aud_down().main()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
