import schedule
import time
import subprocess

def job():
    subprocess.call(['python3', '/home/elvys/Desktop/Python Projects/Webscrapping/main.py'])

schedule.every().day.at("17:49").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)