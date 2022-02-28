import time

class Person:
    def __init__(self,character,gender):
        self.characterIsHost = character
        self.genderIsFemale = gender

class Message:
    def __init__(self,timestamp,isPicture,length):
        self.timeStamp = timestamp
        self.isPicture = isPicture
        self.length = length

class Chat:
    def __init__(self):
        self.messageMember = []

    def addMessage(self,message):
        self.messageMember.append(message)

    def sortMessage(self):
        pass;

    def startTime(self):
        result = 0
        if self.messageMember != []:
            result = self.messageMember[0].timeStamp
        return result

    def stopTime(self):
        result = 0
        if self.messageMember != []:
            result = self.messageMember[-1].timeStamp
        return result


