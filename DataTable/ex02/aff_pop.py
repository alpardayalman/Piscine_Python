from load_csv import load
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.0fM' % (x * 1e-6)


def adapt(x):
    """
    Adapt the population data to be in millions
    """
    a = []
    for i in x:
        if i[-1] == 'M':
            a.append(float(i[:-1])*1000000)
        elif i[-1] == 'k':
            a.append(float(i[:-1])*1000)
        else:
            a.append(float(i))
    return a


def main(path: str = '../population_total.csv'):
    """
    Load the dataset and plot the life expectancy of Turkey
    x = life_expectancy_years.csv country
    """
    try:
        data = load(path)
        if data is None:
            raise ValueError("Data is empty")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    y1 = data[data['country'] == "Turkey"].values[0][1:]
    y2 = data[data['country'] == "France"].values[0][1:]
    new_y1 = adapt(y1)
    new_y2 = adapt(y2)

    x = [int(i) for i in data.columns[1:] if int(i) <= 2050]
    print(x)
    plt.plot(x, new_y1[:len(x)], label="Turkey")
    plt.plot(x, new_y2[:len(x)], label="France")
    plt.title('Population Projections')
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.legend()
    ax = plt.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions))
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
