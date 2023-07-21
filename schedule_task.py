import schedule
import time
import datetime 

def MINUTE():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print( str(TNOW) + "Printing this line every minute...")

def SECONDS():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print( str(TNOW) + "Printing hash ##### keys very 5seconds interval!")

schedule.every(1).minutes.do(MINUTE)
schedule.every(5).seconds.do(SECONDS)

while True:
    schedule.run_pending()
    time.sleep(1)
