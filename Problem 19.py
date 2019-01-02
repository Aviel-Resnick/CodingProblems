# Project Euler; 19

# Variable Declarations
x = 2 # Jan 1, 1901 = Wed
l = []

# Day Identification
def checkDay(i):
    day = i % 7
    if(day == 1):
        return("Mon")
    if(day == 2):
        return("Tues")
    if(day == 3):
        return("Wed")
    if(day == 4):
        return("Thurs")
    if(day == 5):
        return("Fri")
    if(day == 6):
        return("Sat")
    if(day == 0):
        return("Sun")

# Month -> Days
def checkMonth(months, leapness):
    # Jan
    if(months == 1):
        return(31)
    # Feb
    if(months == 2 and leapness == False):
        return(28)
    # Feb leapness
    if(months == 2 and leapness == True):
        return (29)
    # March
    if(months == 3):
        return(31)
    # April
    if(months == 4):
        return(30)
    # May
    if(months == 5):
        return(31)
    # June
    if(months == 6):
        return(30)
    # July
    if(months == 7):
        return(31)
    # Aug
    if(months == 8):
        return(31)
    # Sept
    if(months == 9):
        return(30)
    # Oct
    if(months == 10):
        return(31)
    # Nov
    if(months == 11):
        return(30)
    # Dec
    if(months == 12):
        return(31)

# Warp Speed
for years in range(1901,2001):
    leapness = False
    if(years % 4 == 0 and years != 2000):
        leapness = True
    #print(years, leapness)
    for months in range(1,13):
        #print("Month: ", months)
        for days in range(1, checkMonth(months, leapness) + 1):
            x = x + 1
            if(days == 1):
                l.append(x%7)
            #print(checkDay(x))
print(l)
# Answer = 171
