import os
import time
import datetime
import glob
import MySQLdb
from time import strftime

#Variables for MySQL
db = MySQLdb.connect(host="localhost", user="pi", passwd="Charlesdickens12@",db="ganesh_temp_holder")
cur = db.cursor()

def tempRead():
	temp_c = 23.34
	# for x in range(0,3):
	#	temp_c = temp_c + 1	
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
