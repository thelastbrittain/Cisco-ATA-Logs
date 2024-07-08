"""
Author: Benjamin Brittain
Date Started: 6/21/24
Goal: Create a program that takes in a folder with elevator logs, returns a file with the names of all the 
devices and any errors that they created. 
"""

"""Basic Outline: """
#get a folder 
#loop through each file in folder
    #for each file in the folder
        #for each line in folder
            #turn line into an object
            #check if the message is irregular
            #if irregular, add it to list
            #if list is longer than 10, don't add anymore
    #if irregularity list is empty, add a line in green to the file with device name and print good message
    #if there are messages: print devicename in red with fail
    #for each line in list of error message:
        #print time stamp and message


"""Class required""" 
#Line class


import os
import glob

from LogLine import LogLine


print("Welcome to Elevator Log Analyzer")
# directory = input("Please Enter the path to the folder you would like to have checked: ")
# Specify the directory you want to loop through
directory = '/Users/benjaminbrittain/Desktop/ElevatorLogsFolder/ElevatorLogs'
outLogger = '/Users/benjaminbrittain/Desktop/ElevatorLogsFolder/OutputLogs/Logger.txt'

# Get a list of all files in the directory
files = glob.glob(os.path.join(directory, '*'))
with open (outLogger, 'w') as out_file:
    for file_path in files:
        # Ensure we are only processing files (not directories)
        if os.path.isfile(file_path):
            print(f'Processing file: {file_path}')
            # Open the file for reading
            with open(file_path, 'r',) as file:
                # Loop through each line in the file
                mapOfErrors = {}
                deviceName = ""
                lastTimeStamp = ""
                lineNumber = 0
                try: 
                    for line in file:
                        lineNumber += 1
                        # print(f'Processing file: {file_path}')
                        # print(lineNumber)
                        if lineNumber == 1:
                            logLine = LogLine()
                            logLine.assignAttributes(line.split())
                            deviceName = logLine.getDeviceName()
                        if line.startswith("Jun 14"):
                            logLine = LogLine()
                            logLine.assignAttributes(line.split())
                            if logLine.containsErrors(lastTimeStamp):
                                errorKey = f"{logLine.getTimeStamp()} Line {lineNumber}"      
                                mapOfErrors[errorKey] = logLine.messageBody
                            lastTimeStamp = logLine.getTimeStamp()

                        elif line.startswith("Jun 15"):
                            break
                except UnicodeDecodeError as e:
                    # print("Caught Unicode Error")
                    if "Switched to Jan 1st" not in mapOfErrors.values():
                        mapOfErrors[lineNumber] = "Switched to Jan 1st"
                    continue
                finally:
                    if len(mapOfErrors) == 0:
                        out_file.write("------------------------------------------ \n")
                        out_file.write(deviceName + file_path.rsplit('/', 1)[-1] + ": All tests Passed" + "\n")
                        
                    else:
                        out_file.write("------------------------------------------ \n")
                        out_file.write(deviceName + " "  + file_path.rsplit('/', 1)[-1] + ": Tests failed.\n")  
                          
                        for key, value in mapOfErrors.items():
                            out_file.write(str(key) + ": " + str(value) + "\n")

