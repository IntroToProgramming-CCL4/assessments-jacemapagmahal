import datetime


currentdatetime = datetime.datetime.now()

formatdatetime = currentdatetime.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", formatdatetime)
