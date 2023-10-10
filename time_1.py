currentTime = input("What is the current time?")

alarmTime = input("how many hours till the alarm goes off?")

Time = int(currentTime + alarmTime) % 24

print("Alarm will go off at: ", Time, ":00")
