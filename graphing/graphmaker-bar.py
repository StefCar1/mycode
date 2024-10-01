import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    N = 4
    localnetMeans = (20, 35, 30, 35)  # LAN length of outage (mins)
    # WAN length of outage (min), commented out for now
    # wanMeans = (25, 32, 34, 20)
    
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35        # the width of the bars

    # Create a bar chart for the localnetMeans
    p1 = plt.bar(ind, localnetMeans, width)

    # Describe the chart metadata
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))

    # Adding a legend for just LAN data
    plt.legend([p1], ["LAN"])

    # Save the chart to two different file locations
    plt.savefig("/home/student/mycode/graphing/2018summary.png")
    plt.savefig("/home/student/static/2018summary.png")


if __name__ == "__main__":
    main()

