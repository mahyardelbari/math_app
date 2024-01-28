from PyQt5.QtWidgets import  QMessageBox
from math import pi, tan, cos, sin
from sympy import simplify, sqrt, sympify, Abs, Eq
import re
import math
import sympy as sp

def adad_aval(self):
    try:
        inp = self.ui.lineEdit_22.text()
        inp = int(inp)

# shomarande
        list_smhrnde_aval = []
        tedad_smrnde_aval = 0
        tedad_smrnde = 0 
        for i in range(1, inp+1):
            if (inp % i == 0):
                tedad_smrnde += 1
                list_smhrnde_aval.append(i)

        self.ui.label_28.setText(str(tedad_smrnde))
        self.ui.label_30.setText(str(list_smhrnde_aval))

# tashkis
        if inp > 1:
            if tedad_smrnde > 2:
                self.ui.label_25.setText(str("عدد مرکب است"))
            else:
                self.ui.label_25.setText(str("عدد اول است"))

        if inp <= 1:
            self.ui.label_25.setText(str("عدد نه اول است نه مرکب"))

 # shomarande aval
        list_aval = []
        for po in list_smhrnde_aval:
            zx = 0
            for awd in range(1, po):
                if po % awd == 0:
                    zx += 1
            if zx == 1:
                list_aval.append(po)

        self.ui.label_60.setText(str(list_aval))
    except:
        self.ui.label_25.setText("لطفا کل جاها را پر کنید")


# etehad
def etehadd_moraba1(self):
    try:
        inp1 = self.ui.lineEdit.text()
        inp2 = self.ui.lineEdit_2.text()
        result = "("+inp1+"+"+inp2+")"+"**2"
        pattern = re.compile(r'(\d)([a-zA-Z])') 
        result = re.sub(pattern, r'\1*\2', result)
        result = result.replace("^","**")
        perr = sp.expand(result)
        perr = str(perr)
        resul = perr
        resul = resul.replace("**","^")
        resul = resul.replace("*","")
        self.ui.label_58.setText(resul)
    except:
        self.ui.label_58.setText("لطفا کل جاها را پر کنید")


def etehadd_moraba2(self):
    try:
        inp1 = self.ui.lineEdit_3.text()
        inp2 = self.ui.lineEdit_4.text()
        result = "("+inp1+"-"+inp2+")"+"**2"
        pattern = re.compile(r'(\d)([a-zA-Z])') 
        result = re.sub(pattern, r'\1*\2', result) 
        result = result.replace("^","**")
        perr = sp.expand(result)
        perr = str(perr)
        resul = perr
        resul = resul.replace("**","^")
        resul = resul.replace("*","")
        self.ui.label_59.setText(str(resul))
    except:
        self.ui.label_59.setText("لطفا کل جاها را پر کنید")


def etehadd_moz(self):
    try:
        inp1 = self.ui.lineEdit_9.text()
        inp2 = self.ui.lineEdit_10.text()
        inp3 = self.ui.lineEdit_11.text()
        inp4 = self.ui.lineEdit_12.text()
        result_inp_1 = "("+inp1+"+"+inp2+")"
        result_inp_2 = "("+inp3+"-"+inp4+")"
        result = result_inp_1+"*"+result_inp_2
        pattern = re.compile(r'(\d)([a-zA-Z])') 
        result = re.sub(pattern, r'\1*\2', result) 
        result = result.replace("^","**")
        perr = sp.expand(result)
        perr = str(perr)
        perr = perr.replace("**","^")
        perr = perr.replace("*","")
        self.ui.label_170.setText(perr)
    except:
        self.ui.label_170.setText("لطفا کل جاها را پر کنید")


def delet_all_etehad(self):
    self.ui.lineEdit.clear()
    self.ui.lineEdit_2.clear()
    self.ui.lineEdit_3.clear()
    self.ui.lineEdit_4.clear()
    self.ui.lineEdit_9.clear()
    self.ui.lineEdit_10.clear()
    self.ui.lineEdit_11.clear()
    self.ui.lineEdit_12.clear()
    self.ui.label_58.clear()
    self.ui.label_59.clear()
    self.ui.label_170.clear()


def delet_all_aval(self):
    self.ui.lineEdit_22.clear()
    self.ui.label_25.clear()
    self.ui.label_28.clear()
    self.ui.label_30.clear()
    self.ui.label_60.clear()


# fisaghores
def fisaghores(self):
    try:
        inp1 = self.ui.lineEdit_7.text()
        inp1 = float(inp1)
    except:
        pass
    try:
        inp2 = self.ui.lineEdit_45.text()
        inp2 = float(inp2)
    except:
        pass
    try:
        inp3 = self.ui.lineEdit_44.text()
        inp3 = float(inp3)
    except:
        pass
    try:
        if bool(inp1) == True and bool(inp2) == True:
            result = (inp1)**2+(inp2)**2
            resultt = math.sqrt(result)
            resultt = round(resultt, 3)
            self.ui.lineEdit_44.setText(str(resultt))
        elif bool(inp3) == True and bool(inp1) == True:
            res = (inp3)**2-(inp1)**2
            ress = math.sqrt(res)
            ress = round(ress, 3)
            self.ui.lineEdit_45.setText(str(ress))
        elif bool(inp3) == True and bool(inp2) == True:
            re = (inp3)**2 - (inp2)**2
            ree = math.sqrt(re)
            ree = round(ree, 3)
            self.ui.lineEdit_7.setText(str(ree))
    except:
        messageBox = QMessageBox()
        messageBox.setText("ای کلک درست وارد کن اعداد رو :)")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()


def delet_all_fisa(self):
    self.ui.lineEdit_44.clear()
    self.ui.lineEdit_7.clear()
    self.ui.lineEdit_45.clear()



#HAJM KORE
def hajm_kore(self):
    try:
        inp = self.ui.lineEdit_15.text()
        inp = float(inp)
        result = 4/3 * pi * inp**3
        result = round(result, 3)
        self.ui.label_99.setText(str(result))
    except:
        messageBox = QMessageBox()
        messageBox.setText("لطفا شعاع را وارد کنید")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

def delete_all_kore_hajm(self):
    self.ui.lineEdit_15.clear()
    self.ui.label_99.clear()

#MASAHAT KORE
def masahat_kore(self):
    try:
        inp = self.ui.lineEdit_46.text()
        inp = float(inp)
        result = 4 * pi * inp**2
        result = round(result,3)
        self.ui.label_116.setText(str(result))
    except:
        messageBox = QMessageBox()
        messageBox.setText("لطفا شعاع را وارد کنید")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

def delete_all_kore_masahat(self):
    self.ui.lineEdit_46.clear()
    self.ui.label_116.clear()

# mokab
# hajm
def hajm_mokab(self):
    try:
        inp = self.ui.lineEdit_29.text()
        inp = float(inp)
        result = inp**3
        self.ui.label_121.setText(str(result))
    except:
        messageBox = QMessageBox()
        messageBox.setText("لطفا شعاع را وارد کنید")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

def delete_all_mokab_hajm(self):
    self.ui.lineEdit_29.clear()
    self.ui.label_121.clear()

#masahat
def masahat_mokab(self):
    try:
        inp = self.ui.lineEdit_31.text()
        inp = float(inp)
        result = inp**2 * 6
        self.ui.label_132.setText(str(result))
    except:
        messageBox = QMessageBox()
        messageBox.setText("لطفا شعاع را وارد کنید")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

def delete_all_mokab_masahat(self):
    self.ui.lineEdit_31.clear()
    self.ui.label_132.clear()

#ostovane
#hajm
def hajm_ostovane(self):
    try:
        inp1 = self.ui.lineEdit_34.text()
        inp1 = float(inp1)
        inp2 = self.ui.lineEdit_35.text()
        inp2 = float(inp2)
        result = pi *inp1**2*inp2
        result = round(result,3)
        self.ui.label_135.setText(str(result))
    except:
        messageBox = QMessageBox()
        messageBox.setText("لطفا مغادیر را وارد نمایید")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()
def delete_all_ostovane_hajm(self):
    self.ui.lineEdit_34.clear()
    self.ui.lineEdit_35.clear()
    self.ui.label_135.clear()
    
#masaht
def masahat_ostovane(self):
    try:
        inp1 = self.ui.lineEdit_36.text()
        inp1 = float(inp1)
        inp2 = self.ui.lineEdit_37.text()
        inp2 = float(inp2)
        result = (2*pi*inp1**2) + (2*pi*inp1*inp2)
        result = round(result,3)
        self.ui.label_698.setText(str(result))
    except:
        messageBox = QMessageBox()
        messageBox.setText("لطفا مغادیر را وارد نمایید")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()
def delete_all_ostovane_masahat(self):
    self.ui.lineEdit_36.clear()
    self.ui.lineEdit_37.clear()
    self.ui.label_698.clear()
    

def etehad_moshtarak(self):
    try:
        x, y, z = sp.symbols('x y z')
        
        expr_str = self.ui.lineEdit_39.text()
        pattern = re.compile(r'(\d)([a-zA-Z])') 
        result = re.sub(pattern, r'\1*\2', expr_str) 
        result = result.replace("^","**")
        pattern = r"\)\s*\("
        replacement = ")*("
        result = re.sub(pattern, replacement, result)


        factored_expr = sp.factor(result)
        factored_expr = str(factored_expr)
        factored_expr = factored_expr.replace("**", "^")
        factored_expr = factored_expr.replace("*", "")
        

        expand_expr = sp.expand(result, x)
        expand_expr = str(expand_expr)
        expand_expr = expand_expr.replace("**", "^")
        expand_expr = expand_expr.replace("*", "")

        self.ui.label_157.setText(str(factored_expr))
        self.ui.label_158.setText(str(expand_expr))
    except:
        messageBox = QMessageBox()
        messageBox.setText("لطفا مغادیر را وارد نمایید")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()
        
def delete_jom(self):
        self.ui.label_157.clear()
        self.ui.label_158.clear()
        self.ui.lineEdit_39.clear()


def hendese(self,x):
    data = {"مثلث قایم زاویه" : ["مجموع 3 ظلع","قایده*ارتفاع*2","ندارد","ندارد","ندارد"],
            "مربع" : ["یک ضلع*4","یک ضلع*خودش","ندارد","2","4"],
            "لوزی" : ["یک ضلع*4","( قطر بزرگ * قطر کوچک )÷2","ندارد","2","2"],
            "مستطیل" : ["( طول + عرض)*2","طول * عرض","ندارد","2","2"],
            "ذوزنقه متساوی الساقین": [" مجموع چهار ضلع","(قاعده بزرگ + قاعده کوچک )*ارتفاع ÷ 2","ندارد","2","1"],
            "دایره" : ["3.14*قطر","شعاع*شعاع*3.14","ندارد","بی نهایت","بی نهایت"],
            "هرم" : ["ندارد","مساحت قاعده + 1/2 * (محیط قاعده * طول مایل)","1/3*(ارتفاع*مساحت قایده)","بپرس","بپرس"],
            "مکعب" : ["ندارد","یک ضلع * خودش * 6","طول*عرض*ارتفاع","ندارد","ندارد"],
            "استوانه" :["ندارد","(محیط قاعده×ارتفاع)+(مساحت قاعده×2)","مساحت قایده*ارتفاع","ندارد","ندارد"],
            "متواضی الضلاع" : ["(مجموع 2 ضلع متوالی)*2","قایده * ارتفاع","ندارد","2","ندارد"],
            "بیضی" : ["میانگین 2 شعاع*3.14*2","شعاع کوچک * شعاع بزرگ *2","ندارد","ندارد","ندارد"]
}
    res = data[x]
    mohit = res[0]
    masahat = res[1]
    hajm = res[2]
    ghotr = res[3]
    ghotr = str(ghotr)
    tagharon = res[4]
    tagharon = str(tagharon)


    moh = self.ui.label_207.setText(mohit)
    mas = self.ui.label_200.setText(masahat)
    haj = self.ui.label_206.setText(hajm)
    gho = self.ui.label_205.setText(ghotr)
    tagh = self.ui.label_204.setText(tagharon)





def abss(self):
    try:
        x = self.ui.lineEdit_6.text()
        x = x.split("|")
        del x[0]
        del x[-1]
        new_list = []
        if len(x)==1:
            for item in x:
                new_item = item.replace('√', 'sqrt')
                new_list.append(new_item)
            new_list = str(new_list)
            expression = re.sub(r'(\d)(sqrt)', r'\1*\2', new_list)
            result = re.sub(r'sqrt(\d+)', r'sqrt(\1)', expression)
            resulty = result.strip("[")
            resulty = resulty.strip("]")
            resulty = resulty.strip("'")
            result_sym = sympify(resulty)
            simplified_expr = simplify(Abs(result_sym))
            simplified_str = str(simplified_expr)
            simplified_str = simplified_str.replace('sqrt', '√')
            simplified_str = simplified_str.replace('*', '')
            simplified_str = simplified_str.replace('(', '')
            simplified_str = simplified_str.replace(')', '')
            self.ui.label_202.setText(simplified_str)
    except:
        messageBox = QMessageBox()
        messageBox.setText("لطفا مغادیر را وارد نمایید")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()
        
    if len(x) == 3:
        try:
            for item in x:
                new_item = item.replace('√', 'sqrt')
                new_list.append(new_item)
            inp1 = new_list[0]
            amal_gar = new_list[1]
            inp2 = new_list[2]
            inp1_s = str(inp1)
            inp2_s = str(inp2)
            inp1_ex = re.sub(r'(\d)(sqrt)', r'\1*\2', inp1_s)
            inp2_ex = re.sub(r'(\d)(sqrt)', r'\1*\2', inp2_s)
            inp1_res = re.sub(r'sqrt(\d+)', r'sqrt(\1)', inp1_ex)
            inp2_res = re.sub(r'sqrt(\d+)', r'sqrt(\1)', inp2_ex)
            inp1_res = sympify(inp1_res)
            inp2_res = sympify(inp2_res)
            ressss = f'Abs({inp1_res}){amal_gar}Abs({inp2_res})'
            ressss = sympify(ressss)
            simplified_expr = simplify(ressss)
            simplified_str = str(simplified_expr)
            simplified_str = simplified_str.replace('sqrt', '√')
            simplified_str = simplified_str.replace('*', '')
            simplified_str = simplified_str.replace('(', '')
            simplified_str = simplified_str.replace(')', '')
            self.ui.label_202.setText(simplified_str)
        except:
            pass
    if len(x) == 5:
        try:
            for item in x:
                new_item = item.replace('√', 'sqrt')
                new_list.append(new_item)
            inp11 = new_list[0]
            amal_gar1 = new_list[1]
            inp22 = new_list[2]
            amal_gar2 = new_list[3]
            inp33 = new_list[4]
            inp11_s = str(inp11)
            inp22_s = str(inp22)
            inp33_s = str(inp33)
            inp11_ex = re.sub(r'(\d)(sqrt)', r'\1*\2', inp11_s)
            inp22_ex = re.sub(r'(\d)(sqrt)', r'\1*\2', inp22_s)
            inp33_ex = re.sub(r'(\d)(sqrt)', r'\1*\2', inp33_s)
            inp11_res = re.sub(r'sqrt(\d+)', r'sqrt(\1)', inp11_ex)
            inp22_res = re.sub(r'sqrt(\d+)', r'sqrt(\1)', inp22_ex)
            inp33_res = re.sub(r'sqrt(\d+)', r'sqrt(\1)', inp33_ex)
            inp11_res = sympify(inp11_res)
            inp22_res = sympify(inp22_res)
            inp33_res = sympify(inp33_res)
            ress = f'Abs({inp11_res}){amal_gar1}Abs({inp22_res}){amal_gar2}Abs({inp33_res})'
            ress = sympify(ress)
            simplified_expr = simplify(ress)
            simplified_str = str(simplified_expr)
            simplified_str = simplified_str.replace('sqrt', '√')
            simplified_str = simplified_str.replace('*', '')
            simplified_str = simplified_str.replace('(', '')
            simplified_str = simplified_str.replace(')', '')
            self.ui.label_202.setText(simplified_str)
        except:
            pass
def delete_all_abs(self):
    self.ui.lineEdit_6.clear()
    self.ui.label_202.clear()


def mosalasat_sin(self):
    try:
        inp = self.ui.lineEdit_16.text()
        inp = float(inp)
        result = sin(inp)
        print(result)
        self.ui.label_213.setText(str(result))
    except:
        messageBox = QMessageBox()
        messageBox.setText("لطفا مغادیر را به درستی وارد نمایید")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()
def mosalasat_cos(self):
    try:
        inp = self.ui.lineEdit_47.text()
        inp = float(inp)
        result = cos(inp)
        self.ui.label_214.setText(str(result))
    except:
        messageBox = QMessageBox()
        messageBox.setText("لطفا مغادیر را به درستی وارد نمایید")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()
def mosalasat_tan(self):
    try:
        inp = self.ui.lineEdit_48.text()
        inp = float(inp)
        result = tan(inp)
        self.ui.label_215.setText(str(result))
    except:
        messageBox = QMessageBox()
        messageBox.setText("لطفا مغادیر را به درستی وارد نمایید")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

def delete_all_mosalas(self):
    self.ui.lineEdit_16.clear()
    self.ui.lineEdit_47.clear()
    self.ui.lineEdit_48.clear()
    self.ui.label_214.clear()
    self.ui.label_215.clear()
    self.ui.label_213.clear()



def moadele_yek(self):
    try:
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = sp.symbols('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sp.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
        inp = self.ui.lineEdit_49.text()
        letters = set(re.findall(r'[a-zA-Z]', inp))
        inp = inp.split("=")
        unknown = inp[0]
        anwser = inp[1]
        pattern = re.compile(r'(\d)([a-zA-Z])')
        result_un = re.sub(pattern, r'\1*\2',unknown)
        result_eq = sympify(result_un)
        result_anw = sympify(anwser)
        equation = Eq(result_eq,result_anw)
        result = sp.solve(equation,letters)
        result = str(result)
        result = result.replace("[","")
        result = result.replace("]","")
        letters = str(letters)
        letters = letters.replace("{","")
        letters = letters.replace("}","")
        letters = letters.replace("'","")
        result = f"{letters}:{result}"
        self.ui.label_218.setText(result)
    except:
        pass

def moadele_do(self):
    try:
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = sp.symbols('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sp.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
        eq1 = self.ui.lineEdit_50.text()
        eq2 = self.ui.lineEdit_51.text()
        pattern = re.compile(r'(\d)([a-zA-Z])')
        eq1 = re.sub(pattern, r'\1*\2',eq1)
        eq2 = re.sub(pattern, r'\1*\2',eq2)
        eq1 = eq1.split("=")
        eq2 = eq2.split("=")
        eq1_un = eq1[0]
        eq1_un = sympify(eq1_un)
        eq2_un = eq2[0]
        eq2_un = sympify(eq2_un)
        eq1_anw = eq1[1]
        eq1_anw = sympify(eq1_anw)
        eq2_anw = eq2[1]
        eq2_anw = sympify(eq2_anw)
        equation1 = Eq(eq1_un,eq1_anw)
        equation2 = Eq(eq2_un,eq2_anw)
        result = sp.solve((equation1,equation2),(x,y))
        result = str(result)
        result = result.replace("{","")
        result = result.replace("}","")
        self.ui.label_220.setText(result)
    except:
        pass

def delet_all_moadele(self):
    self.ui.lineEdit_50.clear()
    self.ui.lineEdit_49.clear()
    self.ui.lineEdit_51.clear()
    self.ui.label_220.clear()
    self.ui.label_218.clear()



def delete_all_moadele_marhale(self):
    self.ui.lineEdit_16.clear()
    self.ui.textEdit_3.clear() 



def mohasebe_moraba(self):
    try:
        inp = self.ui.lineEdit_107.text()
        result_mas = float(inp) * float(inp)
        result_moh = float(inp) * 4
        self.ui.label_181.setText(str(result_moh))
        self.ui.label_538.setText(str(result_mas))
    except:
        pass
def delete_all_mohase_mobara(self):
    self.ui.lineEdit_107.clear()
    self.ui.label_181.clear()
    self.ui.label_538.clear()

def mohasebe_mostatil(self):
    try:
        tol = self.ui.lineEdit_108.text()
        arz = self.ui.lineEdit_109.text()
        result_mas = float(tol) * float(arz)
        result_moh = (float(tol) + float(arz)) * 2
        self.ui.label_214.setText(str(result_mas))
        self.ui.label_216.setText(str(result_moh))
    except:
        pass
def delete_all_mohasebe_mosta(self):
    self.ui.lineEdit_108.clear()
    self.ui.lineEdit_109.clear()
    self.ui.label_214.clear()
    self.ui.label_216.clear()

def mohseb_mosalas(self):
    try:
        zel = self.ui.lineEdit_110.text()
        ertefa = self.ui.lineEdit_111.text()
        result_moh = float(zel) * 3
        result_mas = (float(ertefa)*float(zel)) /2
        self.ui.label_188.setText(str(result_moh))
        self.ui.label_190.setText(str(result_mas))
    except:
        pass
def delete_mohasebe_mosalas(self):
    self.ui.lineEdit_110.clear()
    self.ui.lineEdit_111.clear()
    self.ui.label_188.clear()
    self.ui.label_190.clear()  

def mohasebe_chand_zeli(self):
    try:
        inp = self.ui.lineEdit_112.text()
        inp = int(inp)
        zavie_khareki = 360 / inp
        zavie_dakheli = ((inp - 2 ) * 180) / inp
        zavie_dakheli_kol = ((inp - 2 ) * 180)
        ghotr = (inp * (inp - 3) )/ 2
        self.ui.label_268.setText(str(zavie_khareki))
        self.ui.label_265.setText(str(zavie_dakheli))
        self.ui.label_267.setText(str(zavie_dakheli_kol))
        self.ui.label_540.setText(str(ghotr))
    except:
        pass
def delete_mohasebe_chand_zeli(self):
    self.ui.lineEdit_112.clear()
    self.ui.label_268.clear()
    self.ui.label_265.clear()
    self.ui.label_267.clear()
    self.ui.label_540.clear()

def tajzie(self):
    try:
        inp1 = self.ui.lineEdit_55.text()
        inp2 = self.ui.lineEdit_54.text()
        inp1 = int(inp1)
        inp2 = int(inp2)
        list_smhrnde_aval1= []
        list_smhrnde_aval2= []
        listt1 = []
        listt2 = []
        for i in range(1, inp1+1):
            if (inp1 % i == 0):
                list_smhrnde_aval1.append(i)
        for i in range(1, inp2+1):
            if (inp2 % i == 0):
                list_smhrnde_aval2.append(i)
        list_smhrnde_aval1 = str(list_smhrnde_aval1)
        list_smhrnde_aval1 = list_smhrnde_aval1.replace("]",'')
        list_smhrnde_aval1 = list_smhrnde_aval1.replace("[",'')
        list_smhrnde_aval2 = str(list_smhrnde_aval2)
        list_smhrnde_aval2 = list_smhrnde_aval2.replace("]",'')
        list_smhrnde_aval2 = list_smhrnde_aval2.replace("[",'')
        self.ui.label_541.setText(str(list_smhrnde_aval1))
        self.ui.label_543.setText(str(list_smhrnde_aval2))
        for i in range(1,6):
            mazrab_inp1 = inp1 * i 
            listt1.append(mazrab_inp1)
        for i in range(1,6):
            mazrab_inp2 = inp2 * i 
            listt2.append(mazrab_inp2)
        listt1 = str(listt1)
        listt1 = listt1.replace("[","")
        listt1 = listt1.replace("]","")
        listt2 = str(listt2)
        listt2 = listt2.replace("[","")
        listt2 = listt2.replace("]","")
        self.ui.label_542.setText(listt1+",...")
        self.ui.label_544.setText(listt2+",...")
        def find_lcm(num1, num2):
            if num1 > num2:
                greater = num1
            else:
                greater = num2
            while True:
                if greater % num1 == 0 and greater % num2 == 0:
                    lcm = greater
                    break
                greater += 1
            return lcm
        B_M_M = find_lcm(inp1,inp2)
        K_M_M = math.gcd(inp1,inp2)
        self.ui.label_545.setText(str(B_M_M))
        self.ui.label_546.setText(str(K_M_M))
    except:
        pass
def delete_all_tajzie(self):
    self.ui.label_545.clear()
    self.ui.label_546.clear()
    self.ui.label_542.clear()
    self.ui.label_544.clear()  
    self.ui.label_541.clear()
    self.ui.label_543.clear()
    inp1 = self.ui.lineEdit_55.clear()
    inp2 = self.ui.lineEdit_54.clear()

# Darsad


def darsad_giri(self):
    results_message = ""

    try:
        # A az b
        if self.ui.lineEdit_66.text() and self.ui.lineEdit_63.text() != None:
            inp1 = self.ui.lineEdit_66.text()
            inp1 = float(inp1)
            inp2 = self.ui.lineEdit_63.text()
            inp2 = float(inp2)
            result_A_az_b = (inp1/100)*inp2
            
            # Check if the result is not NaN or Infinity
            if not math.isnan(result_A_az_b) and not math.isinf(result_A_az_b):
                results_message += f"{int(inp1)}درصد از {int(inp2)}برابر است با {int(result_A_az_b)}\n"
            else:
                results_message += "لطفاً مقادیر را به درستی وارد کنید\n"
    except:
        results_message += "لطفاً مقادیر را به درستی وارد کنید\n"

    try:
        # a chand darsad b hast
        if self.ui.lineEdit_65.text() and self.ui.lineEdit_62.text() != None:
            x1 = self.ui.lineEdit_65.text()
            x1 = float(x1)
            x2 = self.ui.lineEdit_62.text()
            x2 = float(x2)
            result_a_chand_b = (x1/x2)*100
            
            # Check if the result is not NaN or Infinity
            if not math.isnan(result_a_chand_b) and not math.isinf(result_a_chand_b):
                results_message += f"{int(x1)}برابر است با %{int(result_a_chand_b)} عدد {int(x2)}\n"
            else:
                results_message += "لطفاً مقادیر را به درستی وارد کنید\n"
    except:
        results_message += "لطفاً مقادیر را به درستی وارد کنید\n"

    try:
        # taghirat a az b
        if self.ui.lineEdit_64.text() and self.ui.lineEdit_61.text() != None:
            y1 = float(self.ui.lineEdit_64.text())
            y2 = float(self.ui.lineEdit_61.text())
            result_a_taghirat_b = ((y2-y1)/y1)*100
            
            # Check if the result is not NaN or Infinity
            if not math.isnan(result_a_taghirat_b) and not math.isinf(result_a_taghirat_b):
                results_message += f"درصد تغییر از {int(y1)}به {int(y2)}برابر است با %{int(result_a_taghirat_b)}\n"
            else:
                results_message += "لطفاً مقادیر را به درستی وارد کنید\n"
    except:
        results_message += "لطفاً مقادیر را به درستی وارد کنید\n"

    messagebox = QMessageBox()
    messagebox.setText(results_message)
    messagebox.setStandardButtons(QMessageBox.Ok)
    messagebox.exec()
    self.ui.lineEdit_66.clear()
    self.ui.lineEdit_63.clear()
    self.ui.lineEdit_65.clear()
    self.ui.lineEdit_62.clear()
    self.ui.lineEdit_64.clear()
    self.ui.lineEdit_61.clear()
    






