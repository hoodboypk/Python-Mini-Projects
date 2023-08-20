import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)
minutes = time.strftime('%M')
print(minutes)
seconds = time.strftime('%S')
print(seconds)


if(hour >=5 and hour<12):
    print("Good Morning!")
elif(hour >= 12 and hour <18):
    print("Good Afternoon!")
elif(hour>=18 and hour <23):
    print("Good Evening!")
else:
    print("Good Night!")