#!/usr/bin/python
import os
import time
import datetime
import glob
import MySQLdb
from time import strftime

# Variables for MySQL
db = MySQLdb.connect(host="localhost", user="pi", passwd="Charlesdickens12@",db="ganesh_temp_holder")
cur = db.cursor()

temp_c = 23.34

def tempRead():
    global temp_c
    if temp_c == 23.34:
		temp_c = -23.34
    elif temp_c == -23.34:
		temp_c = 23.34
    return temp_c

while True:
	temp = tempRead()
	print temp
	datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
	print datetimeWrite
	sql = ("""INSERT INTO tempLog (datetime, temperature) VALUES (%s,%s)""",(datetimeWrite,temp))
	try:
		print "Writing to database ..."
		# Execute the SQL command 
		cur.execute(*sql)
		# Commit the changes in database
		db.commit()
		print "Write complete"

	except:
		# Rollback in case of error
		db.rollback()
		print "Failed writing to database"

	cur.close()
	db.close()
	break
