import matplotlib.pyplot as plt

plt.bar(['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'], [22, 17.5, 9, 8, 7.5, 7],
        color=['red', 'black', 'green', 'blue', 'yellow', 'skyblue'], alpha=0.9)
plt.title("PopularitY of Programming Language Worldwide, Oct 2017 compared to a year ago")
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.ylim(0, 25)
plt.minorticks_on()
plt.grid(which='major', color='r', linewidth=1, alpha=0.5)
plt.grid(which='minor', color='b', linestyle=':')

plt.show()
