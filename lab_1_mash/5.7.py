from matplotlib import pyplot as plt

plt.pie([31.3, 24.8, 12.4, 11.3, 10.8, 9.4], labels=['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'],
        autopct='%1.1f%%',
        shadow=True, explode=(0.1, 0, 0, 0, 0, 0), wedgeprops={'lw': 1, 'edgecolor': "k"}, rotatelabels=True,
        startangle=150)
plt.axis("equal")
plt.show()
