import matplotlib.pyplot as plt


def autolabel(rects, labels=None, height_factor=1.01):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if labels is not None:
            try:
                label = labels[i]
            except (TypeError, KeyError):
                label = ' '
        else:
            label = '%d' % int(height)
        plt.text(rect.get_x() + rect.get_width() / 2., height_factor * height,
                 '{}'.format(label),
                 ha='center', va='bottom')


plt.bar(['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'], [22, 17.5, 9, 8, 7.5, 7], color="blue", alpha=0.7)
plt.title("PopularitY of Programming Language Worldwide, Oct 2017 compared to a year ago")
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.ylim(0, 25)
plt.minorticks_on()
plt.grid(which='major', color='r', linewidth=1, alpha=0.5)
plt.grid(which='minor', color='b', linestyle=':')
ax = plt.gca()
autolabel(ax.patches, ['22.200000', '17.600000', '8.800000', '8.000000', '7.700000', '6.700000'], height_factor=1.01)
plt.show()
