from load_csv import load
import sys
import matplotlib.pyplot as plt


def main(path: str = '../life_expectancy_years.csv'):
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
    y = data[data['country'] == "Turkey"]
    y = y.values[0][1:]
    x = [int(i) for i in data.columns[1:]][:len(y)+1]
    plt.plot(x, y)
    plt.title('Turkey Life expectancy Projections')
    plt.ylabel('Life expectancy')
    plt.xlabel('Year')
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
