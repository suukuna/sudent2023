import schedule

import library


def main():

    schedule.every().monday.at('09:15').do(library.self_promotion)
    schedule.every().tuesday.at('09:15').do(library.self_promotion)
    schedule.every().wednesday.at('09:15').do(library.self_promotion)
    schedule.every().thursday.at('09:15').do(library.self_promotion)
    schedule.every().friday.at('09:15').do(library.self_promotion)

    while True:
        schedule.run_pending()

if __name__ == '__main__':
    main()
