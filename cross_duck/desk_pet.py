import os
import sys
import time
import random
import requests
import threading
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui

class DesktopPet(QWidget):
    def __init__(self, parent=None, **kwargs):
        super(DesktopPet, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")

        # 創建 QLabel 用於顯示圖片
        self.image_label = QLabel(self)

        # 載入圖片
        pixmap = QPixmap("img/duck_cross.png")  # 替換成你的圖片路徑
        self.image_label.setPixmap(pixmap.scaledToWidth(250))
        self.image_label.setScaledContents(True)

        self.resize(250, 250)
        self.setPosition(x = 0.95, y = 0.95)
        self.show()

    def setPosition(self, x = 0.9, y = 0.9):
        screen_geo = QDesktopWidget().screenGeometry()
        pet_geo = self.geometry()
        width = int((screen_geo.width() - pet_geo.width()) * x)
        height = int((screen_geo.height() - pet_geo.height()) * y)
        self.move(width, height)

if __name__ == '__main__':
    # 創建應用程序對象
    app = QApplication(sys.argv)

    # 創建 MyWidget 實例
    widget = DesktopPet()

    # 顯示窗口
    #widget.show()

    # 進入應用程序的主循環
    sys.exit(app.exec_())
