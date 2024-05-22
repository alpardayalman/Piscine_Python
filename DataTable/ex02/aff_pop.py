from load_csv import load
import sys
import matplotlib.pyplot as plt
import pandas as pd


def main(path: str = '../population_total.csv'):
    """
    Load the dataset and plot the life expectancy of Turkey
    x = life_expectancy_years.csv country
    """
    data = load(path)
    y1 = data[data['country'] == "Turkey"].values[0][1:]
    y2 = data[data['country'] == "France"].values[0][1:]
    new_y1 = []
    new_y2 = []
    for i in y1:
        if i[-1] == 'M':
            new_y1.append(float(i[:-1])*1000000)
        elif i[-1] == 'k':
            new_y1.append(float(i[:-1])*1000)
        else:
            new_y1.append(float(i))

    for i in y2:
        if i[-1] == 'M':
            new_y2.append(float(i[:-1])*1000000)
        elif i[-1] == 'k':
            new_y2.append(float(i[:-1])*1000)
        else:
            new_y2.append(float(i))

    length = len(y1) if len(y1) < len(y2) else len(y2)
    # for i in y1.values:
    #     print(i,end=" | ")
    # for i in y2.values:
    #     print(i,end=" | ")
    x = [int(i) for i in data.columns[1:]][:length+1]
    print(x)
    plt.plot(x, new_y1[:length], label="Turkey")
    plt.plot(x, new_y2[:length], label="France")
    plt.title('Turkey vs Seychelles Population')
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.legend()
    plt.show()
    # print(data)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()