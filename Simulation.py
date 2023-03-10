from random import gauss
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

n = 1000000

omega = 0.001
alpha_1 = 0.26
beta_1 = 0.5

series = [gauss(0, 1), gauss(0, 1)]
vols = [1, 1]

for _ in range(n):
    new_vol = np.sqrt(
        omega + alpha_1 * series[-1] ** 2 + beta_1 * vols[-1] ** 2)
    new_val = gauss(0, 1) * new_vol

    vols.append(new_vol)
    series.append(new_val)

df = pd.DataFrame(series)
df = df.iloc[10:, :]
plt.figure(figsize=(10, 4))
plt.title('Simulated GARCH(1,1) Data', fontsize=20)
plt.plot(df)
# plt.show()

x2squared = np.square(df)
x4squared = np.square(x2squared)
x6squared = np.power(x2squared, 3)
# plt.plot(x2squared)
# plt.show()
# plt.plot(x4squared)
# plt.show()

mean2 = x2squared.mean()
mean4 = x4squared.mean()
mean6 = x6squared.mean()

# print('x^2=', mean2)
# print('x^4=', mean4)
# print('x^6=', mean6)

# ans = mean4/mean2**2


# Calculating <x^6>
ans = mean6 / ((mean2) ** 3)
print('simulation solution', ans)

subin1 = (alpha_1 + beta_1) / (1 - alpha_1 - beta_1)
subin2 = (1 + 2 * subin1) * (beta_1 ** 2 + 2 * alpha_1 * beta_1 + 3 * alpha_1 ** 2)
den1 = (1 - 3 * alpha_1 ** 2 - 2 * alpha_1 * beta_1 - beta_1 ** 2)
numerator1 = 15 * (1 - alpha_1 - beta_1) ** 3
numerator2 = 1 + 3 * subin1 + 3 * (subin2 / den1)
den = 1 - 15 * alpha_1 ** 3 - 9 * alpha_1 ** 2 * beta_1 - 3 * alpha_1 * beta_1 ** 2 - beta_1 ** 3
analytical6 = numerator1 * numerator2 / den

print('analytical solution', analytical6)
