import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

#BMI
def bmi(self):
    try:
        weight = self.ui.lineEdit_24.text()  # وزن کاربر را از ویجت متنی دریافت می‌کنیم
        weight = float(weight)  # تبدیل وزن به عدد اعشاری
        height = self.ui.lineEdit_23.text()  # قد کاربر را از ویجت متنی دریافت می‌کنیم
        height = float(height)  # تبدیل قد به عدد اعشاری
        BMI = weight / (height/100)**2  # محاسبه شاخص توده بدنی (BMI)
        BMI = round(BMI, 2)  # گرد کردن BMI به دو رقم اعشار
        self.ui.label_43.setText(str(BMI))  # نمایش مقدار BMI در ویجت متنی نمایش داده

        if BMI < 18.5:
            self.ui.label_45.setText("کمبود وزن")  # نمایش متن "کمبود وزن" در ویجت متنی نمایش داده
            self.ui.label_47.setText("شما دچار کمبود وزن هستید با تنظیم رژیم غذایی و ورزش به وزن ایده عال برسی")  # نمایش متن توضیحی درباره کمبود وزن در ویجت متنی نمایش داده
        elif 18.5 < BMI < 24.9:
            self.ui.label_45.setText("وزن طبیعی")  # نمایش متن "وزن طبیعی" در ویجت متنی نمایش داده
            self.ui.label_47.setText("تبریک میگویم شما ایده ال هستین")  # نمایش متن توضیحی درباره وزن طبیعی در ویجت متنی نمایش داده
        elif 25 < BMI < 29.9:
            self.ui.label_45.setText("اضافه وزن")  # نمایش متن "اضافه وزن" در ویجت متنی نمایش داده
            self.ui.label_47.setText("شما دارای اضافخ وزن هستین توده ی بدنی خود را به 24 برسانید")  # نمایش متن توضیحی درباره اضافه وزن در ویجت متنی نمایش داده
        elif 30 < BMI < 34.9:
            self.ui.label_45.setText("چاق")  # نمایش متن "چاق" در ویجت متنی نمایش داده
            self.ui.label_47.setText("شما دارای چاقی هستید وزن خود را به حد مناسب برسانید")  # نمایش متن توضیحی درباره چاقی در ویجت متنی نمایش داده
        elif 35 < BMI:
            self.ui.label_45.setText("خیلی چاق")  # نمایش متن "خیلی چاق" در ویجت متنی نمایش داده
            self.ui.label_47.setText("شما خیلی چاق هستنین این چاقی می تواند خطرناک باشد")  # نمایش متن توضیحی درباره خیلی چاقی در ویجت متنی نمایش داده
    except:
        pass

def delete_all_salamat(self):
    self.ui.lineEdit_23.clear()  # حذف مقدار قد از ویجت متنی
    self.ui.lineEdit_24.clear()  # حذف مقدار وزن از ویجت متنی
    self.ui.label_43.clear()  # حذف مقدار BMI از ویجت متنی نمایش داده
    self.ui.label_45.clear()  # حذف متن وضعیت وزن از ویجت متنی نمایش داده
    self.ui.label_47.clear()  # حذف متن توضیحی وضعیت وزن از ویجت متنی نمایش داده
