import time

months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
days = {1:"monday", 2:"tuesday", 3:"wednesday", 4:"thursday", 5:"friday", 6:"saturday", 7:"sunday"}

def isLeapYear(yr):
	if(yr%4 != 0):
		return False
	elif(yr%100 != 0):
		return True
	elif(yr%400 != 0):
		return False
	else:
		return True

#
# Day is a dictionary object with "month", "day", and "year" stored as numbers 
# and "name" being the number of the day of the week
#
def addDay(d):
	d["day"] += 1
	d["name"] = (d["name"]%7)+1
	if(isLeapYear(d["year"]) and d["month"] == 2 and d["day"] == 29):
		return d
	elif(isLeapYear(d["year"]) and d["month"] == 2 and d["day"] == 30):
		d["day"] -= (months[d["month"]] + 1)
		d["month"] += 1
	elif(d["day"] > 31 and d["month"] == 12):
		d["day"] -= 31
		d["month"] = 1
		d["year"] += 1
	elif(d["day"] > months[d["month"]]):
		d["day"] -= months[d["month"]]
		d["month"] += 1
	return d

s = time.time()

start_date = {"month":1, "day":1, "year":1900, "name":1}

day = start_date

for x in range(365):
	day = addDay(day)

count = 0 # Count of Sundays landing on the first of the month for 99 years
		  # from Jan 1, 1901 to Dec 31, 2000

while(day["month"] != 12 or day["day"] != 31 or day["year"] != 2000):
	day = addDay(day)
	if(day["day"] == 1 and day["name"] == 7):
		count += 1

s = time.time() - s

print("\nThe number of Sundays on the first of the month from Jan 1, 1901 to Dec 31, 2000 is %d\nTook %.3f seconds\n" % (count, s))