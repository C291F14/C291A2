# Berkeley DB
# Cody Ingram
# Aaron Tse

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

	db = False

	# check valid program argument
	if arg not in inpList:
		print("Invalid Program Argument")
		sys.exit()

	# menu start
	while True:
		
		opt = input("Please Select An Option\n 1 - Create and populate a database\n 2 - Retrieve records with a given key\n 3 - Retrieve records with given data\n 4 - Retrieve records with a range of key values\n 5 - Destroy Database\n 6 - Quit\n")
		
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
			if db == False:
				print("Database not yet initialized")
			else:
				key = input("Please enter a key: ")#.lower()
				key = key.encode(encoding = 'UTF-8')
				if db.has_key(key) == True:
					value = db[key]
					print(value)
				else:
					print("There is no value associated with that key\n")

		elif opt == '3':
			if db == False:
				print("Database not yet initialized")
			else:
				value = input("Please enter a value: ")#.lower()
				value = value.encode(encoding = 'UTF-8')
				for k,v in db.items():
					if v == value:
						key = k
				if key != None:
					print(key)
				else:
					print("There is no key associated with that value\n")

		elif opt == '4':
			print("call something")

		elif opt == '5':
			try:
				db.close()
				subprocess.call(['rm', '-r', '-f', DA_FILE, '/tmp/my_db'])
				print("Database closed")
			except:
				print("Database could not be closed")
				#raise

		elif opt == '6':
			try:
				db.close()
				subprocess.call(['rm','-r','-f',DA_FILE,'/tmp/my_db'])
				print("Thank you, come again")
				sys.exit()
			except:
				print("Database could not be closed because it does not exist")
				raise

		else:
			print("Invalid input, Please try again")
			continue

main()
