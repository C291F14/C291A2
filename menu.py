# Berkeley DB
# Cody Ingram
# Aaron Tse

import bsddb3 as db3
import sys 
import random
import datetime as dt 
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
				start = dt.datetime.now()
				key = input("Please enter a key: ")#.lower()
				key = key.encode(encoding = 'UTF-8')
				if db.has_key(key) == True:
					value = db[key]
					#write to file
					key = key.decode('UTF-8')
					value = value.decode('UTF-8')
					f = open("answers", 'a')
					f.write(str(key) + '\n')
					f.write(str(value) + '\n')
					f.write(" \n")
					f.close()

					end = dt.datetime.now()
					print(value)
					print("Time: " + str((end - start).total_seconds()) + "s")
					print("Number of Records: 1") # isn't this always 1????
				else:
					print("There is no value associated with that key\n")

		elif opt == '3':
			if db == False:
				print("Database not yet initialized")
			else:
				value = input("Please enter a value: ")#.lower()
				start = dt.datetime.now()
				value = value.encode(encoding = 'UTF-8')
				records = 0
				for k,v in db.items():
					if v == value:
						records += 1
						#write to file
						k = k.decode('UTF-8')
						v = v.decode('UTF-8')
						f = open("answers", 'a')
						f.write(str(k) + '\n')
						f.write(str(v) + '\n')
						f.write(" \n")
						f.close()
						print(k)
				
				if records == 0:
					print("There is no key associated with that value\n")

				end = dt.datetime.now()
				print("Time: " + str((end - start).total_seconds()) + "s")
				print("Number of Records: " + str(records)) # Same here??!?!?!?!?!?!?!?!?!WTF>>>!>!>!!!!???


		elif opt == '4':

			if db == False:
				print("Database not yet initialized")
			else:
				in1 = input("Enter a starting point: ").encode(encoding = 'UTF-8')
				in2 = input("Enter an end point: ").encode(encoding = 'UTF-8')

				output = {}

				if in1 > in2:
					print("Invalid range")

				#btree range search
				elif arg == 'btree':	
					start = dt.datetime.now()				
					print("Btree range search")
					k,v = db.set_location(in1)
					k = k.decode('UTF-8')
					v = v.decode('UTF-8')
					output[k] = v
					while True:
						k,v = db.next()
						if k > in2:
							break
						else:
							k = k.decode('UTF-8')
							v = v.decode('UTF-8')
							output[k] = v

					for k,v in output.items():
						print("Key: " , k , ", Value: " , v)
						#write to file
						f = open("answers", 'a')
						f.write(str(k) + '\n')
						f.write(str(v) + '\n')
						f.write(" \n")
						f.close()

					end = dt.datetime.now()				
					print("Time: " + str((end - start).total_seconds()) + "s")

				#hash range search
				elif arg == 'hash':
					print("Hash range search for: " + in1 + " " + in2)

				elif arg == 'indexFile':
					print("indexFilerange search for: " + in1 + " " + in2)


		elif opt == '5':
			try:
				db.close()
				db = False
				subprocess.call(['rm', '-r', '-f', DA_FILE, '/tmp/my_db'])
				print("Database closed")
			except:
				print("Database could not be closed")

		elif opt == '6':
			try:
				db.close()
				subprocess.call(['rm','-r','-f',DA_FILE])
			except:
				print("Database could not be closed because it does not exist")

			print("Thank you, come again")
			sys.exit()

		else:
			print("Invalid input, Please try again")
			continue

main()
