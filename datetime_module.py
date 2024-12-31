#  Write a script using the datetime module to calculate the number of 
#days between two given dates.


import datetime
# Import the date class from datetime module
from datetime import date
# Define a function called differ_days which calculates the difference in days between two dates
def differ_days(date1, date2):
    # Assign date1 to variable a
    a = date1
    # Assign date2 to variable b
    b = date2
    # Return the difference in days between the two dates
    return (a - b).days
# Print an empty line
print()
# Print the difference in days between October 12, 2016 and December 10, 2015
print(differ_days((date(2016, 10, 12)), date(2015, 12, 10)))
# Print the difference in days between March 23, 2016 and December 10, 2017
print(differ_days((date(2016, 3, 23)), date(2017, 12, 10)))
# Print an empty line
print()
