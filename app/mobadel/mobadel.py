import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

def andazee(self):
    try:
        # دریافت مقدار ورودی از ورودی کاربر
        per = self.ui.lineEdit_21.text()
        per = float(per)
        
        # محاسبه و تبدیل به واحدهای دیگر
        km = per / 1000
        km = round(km, 3)
        mm = per * 10000
        mm = round(mm, 3)
        cm = per * 100
        cm = round(cm, 3)
        mile = per * 0.00062
        mile = round(mile, 3)
        yard = per * 1.094
        yard = round(yard, 3)
        inch = per * 39.37
        inch = round(inch, 3)
        foot = per * 3.281
        foot = round(foot, 3)
        dm = per * 10
        dm = round(dm, 3)

        # نمایش نتایج در برچسب‌ها مربوطه
        self.ui.label_17.setText(str(km))
        self.ui.label_18.setText(str(mm))
        self.ui.label_19.setText(str(cm))
        self.ui.label_20.setText(str(foot))
        self.ui.label_21.setText(str(yard))
        self.ui.label_22.setText(str(mile))
        self.ui.label_23.setText(str(inch))
        self.ui.label_24.setText(str(dm))
    except ZeroDivisionError:
        self.ui.label_17.setText("عدد صفر وارد نکنید")     
    except:
        self.ui.label_17.setText("لطفاً عدد را وارد کنید")

def delet_all_andaze(self):
    # پاک کردن محتوای برچسب‌ها و ورودی
    self.ui.label_17.clear()
    self.ui.label_18.clear()
    self.ui.label_19.clear()
    self.ui.label_20.clear()
    self.ui.label_21.clear()
    self.ui.label_22.clear()
    self.ui.label_23.clear()
    self.ui.label_24.clear()
    self.ui.lineEdit_21.clear()
