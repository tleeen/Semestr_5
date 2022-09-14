import matplotlib.pyplot as plt

plt.barh(['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'], [22, 17.5, 9, 8, 7.5, 7], color="green", alpha=0.7)
plt.title("PopularitY of Programming Language Worldwide, Oct 2017 compared to a year ago")
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.xlim(0, 25)
plt.minorticks_on()
plt.grid(which='major', color='r', linewidth=1, alpha=0.5)
plt.grid(which='minor', color='b', linestyle=':')
plt.show()
