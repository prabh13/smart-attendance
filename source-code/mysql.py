import MySQLdb

from time import strftime,localtime
import datetime
from unidecode import unidecode

def connect():
    # Mysql connection setup. Insert your values here
    return MySQLdb.connect(host="localhost", user="root", passwd="root", db="pi")

def insertReading(tagId,action):
    db = connect()
    cur = db.cursor()
    currentDate=strftime("%Y%m%d", localtime())
    currentTime=strftime("%H%M%S", localtime())
    cur.execute("""INSERT INTO readings (tagId, date, time, action) VALUES (%s, %s, %s, %s)""",(tagId,currentDate,currentTime,action))
    db.commit()
    
    cur.execute("SELECT name,surname FROM users WHERE id = (SELECT userId FROM cards WHERE tagId=%s LIMIT 1)",(tagId))
    row = cur.fetchone();
    db.close()
    if(row==None):
        return "NO user exists"
    else:
        return unidecode(row[0]+" "+row[1])


def getLastReading(tagId):
    '''Returns last reading inserted max 5 minutes ago in array (time,action)'''
    checkTime = datetime.datetime.now() - datetime.timedelta(minutes=5)
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT time, action FROM readings WHERE tagId=%s AND time>%s ORDER BY time DESC LIMIT 1",(tagId,checkTime.strftime("%Y%m%d%H%M%S")))
    row = cur.fetchone()
    db.close()
    return row

def hoursworked(tagId):
    currentDate=strftime("%Y%m%d", localtime())
    checkTime = datetime.datetime.now() - datetime.timedelta(minutes=5)
    db = connect()
    cur = db.cursor()
    
    cur.execute("SELECT time from readings where date=%s AND action=1 AND tagId=tagId",(currentDate))
    row=cur.fetchone()
    t1=row[0]
    cur.execute("SELECT time from readings where date=%s AND action=2 AND tagId=tagId",(currentDate))
    row=cur.fetchone()
    t2=row[0]
    cur.execute("SELECT time from readings where date=%s AND action=3 AND tagId=tagId",(currentDate))
    row=cur.fetchone()
    t3=row[0]
    cur.execute("SELECT time from readings where date=%s AND action=4 AND tagId=tagId",(currentDate))
    row=cur.fetchone()
    t4=row[0]
    hours=t2-t1+t3-t4
    cur.execute("""INSERT INTO total_hours (tagId, date, hours) VALUES (%s, %s, %s)""",(tagId,currentDate,hours))
    db.commit()
    db.close()



def deleteLastReading(tagId):
    '''Deletes last reading inserted max 5(+1) minutes ago'''
    checkTime = datetime.datetime.now() - datetime.timedelta(minutes=6)
    db = connect()
    cur = db.cursor()
    cur.execute("DELETE FROM readings WHERE tagId=%s AND time>%s ORDER BY time DESC LIMIT 1",(tagId,checkTime.strftime("%Y%m%d%H%M%S")))
    row = cur.fetchone()
    db.close()
