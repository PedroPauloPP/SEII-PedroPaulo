import my_module as mm
from my_module import find_index, test 

import random
import math
import datetime
import calendar
import os
import antigravity


courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses,'Math')

print(index)
print(test)

print(sys.path)

random_course = random.choice(courses)
print(random_course)


rads = math.radians(90)
print(math.sin(rads)

today=datetime.date.today()
print(today)
print(calendar.isleap(2020))

print(os.getcwd())
print(os._file_)