import PySide6.QtWidgets as qw
from gui import *
import gui
import pandas as pd
import numpy as np
from PySide6.QtCore import Qt
import sklearn.cluster as cluster
import sklearn.decomposition as fe
from scipy import stats
from sklearn import metrics
from sklearn.linear_model import LinearRegression
import grafice
import functii



class frame(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(frame, self).__init__()
        self.setupUi(self)
        #clusterizare
        self.sumarizare=False
        self.model_creat = False
        self.model_km_creat = False
        self.variabile_selectate = []
        self.tabel_date = None
        self.directorCurent = "."
        self.buton_citire.clicked.connect(self.citire_set)
        self.checkBox.stateChanged.connect(self.selectie_toate_variabilele)
        self.lineEdit.textChanged.connect(self.invalidare_modele)
        self.buton_partitie_kmeans.clicked.connect(self.kM_afisare_partitie)
        self.buton_kmeans_medii.clicked.connect(self.km_afisare_means)
        self.buton_plot_kmeans.clicked.connect(self.plot_partitie)
        self.buton_sumarizare.clicked.connect(self.sumarizare_afisare)

        #regresie
       # self.directorCurent = "."
        self.variabile_selectate = []
        self.tabel_date1 = None
        self.tabel_date_testare = None
        self.date_citite = False
        self.model_creat = False
        self.buton_citire_antrenare.clicked.connect(self.citire_antrenare)
        self.buton_citire_testare.clicked.connect(self.citire_testare)
        self.buton_metrici_liniar.clicked.connect(self.metrici_liniar)
        self.buton_coeficienti_liniar.clicked.connect(self.coeficienti_liniar)
        self.buton_predictie_liniar.clicked.connect(self.predictie_liniar)
        self.buton_heatmap_liniar.clicked.connect(self.plot_heatmap)
        self.buton_plot_predictii_liniar.clicked.connect(self.plot_predictii_liniar)
        self.buton_qqplot_lin.clicked.connect(self.plot_qqplot_lin)

#Clustering
    def invalidare_modele(self):
        self.model_km_creat = False

    def citire_set(self):
        dialog = qw.QFileDialog(directory=".")
        dialog.setFileMode(qw.QFileDialog.AnyFile)
        dialog.setNameFilter("Fisier date (*.csv)")
        dialog.setViewMode(qw.QFileDialog.Detail)
        fileNames = []
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        if len(fileNames) == 0:
            return
        self.fisier = fileNames[0]
        self.tabel_date = pd.read_csv(self.fisier)
        self.n = len(self.tabel_date)
        variabile = list(self.tabel_date)
        self.lista_selectie_variabile.clear()
        self.variabila_index.clear()
        for v in variabile:
            # self.l_variabile_selectate.addItem(qw.QListWidgetItem(v))
            # Se instantiaza un item si se indica prin parametru lista la care va fi adaugat
            item = qw.QListWidgetItem(self.lista_selectie_variabile)
            ch = qw.QCheckBox(v)
            # Inregistrare semnal de schimbare stare
            ch.stateChanged.connect(self.selectie_variabila)
            self.lista_selectie_variabile.setItemWidget(item, ch)
            self.variabila_index.addItem(v)

    def selectie_variabila(self):
        self.variabila_hist.clear()
        n_sel = 0
        for i in range(self.lista_selectie_variabile.count()):
            item = self.lista_selectie_variabile.item(i)
            ch_variabila = self.lista_selectie_variabile.itemWidget(item)
            if ch_variabila.isChecked():
                self.variabila_hist.addItem(ch_variabila.text())
                n_sel = n_sel + 1

    def selectie_toate_variabilele(self):
        flag = self.checkBox.isChecked()
        for i in range(self.lista_selectie_variabile.count()):
            item = self.lista_selectie_variabile.item(i)
            self.lista_selectie_variabile.itemWidget(item).setChecked(flag)
        self.model_creat = False

    def creare_sumarizare(self):
        if self.tabel_date is None:
            msgBox = qw.QMessageBox()
            msgBox.setText("Nu au fost citite datele!")
            msgBox.exec()
            return
        self.variabile_selectate.clear()
        for i in range(self.lista_selectie_variabile.count()):
            item = self.lista_selectie_variabile.item(i)
            checkItem = self.lista_selectie_variabile.itemWidget(item)
            if checkItem.isChecked():
                self.variabile_selectate.append(checkItem.text())
        self.coloana_index = self.variabila_index.currentText()
        self.tabel_date.index = [str(v) for v in self.tabel_date[self.coloana_index]]
        self.nume_instante = self.tabel_date[self.coloana_index]
        self.m = len(self.variabile_selectate)
        t = self.tabel_date[self.variabile_selectate]
        self.x = t.values
        describe = t.describe()
        self.df2 = pd.DataFrame(describe, columns=self.variabile_selectate)
        self.sumarizare=True

    def sumarizare_afisare(self):
        if self.sumarizare is False:
            self.creare_sumarizare()
        if self.sumarizare:
            tabel = gui.Tabel(self.df2)
            self.df2.to_csv("OUT_Cluster/statistici_descriptive.csv")
            layout1 = qw.QHBoxLayout()
            layout1.addWidget(tabel)
            dialog = qw.QDialog()
            dialog.setWindowTitle("Statistici descriptive")
            dialog.setLayout(layout1)
            dialog.setModal(True)
            dialog.exec()

    def creare_model_km(self):
        if self.tabel_date is None:
            msgBox = qw.QMessageBox()
            msgBox.setText("Nu au fost citite datele!")
            msgBox.exec()
            return
        self.variabile_selectate.clear()
        for i in range(self.lista_selectie_variabile.count()):
            item = self.lista_selectie_variabile.item(i)
            checkItem = self.lista_selectie_variabile.itemWidget(item)
            if checkItem.isChecked():
                self.variabile_selectate.append(checkItem.text())
        self.coloana_index = self.variabila_index.currentText()
        self.tabel_date.index = [str(v) for v in self.tabel_date[self.coloana_index]]
        self.nume_instante = self.tabel_date[self.coloana_index]
        self.m = len(self.variabile_selectate)
        if self.m < 2:
            msgBox = qw.QMessageBox()
            msgBox.setText("Prea putine variabile selectate!")
            msgBox.exec()
            return
        t = self.tabel_date[self.variabile_selectate]
        self.x = t.values
        self.k = int(self.lineEdit.text())
        km = cluster.KMeans(n_clusters=self.k)
        km.fit_predict(self.x)
        cluster_means = km.cluster_centers_
        self.df = pd.DataFrame(cluster_means, columns=self.variabile_selectate)
        self.df.insert(0, "Cluster", ["Cluster " + str(i + 1) for i in range(km.n_clusters)], True)
        self.clustere = ["c" + str(i) for i in km.labels_]
        self.partitie_km = pd.DataFrame(index=t.index)
        self.partitie_km.index.name = self.variabila_index.currentText()
        self.partitie_km["Cluster"] = self.clustere
        self.model_km_creat = True

    def kM_afisare_partitie(self):
        if self.model_km_creat is False:
            self.creare_model_km()
        if self.model_km_creat:
            tabel = gui.Tabel(self.partitie_km)
            self.partitie_km.to_csv("OUT_Cluster/kMeans_p" + str(self.k) + ".csv")
            layout1 = qw.QHBoxLayout()
            layout1.addWidget(tabel)
            dialog = qw.QDialog()
            dialog.setWindowTitle("Partitia KM")
            dialog.setLayout(layout1)
            dialog.setModal(True)
            dialog.exec()

    def km_afisare_means(self):
        if self.model_km_creat is False:
            self.creare_model_km()
        if self.model_km_creat:
            tabel = gui.Tabel(self.df)
            self.df.to_csv("OUT_Cluster/km_means" + str(self.k) + ".csv")
            layout1 = qw.QHBoxLayout()
            layout1.addWidget(tabel)
            dialog = qw.QDialog()
            dialog.setWindowTitle("Cluster Means")
            dialog.setLayout(layout1)
            dialog.setModal(True)
            dialog.exec()


    def plot_partitie(self):
        if self.model_km_creat is False:
            self.creare_model_km()
        if self.model_km_creat:
            grupe = list(set(self.clustere))
            etichete = None
            n, m = np.shape(self.x)
            if n < 2000:
                etichete = self.nume_instante
            if m == 2:
                grafice.plot_clustere(self.x[:, 0], self.x[:, 1], self.clustere, grupe, etichete=etichete,
                                      titlu='KM. Axe principale. Partitia din ' + str(self.k) + " clustere",
                                      fisier="km_p" + str(self.k))
            else:
                c = functii.acp(self.x)
                grafice.plot_clustere(c[:, 0], c[:, 1], self.clustere, grupe, etichete=etichete,
                                      titlu='KM. Axe principale. Partitia din ' + str(self.k) + " clustere",
                                      fisier="km_p" + str(self.k))
            grafice.show()

#Regresie

    def citire_antrenare(self):
        dialog = qw.QFileDialog(directory=self.directorCurent)
        dialog.setFileMode(qw.QFileDialog.AnyFile)
        dialog.setNameFilter("Fisier date (*.csv)")
        dialog.setViewMode(qw.QFileDialog.Detail)
        fileNames = []
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        if len(fileNames) == 0:
            return
        self.fisier = fileNames[0]
        self.tabel_date1 = pd.read_csv(self.fisier)
        self.cale_antrenare.setText(self.fisier)
        variabile = list(self.tabel_date1)
        self.lista_predictori.clear()
        self.combo_index.clear()
        self.combo_tinta.clear()
        for v in variabile:
            # Se instantiaza un item si se indica prin parametru lista la care va fi adaugat
            item = qw.QListWidgetItem(self.lista_predictori)
            ch = qw.QCheckBox(v)
            # Inregistrare semnal de schimbare stare
            ch.stateChanged.connect(self.selectie_variabila1)
            self.lista_predictori.setItemWidget(item, ch)
            self.combo_index.addItem(v)
            self.combo_tinta.addItem(v)
        self.directorCurent = dialog.directory().absolutePath()
        self.date_citite = False
        self.invalidare_modele1()
        # print(self.directorCurent,type(self.directorCurent))

    def citire_testare(self):
        dialog = qw.QFileDialog(directory=self.directorCurent)
        dialog.setFileMode(qw.QFileDialog.AnyFile)
        dialog.setNameFilter("Fisier date (*.csv)")
        dialog.setViewMode(qw.QFileDialog.Detail)
        fileNames = []
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        if len(fileNames) == 0:
            return
        self.fisier_testare = fileNames[0]
        self.tabel_date_testare = pd.read_csv(self.fisier_testare)
        self.cale_testare.setText(self.fisier_testare)
        self.directorCurent = dialog.directory().absolutePath()
        self.invalidare_modele1()

    def selectie_variabila1(self):
        self.date_citite = False
        for i in range(self.lista_predictori.count()):
            item = self.lista_predictori.item(i)
            ch_variabila = self.lista_predictori.itemWidget(item)
        self.invalidare_modele1()

    def citire_date(self):
        self.variabile_selectate.clear()
        for i in range(self.lista_predictori.count()):
            item = self.lista_predictori.item(i)
            checkItem = self.lista_predictori.itemWidget(item)
            if checkItem.isChecked():
                self.variabile_selectate.append(checkItem.text())
        self.coloana_index = self.combo_index.currentText()
        self.tabel_date1.index = [str(v) for v in self.tabel_date1[self.coloana_index]]
        self.nume_instante = self.tabel_date1[self.coloana_index]
        #functii.inlocuire_na(self.tabel_date1)
        #functii.inlocuire_na(self.tabel_date_testare)
        self.x = self.tabel_date1[self.variabile_selectate].values
        nume_variabila_tinta = self.combo_tinta.currentText()
        self.data_subset = self.tabel_date1[self.variabile_selectate + [nume_variabila_tinta]]
        self.y = self.tabel_date1[nume_variabila_tinta].values
        t_predict = self.tabel_date_testare[self.variabile_selectate]
        self.x_test = t_predict.values
        self.date_citite = True

    def alerta(self, mesaj):
        msgBox = qw.QMessageBox()
        msgBox.setText(mesaj)
        msgBox.exec()

    def metrici_liniar(self):
        if not self.model_creat:
            self.creare_model()
        if self.model_creat:
            tabel_metrici = pd.DataFrame(
                data={
                    "MSE": [self.MSE_lin], "R2": self.R_lin
                }
            )
            tabel_metrici.to_csv("OUT_Regresie/metrici_lin.csv")
            self.vizualizareTabel(tabel_metrici, "Metrici modelul liniar")

    def coeficienti_liniar(self):
        if not self.model_creat:
            self.creare_model()
        if not self.model_creat:
            return
        params = np.append(self.b0_lin, self.b_lin)

        n, m = self.x.shape

        newX = np.insert(self.x, 0, np.ones((n,)), axis=1)
        MSE = (sum((self.y - self.y_lin) ** 2)) / (n - m - 1)

        var_b = MSE * (np.linalg.inv(np.dot(newX.T, newX)).diagonal())
        sd_b = np.sqrt(var_b)
        ts_b = params / sd_b

        n, m = newX.shape
        dof = n - m - 1
        p_values = [2 * (1 - stats.t.cdf(np.abs(b), dof)) for b in ts_b]

        sd_b = np.round(sd_b, 3)
        ts_b = np.round(ts_b, 3)
        p_values = np.round(p_values, 3)
        params = np.round(params, 4)

        myDF3 = pd.DataFrame(index=["Intercept"] + self.variabile_selectate)
        myDF3["Coeficienti"], myDF3["Erori standard"], myDF3["t_values"], myDF3["Probabilitati"] = [params, sd_b, ts_b,
                                                                                                    p_values]
        myDF3.to_csv("OUT_Regresie/sign_coef_lin.csv")
        self.vizualizareTabel(myDF3, "Coeficienti Model liniar")

    def vizualizareTabel(self, tabel_df, titlu):
        tabel =gui.Tabel(tabel_df)
        layout1 = qw.QHBoxLayout()
        layout1.addWidget(tabel)
        dialog = qw.QDialog()
        dialog.setWindowTitle(titlu)
        dialog.setLayout(layout1)
        dialog.setModal(True)
        dialog.exec_()

    def predictie_liniar(self):
        if not self.model_creat:
            self.creare_model()
        if not self.model_creat:
            return
        tabel_predict = pd.DataFrame(
            data={
                "Predict": self.y_lin_
            }, index=self.tabel_date_testare.index
        )
        tabel_predict.to_csv("OUT_Regresie/predict_lin.csv")
        self.vizualizareTabel(tabel_predict, "Predictie modelul liniar")

    def plot_predictii_liniar(self):
        if not self.model_creat:
            self.creare_model()
        if not self.model_creat:
            return
        grafice.plot_predictii(self.y_lin_, "Liniar")
        grafice.show()


    def creare_model(self):
        # print("Lin")
        if self.tabel_date1 is None or self.tabel_date_testare is None:
            self.alerta("Nu au fost citite datele!")
            return
        if not self.date_citite:
            self.citire_date()

        model_lin = LinearRegression()
        model_lin.fit(self.x, self.y)

        self.b_lin = model_lin.coef_
        self.b0_lin = model_lin.intercept_

        self.y_lin = model_lin.predict(self.x)

        self.MSE_lin = metrics.mean_squared_error(self.y, self.y_lin)
        self.R_lin = model_lin.score(self.x, self.y)

        self.y_lin_ = model_lin.predict(self.x_test)
        self.residuals_lin = self.y - self.y_lin
        self.residuals_lin = self.residuals_lin.reshape(-1, 1)

        self.model_creat = True



    def plot_heatmap(self):
        # Create the heatmap
        grafice.heatmap(self.data_subset.corr(), "Heatmap")
        grafice.show()

    def plot_qqplot_lin(self):
        # Create the heatmap
        grafice.qqplot(self.residuals_lin[:,0], "QQ-plot: Modelul liniar")
        grafice.show()

    def invalidare_modele1(self):
        self.date_citite = False
        self.model_creat = False


