import matplotlib.pyplot as plt
import numpy as np

width = 0.3
a = [f"G{i}" for i in range(5)]
x = np.arange(len(a))
plt.bar(x - width / 2, [22, 30, 34, 30, 26], color="green", width=0.3, label='Men')
plt.bar(x + width / 2, [25, 32, 30, 35, 28], color="red", width=0.3, label='Women')
plt.title("Scores by Person")
plt.xlabel("Person")
plt.ylabel("Scores")
plt.ylim(0, 35)
plt.legend()
plt.xticks(x, a)
plt.show()
