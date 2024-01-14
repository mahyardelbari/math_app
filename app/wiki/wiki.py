import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox,QScrollArea,QVBoxLayout
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
sys.path.append('style/slidebar_ui.py')
from style.slidebar_ui import Ui_MainWindow
from deep_translator import GoogleTranslator
import pyperclip
import wikipedia


def wikii(self):
    try:
        inp = self.ui.lineEdit_14.text()
        search_result = wikipedia.summary(inp)
        global out
        out = GoogleTranslator(source="en", target="fa").translate(text=search_result)
        self.ui.textEdit_5.setText(out)
    except:
        messageBox = QMessageBox()
        messageBox.setText("لطفا از اتصال خود به اینترنت اطمینان حاصل فرمایید")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()


def wiki_copy(self):
    try:
        pyperclip.copy(out)
    except:
        pass

def delete_all_wiki(self):
    self.ui.lineEdit_14.clear()
    self.ui.textEdit_5.clear()
