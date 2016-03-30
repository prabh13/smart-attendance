
import display
import nfc
import mysql


import sys
import tty
import termios
import logging

import thread
import time

import RPi.GPIO as GPIO

#Enable debug logging into log
DEBUG=True
#Enable printing informations to std. output
VERBOSE=True

class Actions:
    incomming=1
    outcomming=2
    breakstart=3
    breakend=4

if(DEBUG):
    logging.basicConfig(format='%(asctime)s %(message)s',filename='attendance.log', level=logging.DEBUG)

def debug(message):
    logging.debug(message)

def onScreen(message):
    if(VERBOSE):
        print(message)

def read():
    #ledRedOn()
    cardId=nfc.readNfc()
    #beep()
    #ledRedOff()
    return cardId

def readNfc(action):
    if(action==55):#7 - Incomming
        onScreen("Logging In...")
        display.lcdWriteFirstLine("Hello")
        onScreen("Hello..")
        display.lcdWriteSecondLine("Swipe your Card")
        onScreen('Swipe your card')
        cardId=read()
        #print (cardId)
        logging.info("Incomming - %s",cardId)
        name = mysql.insertReading(cardId,Actions.incomming)
        print name
        display.lcdWriteSecondLine(name)
    if(action==57):#9 - outcomming
        onScreen("...")
        display.lcdWriteFirstLine("Logging out...")
        print "Logging out" 
        display.lcdWriteSecondLine("Swipe your Card")
        print "Swipe card"
        cardId=read()
        logging.info("Outcomming - %s",cardId)
        name = mysql.insertReading(cardId,Actions.outcomming)
        print name
        display.lcdWriteSecondLine(name)
        mysql.hoursworked(cardId)
    if(action==49):#1 - break start
        onScreen("Break Start..")
        display.lcdWriteFirstLine("Break Start..")
        display.lcdWriteSecondLine("Swipe your Card")
        print "Swipe card.."
        cardId=read()
        logging.info("Break start - %s",cardId)
        name = mysql.insertReading(cardId,Actions.breakstart)
        print name
        display.lcdWriteSecondLine(name)
    if(action==51):#3 - break end
        onScreen("Break End...")
        display.lcdWriteFirstLine("Break End...")
        display.lcdWriteSecondLine("Swipe your Card")
        print "Swipe card.."
        cardId=read()
        logging.info("Break end - %s",cardId)
        name = mysql.insertReading(cardId,Actions.breakend)
        print name
        display.lcdWriteSecondLine(name)
    if(action==53):#5 - Deletion of last inserted action
        onScreen("Delete the last entry...")
        display.lcdWriteFirstLine("Deleting...")
        print "deleting"
        print "Swipe card to confirm deletion"
        display.lcdWriteSecondLine("")
        
        cardId=read()
        logging.info("Deleting last action - %s",cardId)
        (lastTime,lastAction)=mysql.getLastReading(cardId) or (None, None)

        if(lastTime == None and lastAction == None):
            display.lcdWriteSecondLine("Unknown Event")
            print "Unknown Event"
            logging.info("Action not found")
            time.sleep(1)

        else:
            display.lcdWriteFirstLine("Delete Event?")
            print "Delete Event"
            if(lastAction==Actions.incomming):
                display.lcdWriteSecondLine("Check In")
                print "check in"        
            elif(lastAction==Actions.outcomming):
                display.lcdWriteSecondLine("Check Out")
                print "Check out"
            elif(lastAction==Actions.breakstart):
                display.lcdWriteSecondLine("break start")
                print "break start"
            elif(lastAction==Actions.breakend):
                display.lcdWriteSecondLine("End of break?")
                print "End of break"
            print "press 1 to confirm action else any other key"
            a=getOneKey()
            if(a==49):#1
                onScreen("Mazu")
                logging.info(" - Deleting action %s (cas: %s)",lastAction, lastTime)
                mysql.deleteLastReading(cardId)
                display.lcdWriteSecondLine("Deleted!")
                print "Deleted"
            else:
                onScreen("Not Deleted")
                logging.info(" - Deleting canceled")
                display.lcdWriteSecondLine("Not deleted!")

    #Sleep a little, so the information about last action on display is readable by humans
    time.sleep(1)

def ledRedOn():
    GPIO.output(8,True)

def ledRedOff():
    GPIO.output(8,False)



#Backing up the input attributes, so we can change it for reading single
#character without hitting enter  each time
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
def getOneKey():
    try:
        tty.setcbreak(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        return ord(ch)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


displayTime=True
def printDateToDisplay():
    while True:
        #Display current time on display, until global variable is set
        if displayTime!=True:
            thread.exit()
        display.lcdWriteFirstLine(time.strftime("%d.%m %H:%M:%S", time.localtime()))
        #onScreen(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
        time.sleep(1)

#def initGpio():
    #GPIO.setmode(GPIO.BCM)
   # GPIO.setup(8, GPIO.OUT)
   # GPIO.setup(13, GPIO.OUT)

def main():
    GPIO.cleanup()
    try:
        #initGpio()
        display.init()
        while True:
            display.lcdWriteSecondLine("Choose an action...")
            print "choose an action"
            global displayTime
            displayTime=True
            #Start new thread to show curent datetime on display
            # and wait for user input on keyboard
            thr = thread.start_new_thread(printDateToDisplay, ())
            a = getOneKey()
            displayTime=False
            if 47 < a < 58:
                readNfc(a)
    except KeyboardInterrupt:
        GPIO.cleanup()
        pass
    GPIO.cleanup()

if __name__ == '__main__':
    debug("----------========== Starting session! ==========----------")
    main()
