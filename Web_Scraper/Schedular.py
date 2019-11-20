import WebScrapper
import schedule
import time

schedule.every().day.at("09:00").do(WebScrapper.Main)

while True:
    # Checks whether a scheduled task is pending to run or not

    schedule.run_pending()
    time.sleep(1)


