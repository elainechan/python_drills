"""
Input: hour, minute

Smallest increment is 1 min

Hour hand:
12 hours 360 degrees
each hour 360/12
movement of hour hand each minute 360/12/60

Scenario:
midnight right now

hr hand movement per min 
360/12/60 = 0.5 degrees/min

min hand movement per min
360/60 = 6 degrees/min

hr hand in relation to mins
val min hand - val hr hand = desired angle
val hr hand - val min hand = desired angle
(take absolute value)

first case 12:30
second case 2:05

at 12:30
min hand angle = 180
hr hand angle = 30 * 0.5 = 15

180 deg is max

if angle > 180,
subtract from 360

Algorithm steps:
1. take an input of hour and min
2. convert both inputs into degrees (if any angles > 180, subtract from 360)
3. 
4.

"""
input = 

min_position = min_input * 6
hr_position = (h_input * 60 + min_input) * 0.5