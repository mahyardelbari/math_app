import sys
import os
# فراخوانی دایرکتوری ها 
sys.path.append('app/riazi/riaz.py')
sys.path.append('app/olom/olom.py')
sys.path.append('app/motarjem/translate.py')
sys.path.append('app/ai/chat.py')
sys.path.append('app/mobadel/mobadel.py')
sys.path.append('app/salamt/salamt.py')
sys.path.append('app/wiki/wiki.py')
sys.path.append('app/map/test.py')
sys.path.append('app/riazi/gharbal.py')

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox , QListWidgetItem 
from PyQt5.QtCore import QObject
sys.path.append('style/slidebar_ui.py')
from style.slidebar_ui import Ui_MainWindow
import sqlite3
import webbrowser
import subprocess


from PyQt5 import QtCore
from app.olom.olom import sorattt, shetabbb, delete_Shetab, delete_sorattt, feshar_jamed, feshar_maye, delete_feshar_jamed, delete_feshar_maye,chegali,delete_all_chegali
from app.mobadel.mobadel import andazee, delet_all_andaze
from app.riazi.riaz import (
                    adad_aval, etehadd_moraba1,etehadd_moraba2, etehadd_moz,
                    delet_all_etehad, delet_all_aval,
                    fisaghores, delet_all_fisa, hajm_kore, delete_all_kore_hajm,
                    masahat_kore, delete_all_kore_masahat,hajm_mokab,masahat_mokab,
                    delete_all_mokab_hajm,delete_all_mokab_masahat,delete_all_ostovane_masahat,
                    delete_all_ostovane_hajm,hajm_ostovane,masahat_ostovane,
                    delete_jom,etehad_moshtarak,hendese,abss,delete_all_abs,
                    moadele_yek,moadele_do,delet_all_moadele,delete_all_moadele_marhale,
                    delete_all_mohase_mobara,mohasebe_moraba,mohasebe_mostatil,
                    delete_all_mohasebe_mosta,delete_mohasebe_mosalas,mohseb_mosalas,
                    mohasebe_chand_zeli,delete_mohasebe_chand_zeli,tajzie,delete_all_tajzie,darsad_giri)
from app.salamet.salamat import bmi ,delete_all_salamat
from app.motarjem.translate import translator, trans_copy, delete_all_trans
from app.wiki.wiki import wikii, wiki_copy, delete_all_wiki
from app.map.test import showMap
from app.riazi.gharbal import gharbal,delete_all_gharbal
class screen(QMainWindow):
    def __init__(self):
        super(screen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('دانشور')
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.ui.saveButton.clicked.connect(self.saveChanges)
        self.ui.addButton.clicked.connect(self.addNewTask)
        self.ui.textEdit_3.setReadOnly(True)
        self.ui.textEdit_4.setReadOnly(True)
        self.ui.textEdit_5.setReadOnly(True)
        self.ui.textEdit_6.setReadOnly(True)
        self.ui.textEdit_13.setReadOnly(True)

    def on_btn_riaz2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        
    def on_btn_salamat2_8_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_btn_dar2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_btn_olom_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_btn_olom2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_btn_mobadel2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_btn_mobadel_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_btn_salamat2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_btn_salamat_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_btn_aval_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(51)

    def on_btn_aval_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(26)

    def on_btn_sorat_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_btn_sorat_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def on_btn_sorat_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def on_btn_aval_5_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(10)

    def on_btn_aval_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(11)

    def on_btn_aval_4_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(9)

    def on_btn_salamat2_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(12)

    def on_btn_bazi_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(12)

    def on_pushButton_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(13)

    def on_pushButton_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def on_btn_aval_6_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(15)

    def on_btn_aval_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(14)

    def on_btn_salamat_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(17)

    def on_btn_salamat2_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(17)

    def on_btn_sorat_5_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(18)

    def on_btn_feshar_jamed_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(16)

    def on_btn_feshar_maye_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(19)

    def on_btn_wiki_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(20)

    def on_btn_salamat2_4_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(20)
        messageBox = QMessageBox()
        messageBox.setText('این سایت به ای پی ای ویکی پدیا وصل است و ممکن سات خطا داشته باشد')
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()
        sender = QObject.sender(self)
        sender.clicked.disconnect()
        self.ui.btn_salamat2_4.clicked.connect(self.on_btn_salamat2_4_clicked)

    def on_btn_wiki_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(30)

    def on_btn_salamat2_5_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(30)


    def on_btn_sorat_11_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(24)

    def on_btn_sorat_6_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(21)

    def on_btn_sorat_7_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(22)

    def on_btn_sorat_8_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(23)
        
    def on_btn_sorat_10_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def on_btn_sorat_9_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(27)
        
    def on_pushButton_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(28)

    def on_pushButton_4_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(27)

    def on_btn_salamat_4_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(29)

    def on_btn_salamat2_6_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(29)

    def on_btn_sorat_12_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(31)

    def on_btn_aval_7_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(47)

    def on_btn_aval_8_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(33)

    def on_btn_aval_9_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(34)

    def on_btn_aval_10_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(35)

    def on_pushButton_7_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(35)

    def on_pushButton_6_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(36)

    def on_btn_sorat_12_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(37)

    def on_btn_aval_11_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(39)

    def on_btn_feshar_maye_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(40)

    def on_pushButton_12_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(41)

    def on_pushButton_89_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(39)

    def on_pushButton_71_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(40)

    def on_btn_feshar_maye_4_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(42)

    def on_btn_aval_12_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(32)

    def on_btn_aval_13_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(48)

    def on_btn_aval_14_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(43)

    def on_btn_aval_15_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(45)

    def on_btn_aval_16_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(46)

    def on_btn_aval_17_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(44)

    def on_btn_aval_18_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_btn_aval_19_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(49)

    def on_btn_salamat2_9_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(50)

    def on_btn_aval_20_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(52)
# physic pages


    def on_pushButton_20_clicked(self):
        sorattt(self)

    def on_pushButton_15_clicked(self):
        delete_sorattt(self)

    def on_pushButton_19_clicked(self):
        shetabbb(self)

    def on_pushButton_13_clicked(self):
        delete_Shetab(self)

    def on_pushButton_31_clicked(self):
        feshar_jamed(self)

    def on_pushButton_34_clicked(self):
        delete_feshar_jamed(self)

    def on_pushButton_36_clicked(self):
        feshar_maye(self)

    def on_pushButton_35_clicked(self):
        delete_feshar_maye(self)
# convertor pages
    def on_pushButton_16_clicked(self):
        andazee(self)

    def on_pushButton_30_clicked(self):
        delet_all_andaze(self)


# maths pages


    def on_pushButton_17_clicked(self):
        adad_aval(self)

    def on_pushButton_27_clicked(self):
        etehadd_moraba1(self)

    def on_pushButton_28_clicked(self):
        etehadd_moraba2(self)

    def on_pushButton_29_clicked(self):
        etehadd_moz(self)

    def on_pushButton_14_clicked(self):
        delet_all_etehad(self)

    def on_pushButton_21_clicked(self):
        delet_all_aval(self)

    def on_pushButton_22_clicked(self):
        fisaghores(self)

    def on_pushButton_23_clicked(self):
        delet_all_fisa(self)
# hajm kore

    def on_pushButton_58_clicked(self):
        hajm_kore(self)

    def on_pushButton_40_clicked(self):
        delete_all_kore_hajm(self)
# masahat kore

    def on_pushButton_57_clicked(self):
        masahat_kore(self)

    def on_pushButton_41_clicked(self):
        delete_all_kore_masahat(self)


    def on_pushButton_59_clicked(self):
        hajm_mokab(self)

    def on_pushButton_60_clicked(self):
        delete_all_mokab_hajm(self)
    
    def on_pushButton_47_clicked(self):
        masahat_mokab(self)

    def on_pushButton_46_clicked(self):
        delete_all_mokab_masahat(self)
    
    def on_pushButton_49_clicked(self):
        hajm_ostovane(self)

    def on_pushButton_48_clicked(self):
        delete_all_ostovane_hajm(self)
    
    def on_pushButton_193_clicked(self):
        masahat_ostovane(self)

    def on_pushButton_50_clicked(self):
        delete_all_ostovane_masahat(self)

# salamat pages
    def on_pushButton_18_clicked(self):
        bmi(self)
    
    def on_pushButton_42_clicked(self):
        delete_all_salamat(self)


# translate page

    def on_pushButton_24_clicked(self):
        translator(self)

    def on_pushButton_25_clicked(self):
        trans_copy(self)

    def on_pushButton_26_clicked(self):
        delete_all_trans(self)
# wiki pedia page

    def on_pushButton_38_clicked(self):
        wikii(self)

    def on_pushButton_39_clicked(self):
        wiki_copy(self)

    def on_pushButton_37_clicked(self):
        delete_all_wiki(self)
    
    def on_pushButton_54_clicked(self):
        chat_gptt(self)
    
    def on_pushButton_53_clicked(self):
        copy_chat(self)
    
    def on_pushButton_52_clicked(self):
        delete_Chat(self)
    
    def on_pushButton_32_clicked(self):
        etehad_moshtarak(self)
    
    def on_pushButton_55_clicked(self):
        delete_jom(self)

    def on_btn_salamat_5_clicked(Self):
        showMap()
        feshar_jamed
    def on_btn_salamat2_7_clicked(self):
        showMap()
        sender = QObject.sender(self)
        sender.clicked.disconnect()
        self.ui.btn_salamat2_7.clicked.connect(self.on_btn_salamat2_7_clicked)

    def on_pushButton_45_clicked(self):
        inputt = self.ui.comboBox.currentText()
        inputt = str(inputt)
        hendese(self,inputt)
    
    def on_pushButton_5_clicked(self):
        self.ui.lineEdit_6.insert("√")
        sender = QObject.sender(self)
        sender.clicked.disconnect()
        self.ui.pushButton_5.clicked.connect(self.on_pushButton_5_clicked)
    
    def on_pushButton_8_clicked(self):
        self.ui.lineEdit_6.insert("|")
        sender = QObject.sender(self)
        sender.clicked.disconnect()
        self.ui.pushButton_8.clicked.connect(self.on_pushButton_8_clicked)

    def on_pushButton_51_clicked(self):
        abss(self)
    
    def on_pushButton_61_clicked(self):
        delete_all_abs(self)
    
    def on_pushButton_66_clicked(self):
        moadele_yek(self)
    
    def on_pushButton_67_clicked(self):
        moadele_do(self)
    
    def on_pushButton_68_clicked(self):
        delet_all_moadele(self)
        
    def on_pushButton_69_clicked(self):
        chegali(self)
    
    def on_pushButton_70_clicked(self):
        delete_all_chegali(self)
    
    def on_pushButton_64_clicked(self):
        inp = self.ui.lineEdit_16.text()
        def solve_expression(expression):
            result = subprocess.run(['node', 'moadele.js', expression], capture_output=True)
            result = result.stdout.decode()
            return  result
        marhale = solve_expression(inp)
        marhale = marhale.replace("Before change","قبل از تغیر")
        marhale = marhale.replace("Change","تغیر")
        marhale = marhale.replace("After change","بعد از تغیر")
        marhale = marhale.replace("ADD_TO_BOTH_SIDES","اضافه کردن به هردو طرف")
        marhale = marhale.replace("SIMPLIFY_LEFT_SIDE","ساده سازی سمت چپ")
        marhale = marhale.replace("SIMPLIFY_Right_SIDE","ساده سازی سمت راست")
        marhale = marhale.replace("SIMPLIFY_ARITHMETIC","ساده سازی سوال")
        marhale = marhale.replace("DIVIDE_FROM_BOTH_SIDES","تقسیم بر هردو طرف")
        marhale = marhale.replace("SIMPLIFY_FRACTION","ساده سازی کسر")
        marhale = marhale.replace("SWAP_SIDES","تعویض طرفین")
        marhale = marhale.replace("SUBTRACT_FROM_BOTH_SIDES","کم کردن از هردو طرف")
        marhale = marhale.replace("COLLECT_AND_COMBINE_LIKE_TERMS","جمع و ترکیب اصطلاحات مشابه")
        self.ui.textEdit_3.setText(marhale)
    def on_pushButton_65_clicked(self):
        delete_all_moadele_marhale(self)
        
    def on_pushButton_62_clicked(self):
        gharbal(self)
    
    def on_pushButton_63_clicked(self):
        delete_all_gharbal(self)
        
    def on_pushButton_91_clicked(self):
        mohasebe_moraba(self)
    
    def on_pushButton_92_clicked(self):
        delete_all_mohase_mobara(self)
    
    def on_pushButton_96_clicked(self):
        mohasebe_mostatil(self)
    
    def on_pushButton_95_clicked(self):
        delete_all_mohasebe_mosta(self)
    
    def on_pushButton_94_clicked(self):
        mohseb_mosalas(self)
    
    def on_pushButton_93_clicked(self):
        delete_mohasebe_mosalas(self)
    
    def on_pushButton_97_clicked(self):
        mohasebe_chand_zeli(self)
    
    def on_pushButton_200_clicked(self):
        delete_mohasebe_chand_zeli(self)

    def on_pushButton_213_clicked(self):
        tajzie(self)
    
    def on_pushButton_214_clicked(self):
        delete_all_tajzie(self)

    def on_pushButton_216_clicked(self):
        base = "https://ino.school/app/learning/"
        paye = self.ui.comboBox_4.currentText()                             
        drs = self.ui.comboBox_5.currentText()
        base_drs = f"{drs}-{paye}/"
        base_paye = f"متوسطه-اول-پایه-{paye}/"
        finall  = f'{base}{base_paye}{base_drs}'
        sender = QObject.sender(self)
        sender.clicked.disconnect()
        self.ui.pushButton_216.clicked.connect(self.on_pushButton_216_clicked)
        webbrowser.open(finall)


    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'تأیید',
            'آیا مطمئن هستید که می خواهید خارج شوید؟',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
# darsad giri
    def on_pushButton_215_clicked(self):
        darsad_giri(self)
        sender = QObject.sender(self)
        sender.clicked.disconnect()
        self.ui.pushButton_215.clicked.connect(self.on_pushButton_215_clicked)

#back btns 
    def on_pushButton_74_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(51)
    
    def on_pushButton_9_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_pushButton_11_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_pushButton_82_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(47)
    
    def on_pushButton_78_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_pushButton_76_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_pushButton_83_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_pushButton_75_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(26)
    
    def on_pushButton_77_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(26)
    
    def on_pushButton_81_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(14)
    
    def on_pushButton_80_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(14)
    
    def on_pushButton_79_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(14)
    
    def on_pushButton_86_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    
    def on_pushButton_87_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    
    def on_pushButton_88_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    
    def on_pushButton_10_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    
    def on_pushButton_85_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(18)
    
    def on_pushButton_84_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(18)
    
    def on_pushButton_202_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_pushButton_195_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(47)
    
    def on_pushButton_199_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(48)
    
    def on_pushButton_198_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(48)
    
    def on_pushButton_197_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(48)
    
    def on_pushButton_196_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(48)
    
    def on_pushButton_201_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_pushButton_203_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(51)
    
    def updateTaskList(self, date):
        self.ui.tasksListWidget.clear()

        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        query = "SELECT task, completed FROM tasks WHERE date = ?"
        row = (date,)
        results = cursor.execute(query, row).fetchall()
        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            elif result[1] == "NO":
                item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tasksListWidget.addItem(item)


    def calendarDateChanged(self):
        dateSelected = self.ui.calendarWidget.selectedDate().toPyDate()
        self.updateTaskList(dateSelected)

    def saveChanges(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        date = self.ui.calendarWidget.selectedDate().toPyDate()

        for i in range(self.ui.tasksListWidget.count()):
            item = self.ui.tasksListWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE task = ? AND date = ?"
            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND date = ?"
            row = (task, date,)
            cursor.execute(query, row)
        db.commit()

        messageBox = QMessageBox()
        messageBox.setText("ذخیره شد")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def addNewTask(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        newTask = str(self.ui.taskLineEdit.text())
        date = self.ui.calendarWidget.selectedDate().toPyDate()

        query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)"
        row = (newTask, "NO", date,)

        cursor.execute(query, row)
        db.commit()
        self.updateTaskList(date)
        self.ui.taskLineEdit.clear()

style = """
/*= Style for mainwindow START
  ==================================================== */
  #MainWindow {
	background-color: #1A5F7A;
}
/*= END
==================================================== */
/*= Style for button to change menu style START
==================================================== */
#changebtn {
	padding: 5px;
	border: none;
	width: 30px;
	height: 30px;
}

/*= END
==================================================== */
/*= Style for menu with icon only START
==================================================== */
  /* style for widget */
#icon_only_widget {
	background-color: #1A5F7A;
	width:50px;
}


/* style for QPushButton and QLabel */
#icon_only_widget QPushButton, QLabel {
		height:50px;
        
		border:none;
	/* border: 1px solid #57C5B6; */

}
#button{
	border: 1px soloid #57C5B6;
	/* border-width: 5px; */
}

#icon_only_widget QPushButton:hover {
	background-color: rgba( 86, 101, 115, 0.5);
}

/*= END
==================================================== */
/*= Style for menu with icon and text START
==================================================== */
/* style for widget */
#full_menu_widget {
	background-color: #1A5F7A;
}

/* style for QPushButton */
#full_menu_widget QPushButton {
	border:none;
	border-radius: 6px;
	text-align: left;
	padding: 8px 0 8px 15px;
	color: #788596;
}


#full_menu_widget QPushButton:hover {
	background-color: rgba( 86, 101, 115, 0.5);
 
}

#full_menu_widget QPushButton:checked {
	color: #1A5F7A;
}


/* style for APP title */
#logo_label_3 {
	padding-right: 10px;
	color: #1A5F7A;
}
/*= END
==================================================== */
/*= Style for header widget START
==================================================== */
#widget {
	background-color: #1A5F7A;
}
/*= END
==================================================== */
    """

app = QApplication(sys.argv)
app.setStyleSheet(style)
window = screen()
window.show()
sys.exit(app.exec())



# python -m PyQt5.uic.pyuic -x mainwindow.ui -o slidebar_ui.py
sorattt