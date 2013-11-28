#this program is designed as a continuous loop so that the program keeps
#the data entered from the user over a long period of time.
def menuMain ():
    choice = int (input ("""
    Main Menu:
    1 Log your run
    2 Your averages
    3 Your totals
    4 Your pace of a single run
    :"""))
    return choice
def choiceOneA ():
    distance= round(float(input("Enter the distance in miles:")),2)
    print ("we have recorded your distance as", distance, "miles")
    return distance
def choiceOneB ():    
    time= round(float(input("Enter your time in minutes:")),3)
    print ("we have recorded your time as", time, "minutes")
    return time
def choiceTwo():
    avgDistance= sum(distanceList)/len(distanceList)
    avgTime= sum(timeList)/len(timeList)
    print ("your average distance is", avgDistance, "miles")
    print ("your average time is", avgTime, "minutes")
    print ("your pace is", round(avgTime/avgDistance, 2), "miles per minute")
    print ("your average speed is", round ((avgDistance/avgTime)*60, 2), "miles per hour")
    return()
def choiceThree():
    totalDistance= sum(distanceList)
    totalTime= sum(timeList)
    totalRuns= len(distanceList)
    print ("your total distance is", totalDistance,"miles")
    print ("your total time is", totalTime, "minutes")
    print ("you have completed", totalRuns, "runs congratulations!")
    return()
def choiceFour ():
    distance= float(input("for this single calculation what was your distance in miles?"))
    time=float(input("for this single calculation what was your time in minues?"))
    pace= round(time/distance,2)
    print ("your pace for this single run was", pace, "minutes per mile")
    return()
#main
print ("Welcome to the Runner's Calculator")
distanceList = []
timeList= []
choice="start"
while choice != "stop":
    choice=menuMain()
    if choice == 1:
        distanceList.append (choiceOneA())
        timeList.append (choiceOneB())
    elif choice == 2:
        choiceTwo ()
    elif choice == 3:
        choiceThree ()
    elif choice == 4:
        choiceFour ()
    else:
        menuMain()
