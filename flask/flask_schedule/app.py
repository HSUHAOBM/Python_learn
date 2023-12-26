from flask import Flask
from multiprocessing import Process
import threading
import time
import schedule

app = Flask(__name__)

def job_1min():
    print("1 minute job")

def job_5min():
    print("5 minute job")

def job_1300():
    print("13:00 job")

def start_scheduler():
    schedule.every(1).minutes.do(job_1min)
    schedule.every(5).minutes.do(job_5min)
    schedule.every().day.at('13:00').do(job_1300)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    # use thread
    scheduler_thread = threading.Thread(target=start_scheduler, daemon=True)
    scheduler_thread.start()

    # use process
    # p = Process(target=start_scheduler)
    # p.start()

    app.run()