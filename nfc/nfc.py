import nxppy

import getpass
import display

import mysql

import hashlib

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




def readNfc(action):
    if(action==48):#0 - Incomming
        onScreen("Logging In...")
        display.lcdWriteFirstLine("Hello..")
        onScreen("Hello..")
    
        display.lcdWriteSecondLine("Swipe your Card")
          
        onScreen('Swipe your card')
        
        uid=""
        
        while True:
        
            try:
                #GPIO.cleanup()
                mifare = nxppy.Mifare()
                uid = mifare.select()
                if uid != "": 
                    break
                #print(uid)
            except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
                 pass

            time.sleep(1)

        
        
        mysql.insertReading(uid,Actions.incomming,1)
        cardcheck=mysql.checkcard(uid)
        if cardcheck==0:
            
            display.lcdWriteFirstLine("Hello.USER")
            display.lcdWriteSecondLine(uid) 
            print "Hello User, ",uid
            #print (uid)
            time.sleep(3)
	

            display.lcdWriteFirstLine("Processing...")
            display.lcdWriteSecondLine("Plz wait...")
            time.sleep(4)
            temp=input("Press any key to continue  ")
            res=0
            while True:
                res=mysql.checkamtpay(uid)
                if res!= 0 :
                    break

            print res
            display.lcdWriteFirstLine("Amount to pay : ")
            display.lcdWriteSecondLine(str(res))
            time.sleep(3)
            display.lcdWriteFirstLine("Enter pin to ")
            display.lcdWriteSecondLine("confirm")
            time.sleep(1)
            pin=""
            pin=getpass.getpass("Enter pin to confirm   ")
            pin=str(pin)
            pin=hashlib.md5(pin).hexdigest()
            bal=mysql.authenticat(uid)
            if bal[1]==pin:
            
        
                if bal[0]>=res:
            
                    mysql.payment(bal[0]-res,uid)
                    mysql.clearvalues()
                    display.lcdWriteFirstLine("Tranx Success")
                    display.lcdWriteSecondLine("Thank You !!")
                    
                    time.sleep(4)
            
                else:
                    display.lcdWriteFirstLine("Tranx failed")
                    display.lcdWriteSecondLine("Insuffient balance")
                    mysql.clearvalues()
                    time.sleep(3)


            else:
                display.lcdWriteFirstLine("Tranx failed")
                display.lcdWriteSecondLine("Wrong pin")
                mysql.clearvalues()
                time.sleep(3)




        elif cardcheck==1:
            display.lcdWriteFirstLine("Tranx failed")
            display.lcdWriteSecondLine("Invalid Card")
            mysql.clearvalues()
            time.sleep(3)

    #Sleep a little, so the information about last action on display is readable by humans
    time.sleep(1)






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
        #display.lcdWriteFirstLine(time.strftime("%d.%m. %H:%M:%S", time.localtime()))
        onScreen(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
        time.sleep(1)



def main():
    #GPIO.cleanup()
    try:
        #display.initGpio()
        display.init()
        while True:
            display.lcdWriteFirstLine("Welcome..")
            display.lcdWriteSecondLine("Choose an action...")
            print "choose an action"
            
            global displayTime
            displayTime=True
            #Start new thread to show curent datetime on display
            # and wait for user input on keyboard
            #thr = thread.start_new_thread(printDateToDisplay, ())
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

