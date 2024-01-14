import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

def sorattt(self):
    try:
        # دریافت ورودی‌ها
        first_speed = self.ui.lineEdit_17.text()
        first_speed = float(first_speed)
        secend_speed = self.ui.lineEdit_18.text()
        secend_speed = float(secend_speed)
        speed_result = secend_speed - first_speed
        first_time = self.ui.lineEdit_19.text()
        first_time = float(first_time)
        secend_time = self.ui.lineEdit_20.text()
        secend_time = float(secend_time)
        time_result = secend_time - first_time

        # محاسبه نتیجه
        result = speed_result/time_result
        result = round(result, 3)
        resultt = f"{result}m/s"
        self.ui.label_13.setText(str(resultt))
    except ZeroDivisionError:
        self.ui.label_13.setText(str("تقسیم بر صفر نمیشود"))
    except:
        self.ui.label_13.setText(str("لطفا کل جاها را پر کنید"))
# تابع delete_sorattt همانند تابع sorattt عمل می‌کند
def delete_sorattt(self):
    first_speed = self.ui.lineEdit_17.clear()
    secend_speed = self.ui.lineEdit_20.clear()
    first_time = self.ui.lineEdit_19.clear()
    secend_time = self.ui.lineEdit_18.clear()
    self.ui.label_13.clear()
    
def shetabbb(self):
    try:
        # دریافت ورودی‌ها
        first_speed = self.ui.lineEdit_26.text()
        first_speed = float(first_speed)
        secend_speed = self.ui.lineEdit_25.text()
        secend_speed = float(secend_speed)
        speed_result = secend_speed - first_speed
        first_time = self.ui.lineEdit_28.text()
        first_time = float(first_time)
        secend_time = self.ui.lineEdit_27.text()
        secend_time = float(secend_time)
        time_result = secend_time - first_time

        # محاسبه نتیجه
        result = speed_result/time_result
        result = round(result, 3)
        resultt = f"{result}m/s2"
        self.ui.label_12.setText(str(resultt))
    except ZeroDivisionError:
        self.ui.label_12.setText(str("تقسیم بر صفر نمیشود"))
    except:
        self.ui.label_12.setText(str("لطفا کل جاها را پر کنید"))
# تابع delete_Shetab همانند تابع shetabbb عمل می‌کند
def delete_Shetab(self):
    self.ui.lineEdit_26.clear()
    self.ui.lineEdit_25.clear()
    self.ui.lineEdit_28.clear()
    self.ui.lineEdit_27.clear()
    self.ui.label_12.clear()


def feshar_maye(self):
    try:
        # دریافت ورودی‌ها
        inp1 = self.ui.lineEdit_30.text()
        inp1 = float(inp1)
        inp2 = self.ui.lineEdit_32.text()
        inp2 = float(inp2)
        inp3 = self.ui.lineEdit_33.text()
        inp3 = float(inp3)
        
        # محاسبه نتیجه
        result = inp1 * inp2 * inp3
        result = round(result, 3)
        resultt = f"{result}pa"
        self.ui.label_103.setText(str(resultt))
    except:
        pass
# تابع delete_feshar_maye همانند تابع feshar_maye عمل می‌کند
def delete_feshar_maye(self):
    self.ui.lineEdit_30.clear()
    self.ui.lineEdit_32.clear()
    self.ui.lineEdit_33.clear()
    self.ui.label_103.clear()


def feshar_jamed(self):
    try:
        # دریافت ورودی‌ها
        inp1 = self.ui.lineEdit_13.text()
        inp1 = float(inp1)
        inp2 = self.ui.lineEdit_8.text()
        inp2 = float(inp2)
        
        # محاسبه نتیجه
        result = inp1 / inp2
        result = round(result, 3)
        resultt = f"{result}pa"
        self.ui.label_88.setText(str(resultt))
    except:
        pass
# تابع delete_feshar_jamed همانند تابع feshar_jamed عمل می‌کند
def delete_feshar_jamed(self):
    self.ui.lineEdit_13.clear()
    self.ui.lineEdit_8.clear()
    self.ui.label_88.clear()
    
    
def chegali(self):
    try:
        # دریافت ورودی‌ها
        mass = self.ui.lineEdit_52.text()
        mass = float(mass)
        valo = self.ui.lineEdit_53.text()
        valo = float(valo)
        
        # محاسبه نتیجه
        result = mass / valo
        result = round(result, 3)
        result = str(result)
        result = f"{result}kg/m³"
        self.ui.label_231.setText(result)
    except:
        pass

# تابع delete_all_chegali همانند تابع chegali عمل می‌کند

def delete_all_chegali(self):
    self.ui.lineEdit_52.clear()
    self.ui.lineEdit_53.clear()
    self.ui.label_231.clear()