import MFRC522
from attendance import onScreen

def readNfc():
    reading = True
    while reading:
        MIFAREReader = MFRC522.MFRC522()

        #while continue_reading:
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        if status == MIFAREReader.MI_OK:
            print("Card detected")

        
        if status == MIFAREReader.MI_OK:
            (status,backData) = MIFAREReader.MFRC522_Anticoll()
            print ("Card Number: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4]))
            
            MIFAREReader.AntennaOff()
            reading=False
            return str(backData[0])+str(backData[1])+str(backData[2])+str(backData[3])+str(backData[4])

