#ymdhms_to_jd.py

# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#  Converts Years, Months, Days, Hours, Minutes, Seconds to the Julian Date

# Parameters:
#  year
#  month
#  day
#  hour
#  minute
#  second

# Output:
#  Prints the year, month, day, hour, minute, second input into the fractional Julian date

# Written by Owen Davies
# Other contributors: None

# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys  # argv

# initialize script arguments
year: float(sys.argv[1])
month: float(sys.argv[2])
day: float(sys.argv[3])
hour: float(sys.argv[4])
minute: float(sys.argv[5])
second: float(sys.argv[6])

# parse script arguments
if len(sys.argv)==7:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 ymdhms_to_jd.py year month day hour minute second'\
  )
  exit()

# write script below this line
jd = day-32075+(1461*(year+4800+(month-14)/12)/4)+(367*(month-2-((month-14)/12)*12)/12)-(3*((year+4900+((month-14)/12))/100)/4)
jdint = int(jd)
jdmidnight = jdint-0.5
dfrac = (second+60*(minute+60*hour))/86400
jdfrac = jdmidnight+dfrac
print(jdfrac)