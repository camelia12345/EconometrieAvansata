import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import pylab as plab
import seaborn as sb
import statsmodels.api as sm


culori = ['green', 'darkgoldenrod', 'firebrick', 'purple', 'teal', 'darkorange', 'darkcyan', 'seagreen', 'blue', 'darkviolet',
          'maroon', 'forestgreen', 'navy', 'darkslategray', 'indigo',
          'mediumseagreen', 'seagreen',
          'crimson', 'chocolate', 'darkolivegreen', 'slateblue']


def plot_clustere(x, y, g, grupe, etichete=None, titlu="Plot clustere", fisier=None):
    plt.style.use('ggplot')
    g_ = np.array(g)
    f = plt.figure(figsize=(10, 7))
    ax = f.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontsize=16, color='teal')
    nr_grupe = len(culori)
    for v in grupe:
        x_ = x[g_ == v]
        y_ = y[g_ == v]
        k = int(v[1:])
        if len(x_) == 1:  # Cluster singleton
            ax.scatter(x_, y_, color='k', label=v)
        else:
            ax.scatter(x_, y_, color=culori[k % nr_grupe], label=v)
    ax.legend()
    if etichete is not None:
        for i in range(len(etichete)):
            ax.text(x[i], y[i], etichete[i])
    if fisier is not None:
        f.savefig("OUT_Cluster/" + fisier)


def plot_regresie(y1, y2, nume_model=""):
    plt.style.use('ggplot')
    f = plt.figure(figsize=(14, 8))
    assert isinstance(f, plt.Figure)
    ax = f.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title("PLot Y real vs. Y estimat" + ". Model: "+nume_model, fontsize=18)
    ticks_font = font_manager.FontProperties(
        family='Times New Roman',
        style='italic',
        size=16, weight='bold')
    for label in ax.get_xticklabels():
        label.set_fontproperties(ticks_font)
    for label in ax.get_yticklabels():
        label.set_fontproperties(ticks_font)

    n = len(y1)
    x = np.arange(1, n + 1)

    ax.scatter(x, y1, s=10, c='darkorange', label="Y real")
    ax.scatter(x, y2, s=10, c='teal', label="Y estimat")

    params = {'legend.fontsize': 16,
              'legend.handlelength': 2}
    plab.rcParams.update(params)
    ax.legend()
    f.savefig("OUT_Regresie/estim_" + "Y real_ Y estimat" + ".png")


def plot_predictii(y,model):
    plt.style.use('ggplot')
    f = plt.figure(figsize=(14, 8))
    assert isinstance(f, plt.Figure)
    ax = f.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title("PLot predictii. Model "+model, fontsize=18)
    ticks_font = font_manager.FontProperties(
        family='Times New Roman',
        style='italic',
        size=16, weight='bold')
    for label in ax.get_xticklabels():
        label.set_fontproperties(ticks_font)
    for label in ax.get_yticklabels():
        label.set_fontproperties(ticks_font)

    n = len(y)
    x = np.arange(1, n + 1)
    m, b = np.polyfit(x, y, 1)
    ax.scatter(x, y, s=10, c='darkorange', label="Predictii")
    ax.plot(x, m * x + b, c='teal', label="Regresia")

    params = {'legend.fontsize': 16,
              'legend.handlelength': 2}
    plab.rcParams.update(params)
    ax.legend()
    f.savefig("OUT_Regresie/predict" + ".png")

def heatmap(t, titlu, vmin=-1, vmax=1):
    f = plt.figure(figsize=(13, 9))
    ax = f.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontsize=16)
    sb.heatmap(t, vmin=vmin, vmax=vmax, cmap="rocket", ax=ax, annot=True)
    f.savefig("OUT_Regresie/heatmap" + ".png")


def qqplot(t, titlu):
    plt.style.use('ggplot')
    f = plt.figure(figsize=(13, 9))
    ax = f.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontsize=16)
    sm.qqplot(t, line ='45', ax=ax)
    f.savefig("OUT_Regresie/qqplot" + ".png")


def show():
    plt.show()


