import sys
import string
from itertools import product
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt

sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = my_exception_hook

list_sorted = []
listk = []
i = 0
i2 = 0


class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.ui.textEdit.setText("Нажмите кнопку \"Следующая версия ->\" чтобы увидеть расшифровку")
        self.window.show()

    def myFunction_3(self):
        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 781, 181))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 270, 781, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 151, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 240, 131, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 310, 141, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 330, 781, 181))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 520, 781, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 550, 781, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Первичные данные"))
        self.pushButton.setText(_translate("MainWindow", "Зашифровать"))
        self.label_2.setText(_translate("MainWindow", "Ключ (от 2 до 5 символов)"))
        self.label_3.setText(_translate("MainWindow", "Зашифрованные данные"))
        self.pushButton_2.setText(_translate("MainWindow", "Расшифровать методом ИС"))
        self.pushButton_3.setText(_translate("MainWindow", "Расшифровать методом Казиски"))


class Ui_OtherWindow(object):
    def prevv(self):
        global i
        global i2
        if i != 0: i -= 1
        self.textEdit.setText(list_sorted[i])
        i2 = i

    def nextt(self):
        global i
        global i2
        self.textEdit.setText(list_sorted[i])
        i2 = i
        i += 1
        print(i)

    def okk(self):
        global i2
        self.lineEdit_2.setText(listk[i2])



    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(812, 428)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 791, 181))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 220, 131, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 250, 261, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.prevv)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 250, 231, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.okk)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 250, 261, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.nextt)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 111, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 300, 131, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 21))
        self.menubar.setObjectName("menubar")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)
        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "OtherWindow"))
        self.label.setText(_translate("OtherWindow", "Это правильный текст?"))
        self.pushButton.setText(_translate("OtherWindow", "<- Предыдущая версия"))
        self.pushButton_2.setText(_translate("OtherWindow", "Да"))
        self.pushButton_3.setText(_translate("OtherWindow", "Следующая версия ->"))
        self.label_2.setText(_translate("OtherWindow", "Расшифрованная версия текста"))
        self.label_3.setText(_translate("OtherWindow", "Возможный ключ"))


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.MyFunction)
        self.ui.pushButton_2.clicked.connect(self.MyFunction_2)
        self.ui.pushButton_3.clicked.connect(self.MyFunction_3)

    def MyFunction(self):
        self.ui.textEdit_2.setText("")
        e = self.ui.textEdit.toPlainText()
        clearstring = ''.join(c for c in e.lower() if c in string.ascii_lowercase)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        key = self.ui.lineEdit.text()
        key_len = len(key)
        key_as_int = [alphabet.index(i) for i in key]
        word_as_int = [alphabet.index(i) for i in clearstring]
        cipher = ''
        for i in range(len(word_as_int)):
            value = (word_as_int[i] + key_as_int[i % key_len]) % 26
            cipher += alphabet[value]
        self.ui.textEdit_2.setText(cipher)

    def MyFunction_2(self):
        del list_sorted[:]
        del listk[:]
        global i
        global i2
        global list_divided
        i = 0
        i2 = 0
        self.ui.openWindow()
        cipher = self.ui.textEdit_2.toPlainText()
        c = [i for i in range(2, 6, 1)]
        list2 = ic_get_list_cisum(cipher, c)
        key_len2 = ic_know_key_length(list2)
        complete_decrypting(key_len2, cipher)

    def MyFunction_3(self):
        del list_sorted[:]
        del listk[:]
        global i
        global i2
        i = 0
        i2 = 0
        self.ui.openWindow()
        cipher = self.ui.textEdit_2.toPlainText()
        key_len = find_key_length(cipher, 4, 5)
        complete_decrypting(key_len, cipher)


def find_key_length(a, b, c):
    rsp = repeated_seq_pos(a=a, b=b)
    seq_spc = {}
    for seq, positions in rsp:
        seq_spc[seq] = get_spacings(positions)
        print(seq_spc[seq])
    factor_lists = []
    for spacings in seq_spc.values():
        for space in spacings:
            factor_lists.append(get_factors(a=space))
    print(factor_lists)
    print(len(factor_lists))
    ckl = candidate_key_lengths(a=factor_lists, b=c)
    key_len = ckl[1]
    return key_len


def candidate_key_lengths(a, b):
    all_factors = [a[lst][fac] for lst in range(len(a)) for fac in range(len(a[lst]))]
    candidate_lengths = list(filter(lambda x: x <= b, all_factors))
    sorted_candidates = sorted(set(candidate_lengths), key=lambda x: all_factors.count(x), reverse=True)
    return sorted_candidates


def repeated_seq_pos(a, b):
    seq_pos = {}
    for i, char in enumerate(a):
        next_seq = a[i:i + b]
        print(next_seq)
        if next_seq in seq_pos.keys():
            seq_pos[next_seq].append(i)
            print(i)
        else:
            seq_pos[next_seq] = [i]
    repeated = list(filter(lambda x: len(seq_pos[x]) >= 2, seq_pos))
    print(repeated)
    rep_seq_pos = [(seq, seq_pos[seq]) for seq in repeated]
    print(rep_seq_pos)
    return rep_seq_pos


def get_factors(a):
    factors = set()
    for i in range(1, int(sqrt(a)) + 1):
        if a % i == 0:
            factors.add(i)
            factors.add(a // i)
    return sorted(factors)


def get_spacings(a):
    return [a[i + 1] - a[i] for i in range(len(a) - 1)]


def ic_know_key_length(a):
    s = 0
    b = 0.0667
    minn = 100
    for i in range(len(a)):
        ee = abs(a[i] - b)
        if (minn > ee):
            minn = ee
            s = i + 2
    return s


def form_alph():
    alph = []
    for i in range(26):
        alph.append(chr(ord('a') + i))

    return alph


def precombine(a, s):
    b = np.array(a)
    c = np.transpose(b)
    listt = []
    for i in product(*c):
        lisst = list(i)

        lissst = combine(lisst, s)
        listt.append(''.join(lissst))
    return listt


def form_alph():
    alph = []
    for i in range(26):
        alph.append(chr(ord('a') + i))

    return alph


def combine(a, s):
    list_final = []
    list_final2 = []
    for i in range(len(''.join(a))):
        list_final.append(0)
    for e in range(len(a)):
        r = 0
        for i in a[e]:
            list_final[r * s + e] = i
            r += 1
    strr = ''.join(str(i) for i in list_final)
    list_final2.append(strr)
    return list_final2


def get_list_decrypted(a, b, h):
    list_letters = ['e', 't', 'a', 'o', 'i', 'n']
    list_good2 = []
    for k in list_letters:
        list_good = []
        for q in range(len(a)):
            str_temp = ""
            for i in a[q]:
                razn = b.index(h[q]) - b.index(k)
                sm = b.index(i) - razn
                if (26 > sm >= 0):
                    str_temp = str_temp + b[b.index(i) - razn]
                if (sm < 0):
                    str_temp = str_temp + b[len(b) + (b.index(i) - razn)]
                if (sm > 25):
                    str_temp = str_temp + b[sm - 26]
            list_good.append(str_temp)
        list_good2.append(list_good)
    return list_good2


def divide_by_key_length(s, a):
    t = 0
    list_shifrov = []
    list_tmp = []
    while (t < len(a)):
        strd = ""
        iss = 0
        while (t + s * iss < len(a)):
            if (t + s * iss not in list_tmp):
                strd = strd + a[t + s * iss]
                list_tmp.append(t + s * iss)
                iss = iss + 1
            else:
                iss = iss + 1
        if (strd != ""):
            list_shifrov.append(strd)
        t = t + 1
    print(list_shifrov)
    return list_shifrov


def most_popular_letter(a):
    h = []
    for i in range(len(a)):
        gg = dict.fromkeys(a[i], 0)
        for ii in a[i]:
            gg[ii] += 1
        u = 0
        max_str = ''
        for iiii in gg:

            if gg[iiii] > u:
                u = gg[iiii]
                max_str = iiii
        h.append(max_str)
        print(max_str)

    return h


def ic_get_list_cisum(a, b):
    c2 = []
    for ii in b:
        st = ""
        t = 0
        while (t < len(a)):
            st = st + a[t]
            t += ii

        d = dict.fromkeys(st, 0)
        for i in st:
            d[i] += 1

        d2 = dict.fromkeys(st, 0)
        for i in d:
            d2[i] = (d[i] * (d[i] - 1)) / (len(st) * (len(st) - 1))

        summ = 0
        for i in d2:
            summ = summ + d2[i]
        c2.append(summ)

    return c2


def complete_decrypting(a, b):
    list3 = divide_by_key_length(a, b)
    list4 = most_popular_letter(list3)
    alph = form_alph()
    list5 = get_list_decrypted(list3, alph, list4)
    list6 = precombine(list5, a)
    popular_words = ['the', 'be', 'to', 'of', 'and', 'in', 'that', 'have', 'it', 'for']
    for i in list6:
        kk = 0
        for n in popular_words:
            if n in i:
                kk += 1
        if kk < 3: list6.remove(i)
    listg = []
    for i in list6:
        m = 0
        for bb in popular_words:
            m += i.count(bb)
        listg.append(m)
    for i in list6:
        r = listg.index(max(listg))
        list_sorted.append(list6[r])
        listg[r] = 0
    print(len(list_sorted))
    for i in range(len(list_sorted)):
        lisd = []
        for e in range(len(b)):
            g = alph.index(b[e]) % 26 - alph.index(list_sorted[i][e]) % 26
            if g < 0:
                lisd.append(26 + g)
            else:
                lisd.append(g)
        strr = ''
        for i in lisd:
            strr += alph[i]
        listk.append(strr[:a])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")


