import numpy as np
import pandas as pd
import pandas.api.types as pdt

# ACP simplificat
def acp(x):
    R = np.corrcoef(x, rowvar=False)
    # calcul vector si valori proprii
    valp, vecp = np.linalg.eig(R)
    # sortare valori proprii si vectori proprii
    k_inv = [k for k in reversed(np.argsort(valp))]
    # alpha = valp[k_inv]
    a = vecp[:, k_inv]
    regularizare(a)
    # calcul corelatii factoriale
    # Rxc = a * np.sqrt(alpha)
    # calcul componente
    # standardizare x
    medii = np.mean(x, axis=0)
    abaterestd = np.std(x, axis=0)
    Xstd = (x - medii) / abaterestd
    c = Xstd @ a
    return c[:, :2]

# Regularizare vectori proprii
def regularizare(t, y=None):
    if type(t) is pd.DataFrame:
        for c in t.columns:
            minim = t[c].min()
            maxim = t[c].max()
            if abs(minim) > abs(maxim):
                t[c] = -t[c]
                if y is not None:
                    k = t.columns.get_loc(c)  # determina indexul coloanei
                    y[:, k] = -y[:, k]
    else:
        for i in range(np.shape(t)[1]):
            minim = np.min(t[:, i])
            maxim = np.max(t[:, i])
            if np.abs(minim) > np.abs(maxim):
                t[:, i] = -t[:, i]