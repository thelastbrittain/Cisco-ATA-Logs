from datetime import datetime, timedelta
from typing import Any, List

class LogLine:
    okayMessages = ["lldp send packet", "resync flag 5", "retry after 3600 secs", "dropped 0", "download status: Failed", "download fail reasons: Connection error",
                    "parse_profile_rule done, must_resync=1", "invalid rule!"]
    okayBeginsIn = ["FSTR_SERVER_IP[0]:","FSTR_000:", "download profile:", "lldp stop fast-start"]
    
    def __init__(self, date: Any = 0, timeStamp: Any = 0, deviceName: str = "", logLevel: str = "", process: str = "", method: str = "", messageBody: str = ""):
        self.date = date
        self.timeStamp = timeStamp
        self.deviceName = deviceName
        self.logLevel = logLevel
        self.process = process
        self.method = method
        self.messageBody = messageBody

    def getDate(self):
        return self.date
    
    def setDate(self, date):
        self.date = date
        
    def getTimeStamp(self):
        return self.timeStamp
    
    def setTimeStamp(self, timeStamp):
        self.timeStamp = timeStamp

    def getDeviceName(self):
        return self.deviceName
    
    def setDeviceName(self, deviceName):
        self.deviceName = deviceName

    def getLogLevel(self):
        return self.logLevel
    
    def setLogLevel(self, logLevel):
        self.logLevel = logLevel
        
    def getProcess(self):
        return self.process
    
    def setProcess(self, process):
        self.process = process

    def getMethod(self):
        return self.method
    
    def setMethod(self, method):
        self.method = method

    def getMessageBody(self):
        return self.messageBody
    
    def setMessageBody(self, messageBody):
        self.messageBody = messageBody

    def assignAttributes(self, attributeList: List[Any]):

        if len(attributeList) >= 7:
            date = " ".join(attributeList[0:2])
            self.setDate(date)
            self.setTimeStamp(attributeList[2])
            self.setDeviceName(attributeList[3])
            self.setLogLevel(attributeList[4])
            self.setProcess(attributeList[5])
            self.setMethod(attributeList[6])
            message = " ".join(attributeList[7:])
            self.setMessageBody(message)
        else:
            print("Failure in assigning attributes.")
            print("Length of attributes in list: " + str(len(attributeList)))
            print("Attribute List:")
            print(attributeList)
    
    def containsErrors(self, lastTimeStamp):
        #if time stamp isn't right, return true
        #if not okay message
        # and if not in beginning message
        #return true
        if self.faultyTime(lastTimeStamp):
            return True
        if self.getMessageBody() in self.okayMessages:
            return False
        for message in self.okayBeginsIn:
            if self.messageBody.startswith(message):
                return False
        return True

    def faultyTime(self, lastTimeStamp):
        if lastTimeStamp == "":
            return False
        last_time = datetime.strptime(lastTimeStamp, '%H:%M:%S')
        current_time = datetime.strptime(self.getTimeStamp(), '%H:%M:%S')

        time_difference = current_time - last_time

        max_allowed_difference = timedelta(minutes=3)

        if abs(time_difference) <= max_allowed_difference:
            return False
        else:
            return True

"""
if len(attributeList) >= 7:
            date = " ".join(attributeList[0:2])
            self.setDate(date)
            self.setTimeStamp(attributeList[2])
            self.setDeviceName(attributeList[3])
            self.setLogLevel(attributeList[4])
            self.setProcess(attributeList[5])
            self.setMethod(attributeList[6])
            message = " ".join(attributeList[7:])
            self.setMessageBody(message)
            print("Success in assigning attributes.")
        else:
            print("Failure in assigning attributes.")
            print("Length of attributes in list: " + str(len(attributeList)))
            print("Attribute List:")
            print(attributeList)
"""

"""
if len(attributeList) >= 7:
            date = " ".join(attributeList[0:2])
            self.setDate(date)
            print(f"Date set to: {self.getDate()}")

            timeStamp = attributeList[2]
            self.setTimeStamp(timeStamp)
            print(f"TimeStamp set to: {self.getTimeStamp()}")

            deviceName = attributeList[3]
            self.setDeviceName(deviceName)
            print(f"DeviceName set to: {self.getDeviceName()}")

            logLevel = attributeList[4]
            self.setLogLevel(logLevel)
            print(f"LogLevel set to: {self.getLogLevel()}")

            process = attributeList[5]
            self.setProcess(process)
            print(f"Process set to: {self.getProcess()}")

            method = attributeList[6]
            self.setMethod(method)
            print(f"Method set to: {self.getMethod()}")

            message = " ".join(attributeList[7:])
            self.setMessageBody(message)
            print(f"MessageBody set to: {self.getMessageBody()}")

            print("Success in assigning attributes.")
        else:
            print("Failure in assigning attributes.")
            print(f"Length of attributes in list: {len(attributeList)}")
            print("Attribute List:")
            print(attributeList)
"""