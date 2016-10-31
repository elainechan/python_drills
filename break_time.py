import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started at" + time.ctime())
while(break_count < total_breaks):
    time.sleep(5)
    webbrowser.open('http://www.youtube.com/watch?v=8HVWitAW-Qg')
    break_count += 1
