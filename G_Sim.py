n = 1000000

Alpha_0 = 0.00001
Alpha_1 = 0.34
Beta_1 = 0.05

# Initialising array

x_t = sigma_t = [0]*n
sigma_t[1] = Alpha_0

quit()
def GARCH_Simulation():
    for i in range(n):

        sigma_t[i] = Alpha_0 + Alpha_1 * x_t(i - 1) ^ 2 + Beta_1 * sigma_t(i - 1)

        x_t[i] = sqrt(sigma_t(i)) * normrnd(0, 1)

# Calculating Simulation soln of x ^ 2 and x ^ 4 and x ^ 6

x_squared = square(x_t)
x_four = square((x_squared))
x_six = cube((x_squared)

First_Simulation_Soln = mean(x_squared);
Second_Simulation_Soln = mean(x_four) / mean(x_squared). ^ 2
Third_Simulation_Soln = mean(x_six) / (mean(x_squared). ^ 3)

# Calculating Analytical soln of x ^ 2 and x ^ 4

First_Analytical_Soln = Alpha_0 / (1 - Alpha_1 - Beta_1);
Second_Analytical_Soln = 3 + (6 * Alpha_1 ^ 2) / (1 - 3 * Alpha_1 ^ 2 - 2 * Alpha_1 * Beta_1 - Beta_1 ^ 2)

# Calculating Analytical soln of x ^ 6

var1 = 1 - Alpha_1 - Beta_1
var2 = Alpha_1 + Beta_1
var3 = Beta_1 ^ 2 + 2 * Alpha_1 * Beta_1 + 3 * Alpha_1 ^ 2
var4 = var2 / var1

den1 = 1 - 3 * Alpha_1 ^ 2 - 2 * Alpha_1 * Beta_1 - Beta_1 ^ 2
den2 = 1 - 15 * Alpha_1 ^ 3 - 9 * Alpha_1 ^ 2 * Beta_1 - 3 * Alpha_1 * Beta_1 ^ 2 - Beta_1 ^ 3

num1 = 15 * var1 ^ 3
num2 = 3 * (1 + 2 * var4) * (var3) / den1
num3 = 1 + (3 * (var2) / (var1)) + num2

Third_Anaytical_Soln = (num1 * num3) / den2






#Calculating Prices

y_t = zeros([1, n])

# Intial Stock price set to:

y_t(1) = 10

for i = 2:n

y_t(i) = y_t(i - 1) * exp(x_t(i))


#plot(y_t)
title('Price Y_t of Stock')