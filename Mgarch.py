from random import gauss
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

n = 1000

omega_1 = 0.0001
omega_2 = 0.0001
alpha_11 = 0.25
alpha_12 = 0.01
alpha_21 = 0.01
alpha_22 = 0.01
beta_11 = 0.05
beta_12 = 0.05
beta_21 = 0.05
beta_22 = 0.05

return1 = pd.DataFrame(np.random.normal(loc=0,scale=1,size=n))
return2 = pd.DataFrame(np.random.normal(loc=0,scale=1,size=n))

vol1 = return1.rolling(2).var()
vol2 = return2.rolling(2).var()

returns1 = return1.to_numpy()
returns2 = return2.to_numpy()
vols1 = vol1.to_numpy()
vols2 = vol2.to_numpy()

mgarchs1 = []
mgarchs2 = []

for i in range(n):
    mgarch1 = omega_1 + alpha_11 *returns1[i]**2 + alpha_12*returns2[i]**2 + beta_11*vols1[i] + beta_12*vols2[i]
    mgarchs1.append(mgarch1)

    mgarch2 = omega_2 + alpha_21 * returns1[i] ** 2 + alpha_22 * returns2[i] ** 2 + beta_21 * vols1[i] + beta_22 * vols2[i]
    mgarchs2.append(mgarch2)


#plt.plot(vols1)
#plt.plot(mgarchs1)
#plt.show()
plt.plot(vols2)
plt.plot(mgarchs2)
plt.show()

x2squared1 = np.square(mgarch1)
mean2 = x2squared1.mean()
print('x^2=', mean2)


analytical1 = (omega_1 * (1-alpha_22-beta_22) + omega_2 * (alpha_12 + beta_12)) / ((1-alpha_11-beta_11) * (1-alpha_22-beta_22) - (alpha_21+beta_21) * (alpha_12+beta_12))
den = ((1-alpha_11-beta_11) * (1-alpha_22-beta_22) - (alpha_21+beta_21) * (alpha_12+beta_12))

print('analytical', analytical1)
print('den', den)