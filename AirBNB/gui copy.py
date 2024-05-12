# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guicDNBQp.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PyQt5 import QtWidgets
from PySide6 import QtWidgets
import PySide6.QtWidgets as qw



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 900)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 30, 921, 61))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"font: 700 30pt \"Arial\";\n"
"color: rgb(255, 90, 95);\n"
"")
        self.label_2.setTextFormat(Qt.RichText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 120, 790, 340))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 166, 153);\n"
"background-color: rgb(0, 166, 153);")
        self.groupBox.setFlat(False)
        self.buton_citire = QPushButton(self.groupBox)
        self.buton_citire.setObjectName(u"buton_citire")
        self.buton_citire.setGeometry(QRect(10, 40, 141, 41))
        self.buton_citire.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 0, 0);\n"
"font: 700 12pt \"Times New Roman\";\n"
"color: rgb(255, 90, 95);")
        icon = QIcon()
        self.buton_citire.setIcon(icon)
        self.buton_citire.setIconSize(QSize(26, 26))
        self.buton_citire.setAutoExclusive(True)
        self.buton_citire.setAutoDefault(False)
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 100, 451, 201))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setScaledContents(True)
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)
        self.variabila_index = QComboBox(self.formLayoutWidget)
        self.variabila_index.setObjectName(u"variabila_index")
        self.variabila_index.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.variabila_index.setIconSize(QSize(20, 20))
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.variabila_index)
        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)
        self.checkBox = QCheckBox(self.formLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(11)
        self.checkBox.setFont(font3)
        self.checkBox.setTristate(False)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.checkBox)
        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(37, 200, 120, 16))
        self.label_11.setFont(font2)
        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit)
        self.variabila_hist = QComboBox(self.formLayoutWidget)
        self.variabila_hist.setObjectName(u"variabila_hist")
        self.variabila_hist.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.variabila_hist)
        self.lista_selectie_variabile = QListWidget(self.formLayoutWidget)
        self.lista_selectie_variabile.setObjectName(u"lista_selectie_variabile")
        self.lista_selectie_variabile.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lista_selectie_variabile)
        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(470, 90, 300, 150))
        self.groupBox_3.setFont(font2)
        self.buton_partitie_kmeans = QPushButton(self.groupBox_3)
        self.buton_partitie_kmeans.setObjectName(u"buton_partitie_kmeans")
        self.buton_partitie_kmeans.setEnabled(True)
        self.buton_partitie_kmeans.setGeometry(QRect(10, 60, 100, 31))
        self.buton_partitie_kmeans.setFont(font2)
        self.buton_partitie_kmeans.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 90, 95);")
        self.buton_partitie_kmeans.setIconSize(QSize(26, 26))
        self.buton_partitie_kmeans.setAutoDefault(False)
        self.buton_plot_kmeans = QPushButton(self.groupBox_3)
        self.buton_plot_kmeans.setObjectName(u"buton_plot_kmeans")
        self.buton_plot_kmeans.setGeometry(QRect(140, 90, 131, 31))
        self.buton_plot_kmeans.setFont(font2)
        self.buton_plot_kmeans.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 90, 95);")
        self.buton_plot_kmeans.setIconSize(QSize(26, 26))
        self.buton_plot_kmeans.setAutoDefault(False)
        self.buton_kmeans_medii = QPushButton(self.groupBox_3)
        self.buton_kmeans_medii.setObjectName(u"buton_kmeans_medii")
        self.buton_kmeans_medii.setEnabled(True)
        self.buton_kmeans_medii.setGeometry(QRect(10, 110, 100, 31))
        self.buton_kmeans_medii.setFont(font2)
        self.buton_kmeans_medii.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 90, 95);")
        self.buton_kmeans_medii.setIconSize(QSize(26, 26))
        self.buton_kmeans_medii.setAutoDefault(False)
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(890, 90, 300, 150))
        self.groupBox_4.setFont(font2)
        self.buton_sumarizare = QPushButton(self.groupBox)
        self.buton_sumarizare.setObjectName(u"buton_sumarizare")
        self.buton_sumarizare.setGeometry(QRect(520, 40, 161, 31))
        self.buton_sumarizare.setFont(font2)
        self.buton_sumarizare.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 90, 95);")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(830, 120, 750, 340))
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 90, 95);\n"
"color: rgb(255, 255, 255);")
        self.buton_citire_antrenare = QPushButton(self.groupBox_2)
        self.buton_citire_antrenare.setObjectName(u"buton_citire_antrenare")
        self.buton_citire_antrenare.setGeometry(QRect(10, 30, 181, 41))
        self.buton_citire_antrenare.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 0, 0);\n"
"font: 700 12pt \"Times New Roman\";\n"
"color: rgb(0, 166, 153);")
        self.buton_citire_antrenare.setIcon(icon)
        self.buton_citire_antrenare.setIconSize(QSize(26, 26))
        self.buton_citire_antrenare.setAutoExclusive(True)
        self.buton_citire_antrenare.setAutoDefault(False)
        self.buton_citire_testare = QPushButton(self.groupBox_2)
        self.buton_citire_testare.setObjectName(u"buton_citire_testare")
        self.buton_citire_testare.setGeometry(QRect(10, 80, 181, 41))
        self.buton_citire_testare.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 0, 0);\n"
"font: 700 12pt \"Times New Roman\";\n"
"color: rgb(0, 166, 153);")
        self.buton_citire_testare.setIcon(icon)
        self.buton_citire_testare.setIconSize(QSize(26, 26))
        self.buton_citire_testare.setAutoExclusive(True)
        self.buton_citire_testare.setAutoDefault(False)
        self.cale_antrenare = QLineEdit(self.groupBox_2)
        self.cale_antrenare.setObjectName(u"cale_antrenare")
        self.cale_antrenare.setGeometry(QRect(200, 40, 191, 21))
        self.cale_antrenare.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 90, 95);")
        self.cale_testare = QLineEdit(self.groupBox_2)
        self.cale_testare.setObjectName(u"cale_testare")
        self.cale_testare.setGeometry(QRect(200, 90, 191, 21))
        self.cale_testare.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 90, 95);")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 140, 151, 16))
        self.label.setFont(font2)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 180, 151, 16))
        self.label_8.setFont(font2)
        self.combo_index = QComboBox(self.groupBox_2)
        self.combo_index.setObjectName(u"combo_index")
        self.combo_index.setGeometry(QRect(200, 140, 191, 22))
        self.combo_index.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.combo_tinta = QComboBox(self.groupBox_2)
        self.combo_tinta.setObjectName(u"combo_tinta")
        self.combo_tinta.setGeometry(QRect(200, 180, 191, 22))
        self.combo_tinta.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 220, 120, 16))
        self.label_9.setFont(font2)
        self.lista_predictori = QListWidget(self.groupBox_2)
        self.lista_predictori.setObjectName(u"lista_predictori")
        self.lista_predictori.setGeometry(QRect(200, 220, 191, 111))
        self.lista_predictori.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(410, 30, 271, 241))
        self.groupBox_5.setFont(font2)
        self.buton_metrici_liniar = QPushButton(self.groupBox_5)
        self.buton_metrici_liniar.setObjectName(u"buton_metrici_liniar")
        self.buton_metrici_liniar.setGeometry(QRect(10, 70, 111, 31))
        self.buton_metrici_liniar.setFont(font2)
        self.buton_metrici_liniar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.buton_coeficienti_liniar = QPushButton(self.groupBox_5)
        self.buton_coeficienti_liniar.setObjectName(u"buton_coeficienti_liniar")
        self.buton_coeficienti_liniar.setGeometry(QRect(10, 110, 111, 31))
        self.buton_coeficienti_liniar.setFont(font2)
        self.buton_coeficienti_liniar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.buton_predictie_liniar = QPushButton(self.groupBox_5)
        self.buton_predictie_liniar.setObjectName(u"buton_predictie_liniar")
        self.buton_predictie_liniar.setGeometry(QRect(10, 150, 111, 31))
        self.buton_predictie_liniar.setFont(font2)
        self.buton_predictie_liniar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.buton_plot_predictii_liniar = QPushButton(self.groupBox_5)
        self.buton_plot_predictii_liniar.setObjectName(u"buton_plot_predictii_liniar")
        self.buton_plot_predictii_liniar.setGeometry(QRect(140, 110, 111, 31))
        self.buton_plot_predictii_liniar.setFont(font2)
        self.buton_plot_predictii_liniar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.buton_heatmap_liniar = QPushButton(self.groupBox_5)
        self.buton_heatmap_liniar.setObjectName(u"buton_heatmap_liniar")
        self.buton_heatmap_liniar.setGeometry(QRect(140, 70, 111, 31))
        self.buton_heatmap_liniar.setFont(font2)
        self.buton_heatmap_liniar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.buton_qqplot_lin = QPushButton(self.groupBox_5)
        self.buton_qqplot_lin.setObjectName(u"buton_qqplot_lin")
        self.buton_qqplot_lin.setGeometry(QRect(140, 150, 111, 31))
        self.buton_qqplot_lin.setFont(font2)
        self.buton_qqplot_lin.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 166, 153);")
        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(710, 30, 261, 241))
        self.groupBox_6.setFont(font2)
        self.label_23 = QLabel(self.groupBox_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(50, 30, 31, 31))
        self.label_23.setPixmap(QPixmap(u"icons/csv.png"))
        self.label_23.setScaledContents(True)
        self.label_25 = QLabel(self.groupBox_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(170, 30, 31, 31))
        self.label_25.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1422, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.buton_citire.setDefault(False)
        self.buton_citire_antrenare.setDefault(False)
        self.buton_citire_testare.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Analiza pre\u021burilor locuin\u021belor Airbnb", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Analiza de clusterizare", None))
        self.buton_citire.setText(QCoreApplication.translate("MainWindow", u"Citire date", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Variabil\u0103 index", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Selec\u021bie variabile ", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Selectare toate", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Num\u0103r clusteri", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Variabile clusterizare", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"K-Means", None))
        self.buton_partitie_kmeans.setText(QCoreApplication.translate("MainWindow", u"Parti\u021bie", None))
        self.buton_plot_kmeans.setText(QCoreApplication.translate("MainWindow", u"Plot parti\u021bie", None))
        self.buton_kmeans_medii.setText(QCoreApplication.translate("MainWindow", u"Centre de greutate", None))
        self.buton_sumarizare.setText(QCoreApplication.translate("MainWindow", u"Statistici descriptive", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Modelul de regresie liniar\u0103", None))
        self.buton_citire_antrenare.setText(QCoreApplication.translate("MainWindow", u"Set de antrenare", None))
        self.buton_citire_testare.setText(QCoreApplication.translate("MainWindow", u" Set de testare", None))
        self.cale_antrenare.setText("")
        self.cale_testare.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Variabil\u0103 index", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Variabil\u0103 dependent\u0103", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Variabile independente", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Modelul liniar", None))
        self.buton_metrici_liniar.setText(QCoreApplication.translate("MainWindow", u"Metrici", None))
        self.buton_coeficienti_liniar.setText(QCoreApplication.translate("MainWindow", u"Coeficien\u021bi", None))
        self.buton_predictie_liniar.setText(QCoreApplication.translate("MainWindow", u"Predic\u021bie", None))
        self.buton_plot_predictii_liniar.setText(QCoreApplication.translate("MainWindow", u"Plot predic\u021bii", None))
        self.buton_heatmap_liniar.setText(QCoreApplication.translate("MainWindow", u"Heatmap", None))
        self.buton_qqplot_lin.setText(QCoreApplication.translate("MainWindow", u"QQ-plot", None))
    # retranslateUi

class ModelTabel(QAbstractTableModel):
    # Primeste un pandas DataFrame
    def __init__(self, data):
        super(ModelTabel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            coloana = index.column()
            linia = index.row()
            valoare = self._data.iloc[linia, coloana]
            return str(valoare)

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data.columns)

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

# Clasa de tip tabel
class Tabel(QtWidgets.QTableView):
    def __init__(self, data):
        QtWidgets.QTableView.__init__(self)
        self.horizontalHeader().setSectionResizeMode(
            qw.QHeaderView.ResizeToContents
        )
        self.verticalHeader().setSectionResizeMode(
            qw.QHeaderView.ResizeToContents
        )
        # self.horizontalHeader().setStretchLastSection(True) #Forteaza dimensiunea ultimei coloane
        size = qw.QSizePolicy(qw.QSizePolicy.Preferred, qw.QSizePolicy.Preferred)
        size.setHorizontalStretch(1)
        self.setSizePolicy(size)
        # Ii stabilesc modelul de data
        self.setModel(ModelTabel(data=data))
        self.setFixedSize(700, 400)

# Panelul de continut. Primeste un gestionar de pozitionare. In acesta pun totul
class Panel(qw.QWidget):
    def __init__(self, gestionar_pozitionare):
        qw.QWidget.__init__(self)
        self.main_layout = gestionar_pozitionare
        self.setLayout(self.main_layout)

# Clasa generalizare buton
class Buton(qw.QPushButton):
    def __init__(self, text, w, h, stil=None, click=None):
        qw.QPushButton.__init__(self, text)
        self.setFixedHeight(h)
        self.setFixedWidth(w)
        if stil is not None:
            self.setStyleSheet(stil)
        if click is not None:
            self.clicked.connect(click)

# Clasa generalizare eticheta
class Eticheta(qw.QLabel):
    def __init__(self, text, w=None, h=None, stil=None):
        qw.QLabel.__init__(self, text)
        if w is not None:
            self.setFixedWidth(w)
        if h is not None:
            self.setFixedHeight(h)
        if stil is not None:
            self.setStyleSheet(stil)

# Clasa generalizare text field
class TextField(qw.QLineEdit):
    def __init__(self, text, w=None, h=None, stil=None):
        qw.QLineEdit.__init__(self, text)
        if w is not None:
            self.setFixedWidth(w)
        if h is not None:
            self.setFixedHeight(h)
        if stil is not None:
            self.setStyleSheet(stil)


class DialogNonModal(QDialog):
    def __init__(self, parent, t, w=700, h=500, titlu="Tabel"):
        QDialog.__init__(self, parent)
        self.setModal(0)

        tabel = QTableView()
        model = ModelTabel(data=t)
        tabel.setModel(model)
        tabel.setFixedSize(w, h)
        layout1 = QHBoxLayout()
        layout1.addWidget(tabel)
        self.setLayout(layout1)
        self.setWindowTitle(titlu)
