from load_csv import load
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def custom_formatter(x, pos):
    """
    make the x-axis labels more readable
    """
    if x >= 1e6:
        return f'{x*1e-6:.0f}M'
    elif x >= 1e3:
        return f'{x*1e-3:.0f}k'
    else:
        return f'{x:.0f}'


def main(
        p: str = './income_per_person_gdppercapita_ppp_inflation_adjusted.csv',
        path_life: str = './life_expectancy_years.csv'
        ):
    """
    Load the dataset and plot the life expectancy of Turkey
    x = life_expectancy_years.csv country
    """
    try:
        datagdp = load(p)
        datalife = load(path_life)
        if datagdp is None or datalife is None:
            raise ValueError("Data is empty")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    plt.title('1900')
    plt.ylabel('Life expectancy')
    plt.xlabel('Gross Domestic Product')
    plt.scatter(datagdp['1900'], datalife['1900'])
    plt.xscale('log')
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(custom_formatter))
    plt.gca().set_xticks([300, 1000, 10000])
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
