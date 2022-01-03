from utils import download_window, find_links_window
import math
import random
import sys  # sys нужен для передачи argv в QApplication

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QApplication, QFileDialog
from loguru import logger

import MainWindow  # Это наш конвертированный файл дизайна


logger.add("error.log", level="ERROR", rotation="100 MB", format="{time} - {level} - {message}")

class DowloadApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pasteButton.clicked.connect(self.paste)
        self.findButton.clicked.connect(self.find_file)
        self.downloadButton.clicked.connect(self.download_file)
        self.list_file = []

    def download_file(self):
        row = self.tableURL.currentItem().row()
        url = self.list_file[row][0]
        download_window(url, self.progressBar)

    def paste(self):
        c = QApplication.clipboard()
        self.urlEdit.setText(c.text())

    def find_file(self):
        self.list_file = find_links_window(self.urlEdit.text())
        self.tableURL.setRowCount(len(self.list_file))
        for i, url in enumerate(self.list_file):
            self.tableURL.setItem(i, 0, QTableWidgetItem(url[1]))

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = DowloadApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    # url = 'http://xn----7sbb4ab0aeerjehf9j.xn--p1ai/products/stojkoe-serdtse-1-4'
    # for elem in find_links(url):
    #     download(elem)
    main()
