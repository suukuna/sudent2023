import time

import schedule

import library


# def say_good_morning():
#     schedule.every().day.at("08:10", "Europe/Amsterdam").do(library.greeting)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
#
#
# def say_goodnight():
#     schedule.every().day.at("00:30", "Europe/Amsterdam").do(library.farewell)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
#

def main():
    schedule.every().day.at("15:53", "Europe/Amsterdam").do(library.greeting)

    schedule.every().day.at("00:30", "Europe/Amsterdam").do(library.farewell)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    main()
    # say_good_morning()
    # say_goodnight()
