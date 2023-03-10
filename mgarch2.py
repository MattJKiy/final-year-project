from random import gauss
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

for _ in range(n):
    new_vol1 = np.sqrt(
        omega_1 + alpha_11 * series1[-1] ** 2 + alpha_12 * series2[-1] ** 2 + beta_11 * vols1[-1] ** 2 + beta_12 * vols2[-1] ** 2)
    new_val1 = gauss(0, 1) * new_vol1

    vols1.append(new_vol1)
    series1.append(new_val1)

    new_vol2 = np.sqrt(
        omega_2 + alpha_21 * series1[-1] ** 2 + alpha_22 * series2[-1] ** 2 + beta_11 * vols1[-1] ** 2 + beta_12 *
        vols2[-1] ** 2)
    new_val2 = gauss(0, 1) * new_vol2

    vols2.append(new_vol2)
    series2.append(new_val2)


df = pd.DataFrame(series1)
df = df.iloc[10: , :]
#plt.figure(figsize=(10,4))
#plt.title('Simulated GARCH(1,1) Data', fontsize=20)
#plt.plot(df)
#plt.show()

x2squared = np.square(df)
x4squared = np.square(x2squared)
#plt.plot(x2squared)
#plt.show()
#plt.plot(x4squared)
#plt.show()

mean2 = x2squared.mean()
mean4 = x4squared.mean()

print('x^2=', mean2)
analytical1 = (omega_1 * (1-alpha_22-beta_22) + omega_2 * (alpha_12 + beta_12)) / ((1-alpha_11-beta_11) * (1-alpha_22-beta_22) - (alpha_21+beta_21) * (alpha_12+beta_12))
den = ((1-alpha_11-beta_11) * (1-alpha_22-beta_22) - (alpha_21+beta_21) * (alpha_12+beta_12))

print('analytical', analytical1)
#print('x^4=', mean4)

ans = mean4/mean2**2
print(ans)


#Calulating Cross-correleations
#frame = np.correlate(series1,series2,"full")
frame = np.correlate(series1,series2)
#print(frame, 'frame')
#plt.plot(frame)
#plt.title('cross-correlations')
#plt.show()
print(frame)