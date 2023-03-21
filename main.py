import csv
import matplotlib.pyplot as plt
from datetime import datetime


def main():
    filename = 'avg_temp_warsaw.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)
        highs, dates, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[3])
                high_conv_to_cels = (high - 32) * 5 / 9
                low = int(row[4])
                low_conv_to_cels = (low - 32) * 5 / 9
            except ValueError:
                print(f"Niestety, brak pełnych danych dla pomiarów z {current_date}")
            else:
                highs.append(int(high_conv_to_cels))
                lows.append(low_conv_to_cels)
                dates.append(current_date)

    plt.style.use('bmh')
    fig, ax = plt.subplots(figsize=(15, 9))
    ax.set_title("Najwyższa i najniższa temperatura dnia od początku roku, Warszawa", fontsize = 24)
    ax.plot(dates, highs, c='red')
    ax.plot(dates, lows, c='blue')
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    ax.set_xlabel('Dzień', fontsize= 16)
    ax.set_ylabel('temperatura', fontsize=16)
    fig.autofmt_xdate()
    ax.tick_params(axis='both', which='major', labelsize=10)
    plt.show()


if __name__ == "__main__":
    main()