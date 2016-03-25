
import MySQLdb

from time import strftime,localtime
import datetime
from unidecode import unidecode

def connect():
    # Mysql connection setup.
    return MySQLdb.connect(host="localhost", user="root", passwd="root", db="bank")

def insertReading(tagId,action,current):
    db = connect()
    cur = db.cursor()
    currentTime=strftime("%Y%m%d%H%M%S", localtime())
    cur.execute("""INSERT INTO readings (tagId, time, action, current) VALUES (%s, %s, %s, %s)""",(tagId,currentTime,action,current))
    db.commit()
    #cur.execute("SELECT name,surname FROM users WHERE id = (SELECT userId FROM cards WHERE tagId=%s LIMIT 1)",(tagId))
    #row = cur.fetchone();
    db.close()
    #if(row==None):
     #   return "NO user exists"
    #else:
        #return unidecode(row[0]+" "+row[1])

def checkamtpay(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT amtpay FROM readings WHERE tagID=%s AND current=%s",(tagId,1))
    db.commit()
    row = cur.fetchone()
    
    db.close()
    return row[0]

def authenticat(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT balance,atmpin FROM users,cards WHERE cards.tagID=%s AND cards.userid=users.id LIMIT 1",(tagId))
    
    db.commit()
    row = cur.fetchone()
    
    db.close()
    return row

def payment(balance,tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("UPDATE users, cards SET users.balance=%s where cards.userid=users.id AND cards.tagId=%s",(int(balance),tagId))
    #cur.execute("UPDATE readings SET current=%s, amtpay=%s ",(0,0))
    db.commit()
    row = cur.fetchone()
    db.close()
    
def clearvalues():
    db = connect()
    cur = db.cursor()
    cur.execute("UPDATE readings SET current=%s",(0))
    db.commit()
    db.close()
    
def checkcard(tagId):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT userId FROM cards WHERE tagID=%s",(tagId))
    db.commit()
    row = cur.fetchone()
    db.close()
    if row==None:
        return 1
    else:
        return 0
    
