#  Time Disply 

import time

currTime  = int(time.strftime("%H"))
print(currTime)
if currTime < 12 and currTime > 4:
    print("Good Morning Sir Current Time is: ", currTime)
elif currTime>=12 and currTime <=16:
    print("Good Noon Sir current Time is: ", currTime)
elif currTime>16 & currTime<=21:
    print("Good Evening Sir current Time is: ", currTime)
else:
    print("Good Nigh Sir")