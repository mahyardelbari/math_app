from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QFont



def gharbal(self):
    try:
        n = int(self.ui.lineEdit_47.text())
        self.ui.textEdit_2.setReadOnly(True)
        output = ghar_algo(n)
        font = QFont()
        font.setPointSize(14)
        self.ui.textEdit_2.setFont(font)
        self.ui.textEdit_2.setText(output)
    except:
        pass
def ghar_algo(n):
    try:
        numbers = list(range(2, n+1))
        primes = []
        while len(numbers) > 0:
            prime = numbers[0]
            primes.append(prime)
            for i in range(prime, n+1, prime):
                if i in numbers:
                    numbers.remove(i)
        output = ""
        for i in range(1, n+1):
            if i in primes:
                output += "<font color='black'>{}</font> ".format(i)
            else:
                output += "<font color='red'>{}</font> ".format(i)
            if i % 20 == 0:
                output += "<br>"
        return output
    except:
        pass
def delete_all_gharbal(self):
    self.ui.lineEdit_47.clear()
    self.ui.textEdit_2.clear()