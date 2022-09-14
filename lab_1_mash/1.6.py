from datetime import date
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pylab

xdata = [date(2016, 10, 3),
         date(2016, 10, 4),
         date(2016, 10, 5),
         date(2016, 10, 6),
         date(2016, 10, 7)]
plt.plot(xdata, [772.5, 776.4, 776.5, 776.9, 775.0], color="red", linewidth=2, marker='o', markerfacecolor='r')
plt.title("Closing stock value of Alphabet Inc")
plt.xlabel("Date")
plt.ylabel("Closing Value")
plt.minorticks_on()
plt.grid(which='major', color='r', linewidth=1)
plt.grid(which='minor', color='b', linestyle=':')
plt.xlim(date(2016, 10, 3), date(2016, 10, 7))
plt.ylim(772.5, 777.0)
axes = pylab.subplot(1, 1, 1)
xfmt = mdates.DateFormatter('%Y-%m-%d')
axes.xaxis.set_major_formatter(xfmt)
plt.show()
