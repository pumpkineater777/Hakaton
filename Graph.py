import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

def plot(pairs, name, budget):
    dates = []
    date = []
    cash = []
    pref = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    for i in pairs:
        date.append(i[0])
        dates.append(int(i[0][8:10]) + pref[int(i[0][5:7]) - 1] + (int(i[0][:4]) - 2022) * 365)
        cash.append(i[1])
    for i in range(1, len(cash)):
        cash[i] = cash[i - 1] + cash[i]
    plt.xticks(dates, date)
    plt.plot(dates, cash, color="#909090", marker='o', markersize=6)
    plt.title(name)
    plt.gca().set_facecolor("#F8F3EA")
    plt.axhline(y=budget, linestyle='--')
    plt.savefig("static/graph.jpg", facecolor="#F8F3EA")






