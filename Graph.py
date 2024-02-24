import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def plot(pairs, name):
    dates = []
    date = []
    cash = []
    pref = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    for i in pairs:
        date.append(i[0])
        dates.append(int(i[0][8:10]) + pref[int(i[0][5:7]) - 1])
        cash.append(i[1])
    plt.switch_backend('agg')
    plt.xticks(dates, date)
    plt.plot(dates, cash, marker='o', markersize=6)
    plt.title(name)
    plt.savefig("graph.jpg")
