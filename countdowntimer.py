import time

my_time = int(input("Enter the time in seconds: "))

# for x in reversed(range(0, my_time)): or use the3 step to reverse time
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours}:{minutes:02}:{seconds:02}")
    
    
    # print our conter x
    # print(x)
    # program to sleep for a given amount of seconds
    time.sleep(1)

print("TIME'S UP!")