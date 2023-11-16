import matplotlib.pyplot as plt
import numpy as np
import question3

plt.rcParams["font.sans-serif"] = "SimHei"
plt.rcParams['axes.unicode_minus'] = False

x1 = np.arange(-0.2, 1.4, 0.001)
x2 = np.arange(-2, 2, 0.001)
x3 = np.arange(0.5, 4*np.pi, 0.001)

fig = plt.figure(figsize=(14, 4))
plt.subplot(1, 3, 1)
plt.plot(x1, question3.func1(x1))
plt.title("方程1图像")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(1, 3, 2)
plt.plot(x2, question3.func2(x2))
plt.title("方程2图像")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(1, 3, 3)
plt.plot(x3, question3.func3(x3))
plt.title("方程3图像")
plt.xlabel("x")
plt.ylabel("y")

plt.show()