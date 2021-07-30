import time

currentTime = time.time()                    #'''epoch time'''
print("Current Time: ", currentTime)

seconds = int(currentTime)

minutes = seconds // 60;

hours = seconds // 3600;

print("Hours =", hours, "Minutes = ", minutes, "Seconds =", seconds)