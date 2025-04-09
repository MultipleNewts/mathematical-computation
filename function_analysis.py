# %%
import numpy as np
import matplotlib.pyplot as plt
from hyperbolic_functions import ln as test
# from trigonometric_functions import sin as test


X = np.linspace(-np.pi, np.pi, 1000)
Y1 = np.log(X)
Y2 = []
for x in X:
    Y2.append(test(x))
Y3 = np.abs((np.array(Y2)-Y1)/Y1)

fig, ax = plt.subplots(1, 2)
ax[0].plot(X, Y1, label="numpy computation")
ax[0].plot(X, Y2, label="CORDIC computation")
ax[0].legend()
ax[1].plot(X, Y3, label="error")
ax[1].legend()
# ax[0].set_ylim([-100, 100])
# ax[1].set_ylim([-100, 100])
plt.show()

# %%
