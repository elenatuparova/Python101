from aggregated_money_tracker import AggregatedMoneyTracker
from money_tracker import MoneyTracker
from money_tracker_menu import Menu
import sys

def main():
    file_name = sys.argv[1]
    money_tracker = MoneyTracker(AggregatedMoneyTracker(file_name))
    Menu.choose_option(money_tracker)

if __name__ == '__main__':
    main()