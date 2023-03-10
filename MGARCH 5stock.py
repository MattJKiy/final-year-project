from random import gauss
from statsmodels.graphics import tsaplots
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

n = 1000

omega_1 = 0.0001
omega_2 = 0.0001
alpha_11 = 0.01
alpha_12 = 0.01
alpha_21 = 0.01
alpha_22 = 0.01
beta_11 = 0.05
beta_12 = 0.05
beta_21 = 0.05
beta_22 = 0.05

series1 = [gauss(0, 1), gauss(0, 1)]
vols1 = [1, 1]
series2 = [gauss(0, 1), gauss(0, 1)]
vols2 = [1, 1]
series3 = [gauss(0, 1), gauss(0, 1)]
vols3 = [1, 1]
series4 = [gauss(0, 1), gauss(0, 1)]
vols4 = [1, 1]
series5 = [gauss(0, 1), gauss(0, 1)]
vols5 = [1, 1]

for _ in range(n):
    new_vol1 = np.sqrt(
        omega_1 + alpha_11 * series1[-1] ** 2 + alpha_12 * series2[-1] ** 2 + alpha_12 * series3[-1] ** 2 + beta_11 * vols1[-1] ** 2 + beta_12 * vols2[-1] ** 2
        + beta_12 * vols3[-1] ** 2)
    new_val1 = gauss(0, 1) * new_vol1

    vols1.append(new_vol1)
    series1.append(new_val1)

    new_vol2 = np.sqrt(
        omega_2 + alpha_21 * series1[-1] ** 2 + alpha_22 * series2[-1] ** 2 + alpha_12 * series3[-1] ** 2 + beta_11 * vols1[-1] ** 2 + beta_12 *
        vols2[-1] ** 2 + beta_12 * vols3[-1] ** 2 + alpha_12 * series4[-1] ** 2 + alpha_12 * series5[-1] ** 2 + beta_11 * vols4[-1] ** 2 + beta_12 * vols5[-1] ** 2)
    new_val2 = gauss(0, 1) * new_vol2

    vols2.append(new_vol2)
    series2.append(new_val2)

    new_vol3 = np.sqrt(
        omega_1 + alpha_11 * series1[-1] ** 2 + alpha_12 * series2[-1] ** 2 + alpha_12 * series3[-1] ** 2 + beta_11 * vols1[-1] ** 2 + beta_12 *
        vols2[-1] ** 2 + beta_12 * vols3[-1] ** 2 + alpha_12 * series4[-1] ** 2 + alpha_12 * series5[-1] ** 2 + beta_11 * vols4[-1] ** 2 + beta_12 * vols5[-1] ** 2)
    new_val3 = gauss(0, 1) * new_vol3

    vols3.append(new_vol3)
    series3.append(new_val3)

    new_vol4 = np.sqrt(
        omega_1 + alpha_11 * series1[-1] ** 2 + alpha_12 * series2[-1] ** 2 + alpha_12 * series3[-1] ** 2 + beta_11 *
        vols1[-1] ** 2 + beta_12 *
        vols2[-1] ** 2 + beta_12 * vols3[-1] ** 2 + alpha_12 * series4[-1] ** 2 + alpha_12 * series5[
            -1] ** 2 + beta_11 * vols4[-1] ** 2 + beta_12 * vols5[-1] ** 2)
    new_val4 = gauss(0, 1) * new_vol4

    vols4.append(new_vol4)
    series4.append(new_val4)

    new_vol5 = np.sqrt(
        omega_1 + alpha_11 * series1[-1] ** 2 + alpha_12 * series2[-1] ** 2 + alpha_12 * series3[-1] ** 2 + beta_11 *
        vols1[-1] ** 2 + beta_12 *
        vols2[-1] ** 2 + beta_12 * vols3[-1] ** 2 + alpha_12 * series4[-1] ** 2 + alpha_12 * series5[
            -1] ** 2 + beta_11 * vols4[-1] ** 2 + beta_12 * vols5[-1] ** 2)
    new_val5 = gauss(0, 1) * new_vol5

    vols5.append(new_vol5)
    series5.append(new_val5)


df1 = pd.DataFrame(np.square(series1))
df1 = df1.iloc[10: , :]

df2 = pd.DataFrame(np.square(series2))
df2 = df2.iloc[10: , :]

df3 = pd.DataFrame(np.square(series3))
df3 = df3.iloc[10: , :]

df4 = pd.DataFrame(np.square(series4))
df4 = df4.iloc[10: , :]

df5 = pd.DataFrame(np.square(series5))
df5 = df5.iloc[10: , :]


frames = [df1, df2, df3, df4, df5]
df = pd.concat(frames,axis=1)
print(df)
result = df.corr(method='pearson')
print(result)
