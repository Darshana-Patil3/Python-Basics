
# Math Module 

# Modules need to be imported.
import math


# so we got list of all the functions that are written/stored in this module. 
# let's try using sqrt

math.sqrt(4)

# But if you import sqrt() specifically, then you can access it just like that. 
# e.g.

from math import sqrt       # use ctrl + tab to get suggestions after import
sqrt(4)                     # we can use sqrt() now because in the above line, we are explicitly importing sqrt() function


# Continuing ahead
math.log10(100)

math.sqrt(60)

math.pi


# For mathematicials. (Others can ignore, not a big deal)

# If you remember, sin(90) = 1. 
# But math.sin() accepts value in radian, so we need to convert 90 degree in radian
print(math.sin(math.radians(90)))



# Data Module

from datetime import date
print(date.today())
today = date.today()
print(today)
print(today.day, today.month, today.year)


from datetime import datetime
print(datetime.now()) 
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))        




