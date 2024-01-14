import sys
# وارد کردن کتابخانه‌ی sys

from PyQt5.QtWidgets import  QMessageBox
# وارد کردن کلاس‌ها و توابع مورد نیاز از کتابخانه‌ی PyQt5

import pyperclip
# وارد کردن کتابخانه‌ی pyperclip برای کپی کردن به Clipboard

from deep_translator import GoogleTranslator
# وارد کردن کلاس GoogleTranslator از کتابخانه‌ی deep_translator برای ترجمه


sys.path.append('style/slidebar_ui.py')
# افزودن مسیر فایل slidebar_ui.py به sys.path

pyperclip.copy('The text to be copied to the clipboard.')
# کپی کردن متن 'The text to be copied to the clipboard.' به Clipboard


def translator(self):
    # تابع translator که self را به عنوان پارامتر دریافت می‌کند

    global out
    # تعریف یک متغیر جهانی به نام out

    try:
        la_1 = self.ui.comboBox_2.currentText()
        # دریافت متن انتخاب شده در comboBox_2

        la_1 = la_1[:2]
        # انتخاب دو حرف اول از متن

        la_2 = self.ui.comboBox_3.currentText()
        # دریافت متن انتخاب شده در comboBox_3

        la_2 = la_2[:2]
        # انتخاب دو حرف اول از متن

        inp = self.ui.textEdit.toPlainText()
        # دریافت متن وارد شده در textEdit

        out = GoogleTranslator(source=la_1, target=la_2).translate(text=inp)
        # ترجمه متن inp از زبان la_1 به زبان la_2 با استفاده از کلاس GoogleTranslator و ذخیره نتیجه در متغیر out

        self.ui.label_78.setWordWrap(True)
        # فعال کردن قابلیت Word Wrap برای label_78

        self.ui.label_78.setText(out)
        # تنظیم متن out برای label_78
    except:
        messageBox = QMessageBox()
        # تعریف یک MessageBox جدید

        messageBox.setText("لطفا از اتصال خود به اینترنت اطمینان حاصل فرمایید")
        # تنظیم متن پیام خطا

        messageBox.setStandardButtons(QMessageBox.Ok)
        # تنظیم دکمه OK برای MessageBox

        messageBox.exec()
        # نمایش MessageBox


def trans_copy(self):
    # تابع trans_copy که self را به عنوان پارامتر دریافت می‌کند

    pyperclip.copy(out)
    # کپی کردن مقدار out به Clipboard


def delete_all_trans(self):
    # تابع delete_all_trans که self را به عنوان پارامتر دریافت می‌کند

    self.ui.textEdit.clear()
    # پاک کردن محتوای textEdit

    self.ui.label_78.clear()
    # پاک کردن محتوای label_78
