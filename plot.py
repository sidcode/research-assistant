import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(style="whitegrid")
sns.set_context("poster")
plt.ion()

print "Enter Filename: ",

FILENAME = raw_input()

print FILENAME
data = pd.read_csv(FILENAME)

print "Info about the file - ", data.info()

print "Enter column to be plotted: "
PLOT_COLUMN = raw_input()

plt.plot(data[PLOT_COLUMN])

plt.draw()

print "Enter Title: ",
title = raw_input()
#plt.draw()

plt.title(title)
print "Enter X lower limit: ",
x_lower = float(raw_input())

print "Enter X upper limit: ",
x_upper = float(raw_input())

plt.xlim(x_lower, x_upper)

print "Enter Y lower limit: ",
y_lower = float(raw_input())

print "Enter Y Higher limit: ",
y_upper = float(raw_input())

plt.ylim(y_lower, y_upper)

print "Enter Y Label: ",
Y_LABEL = raw_input()
plt.ylabel(Y_LABEL)

print "Enter X Label: ",
X_LABEL = raw_input()
plt.xlabel(X_LABEL)

print "Showing Final Plot. Saved it?", raw_input()
#plt.plot(data[PLOT_COLUMN])
plt.show()
