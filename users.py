# User class that has many features including setting names, uploading files (.mp4 or .csv), playing videos,
# and receiving quotes
from pathlib import Path  # Necessary for determining if a file is in the directory
import playVideo  # Necessary for video playback
from quotes import Quotes  # Necessary for getting quotes
from Bluetooth_Serial_Communication import record
from threshold_calculator import call


class Users:

    def __init__(self):  # Constructor: Every new account starts with the name "Guest" and an empty array for .mp4
        # and .csv files
        self.name = "Guest"
        self.filename = []
        self.csvfile = []
        self.quotes = Quotes()
        print("New account created.")

    def __del__(self):  # Don't worry about this. This is for memory purposes
        print("Deleting " + self.name + ".")

    def setName(self, name):  # Allows the user to change their account name to any string
        self.name = name
        print("Name set as " + self.name)

    def setVideoFile(self, filename):  # Puts video file in your account if it is already in the directory
        if filename[-4:] != ".mp4":
            print(filename + " is not an .mp4 file. It has not been added to your account.")
        else:
            file = Path(filename)
            if file.is_file():
                print(filename + " is in the directory and has been added to your account.")
                self.filename.append(filename)
            else:
                print(filename + " does NOT exist in the directory and has not been added to your account.")

    def setCSVFile(self, filename):  # Puts .csv file in your account if it is already in the directory
        if filename[-4:] != ".csv":
            print(filename + " is not an .csv file. It has not been added to your account.")
        else:
            file = Path(filename)
            if file.is_file():
                print(filename + " is in the directory and has been added to your account.")
                self.csvfile.append(filename)
            else:
                print(filename + " does NOT exist in the directory and has not been added to your account.")

    def getName(self):  # Returns name set on account. Returns guest if no name was set.
        return self.name

    def videoFileExist(self, filename):  # Returns 1 if .mp4 file exists on the account. Returns 0 otherwise.
        print("Searching for filename \"" + filename + "\" in \"" + self.name + "\"")
        for i in self.filename:
            if filename == i:
                print(filename + " exist.")
                return 1
        print(filename + " does NOT exist.")
        return 0

    def csvFileExist(self, filename):  # Returns 1 if .csv file exists on the account. Returns 0 otherwise.
        print("Searching for filename \"" + filename + "\" in \"" + self.name + "\"")
        for i in self.csvfile:
            if filename == i:
                print(filename + " exist.")
                return 1
        print(filename + " does NOT exist.")
        return 0

    def playVideo(self, filename):  # Imports playVideo.py | If .mp4 file exist on the account, play it.
        if self.videoFileExist(filename):
            playVideo.playVideo(filename)

    def getQuote(self):  # Returns a random quote from our pre-made quotes list
        print(self.quotes.giveRandomQuote())

    def addQuote(self, string):  # Add a quote to the quote list
        self.quotes.addQuote(string)

    def getQuoteTot(self):  # returns an integer, the total number of elements in the quote list
        return self.quotes.giveQuoteTot()

    def listQuotes(self):  # Prints a list of all the quotes in the quote list
        self.quotes.listQuotes()

    def delQuote(self, index):  # Delete a quote from the quote list given an index
        self.quotes.delQuote(index)

    def isHappy(self, videoFile, csvFile):
        if self.csvFileExist(csvFile):
            if call(csvFile):
                self.playVideo(videoFile)
            else:
                self.getQuote()

    @staticmethod
    def recordVid():
        record()


# Code for debugging purposes
Mom = Users()  # Creating User "Andrew" and putting 2 files in his account
Mom.setName("LJ\'s mom")
Mom.setCSVFile("MomHappy1.csv")
Mom.setCSVFile("MomSad1.csv")
Mom.setCSVFile("MomNeutral1.csv")
Mom.setVideoFile("test.mp4")
Mom.isHappy("test.mp4", "MomNeutral1.csv")
# Andrew.setVideoFile("test.mp4")
# Andrew.setVideoFile("test2.mp6")
#
# print()
#
# Isaias = Users()  # Creating User "Isaias" and putting 1 files in his account
# Isaias.setName("Isaias")
# Isaias.setVideoFile("test3.mp4")
#
# print()
#
# LJ = Users()  # Creating Guest User "LJ" and putting no files in her account
# print("The name of this account is: " + LJ.name)
#
# print()
#
# Andrew.videoFileExist("test2.mp4")
#
# Isaias.playVideo("test.mp4")
# Andrew.playVideo("test.mp4")
#
# print()
#
# Andrew.getQuote()
# Isaias.getQuote()

# Andrew.recordVid()

print("\nEnd of program.\n")
