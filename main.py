import csv
import argparse
from datetime import datetime as dt


def parse_arguments():
    parser = argparse.ArgumentParser(description='Get worked time')
    parser.add_argument('start_time', help='Time started', type=str)
    parser.add_argument('end_time', help='Time finished', type=str)
    return parser.parse_args()


def calculate_time(start_time, end_time):
    time_diff = dt.strptime(end_time, '%H:%M') - dt.strptime(start_time, '%H:%M')
    print(str(time_diff)[:-3])
    with open("times.csv", 'a+', newline='') as file:
        fields = [dt.today().strftime("%d/%m/%Y"), start_time, end_time, str(time_diff)[:-3]]
        writer = csv.writer(file)
        writer.writerow(fields)


if __name__ == '__main__':
    args = parse_arguments()
    calculate_time(args.start_time, args.end_time)
