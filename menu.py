# Berkeley DB
# Cody Ingram

import bsddb3 as db3
import sys 
import random
import time 
import subprocess
import btreeCreatePopDB

DA_FILE = "/tmp/my_db/291_db.db"

def main():
	
	arg = sys.argv[1].lower()
	inpList = ['btree', 'hash', 'indexfile']

	# check valid program argument
	if arg not in inpList:
		print("Invalid Program Argument")
		sys.exit()

	# menu start
	while True:
		
		opt = input("Please Select An Option\n 1 - Create and populate a database\n 2 - Retrieve records with a given key\n 3 - Retrieve records with given data\n 4 - Retrieve records with a range of key values\n 5 - Destroy Database\n 6 - Quit\n")
		
		db = False

		if opt == '1':
			if arg == 'btree':
				#btree
				subprocess.call(['rm', '-r', '-f', DA_FILE, '/tmp/my_db'])
				subprocess.call(['mkdir', '/tmp/my_db'])
				try:
					db = db3.btopen(DA_FILE, "w")
				except:
					print("DB doesn't exist, creating a new one.")
					db = db3.btopen(DA_FILE, "c") 
					
				btreeCreatePopDB.CreatePop(db, DA_FILE)

			elif arg == 'hash':
				#hash
				subprocess.call(['rm', '-r', '-f', DA_FILE, '/tmp/my_db'])
				subprocess.call(['mkdir', '/tmp/my_db'])
				try:
					db = db3.hashopen(DA_FILE, "w")
				except:
					print("DB doesn't exist, creating a new one.")
					db = db3.hashopen(DA_FILE, "c") 
				
				btreeCreatePopDB.CreatePop(db, DA_FILE)

			elif arg == 'indexfile':
				#indexfile
				print('indexfile')

		elif opt == '2':
			print("call something")
		elif opt == '3':
			print("call something")
		elif opt == '4':
			print("call something")
		elif opt == '5':
			print("call something")
		elif opt == '6':
			print("call something")
		else:
			print("Invalid Input")
			continue

main()
