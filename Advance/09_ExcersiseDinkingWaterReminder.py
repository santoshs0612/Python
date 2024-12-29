# # Drinking water Reminder 

# Write a python program which reminds you of drinking water every hour or two.
# your pgrogram can either beep or send notification for a specific operating syser 


import os
import time

def function():
    title = "Drink Water"
    message = "20 Minute over have a cup of Water"
    command = f'''
            notify-send "{title}" "{message}"
            '''
    os.system(command)

while True:
    function()
    time.sleep(20*60)