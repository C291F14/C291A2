# Berkeley DB
# Cody Ingram
# Aaron Tse
# Chris Li

import bsddb3 as db3
import sys 
import random
import datetime as dt 
import subprocess
import btreeCreatePopDB
import indexfileCreatePopDB

DA_FILE = "/tmp/cdingram_db/291_db.db"

def main():
	
	arg = sys.argv[1].lower()
	inpList = ['btree', 'hash', 'indexfile']

	db = False
	dbK = False
	dbV = False

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
				subprocess.call(['rm', '-r', '-f', DA_FILE, '/tmp/cdingram_db'])
				subprocess.call(['mkdir', '/tmp/cdingram_db'])
				try:
					db = db3.btopen(DA_FILE, "w")
				except:
					print("DB doesn't exist, creating a new one.")
					db = db3.btopen(DA_FILE, "c") 

				btreeCreatePopDB.CreatePop(db)

			elif arg == 'hash':
				#hash
				subprocess.call(['rm', '-r', '-f', DA_FILE, '/tmp/cdingram_db'])
				subprocess.call(['mkdir', '/tmp/cdingram_db'])
				try:
					db = db3.hashopen(DA_FILE, "w")
				except:
					print("DB doesn't exist, creating a new one.")
					db = db3.hashopen(DA_FILE, "c") 
				
				btreeCreatePopDB.CreatePop(db)

			elif arg == 'indexfile':
				#indexfile
				subprocess.call(['rm', '-r', '-f', DA_FILE, '/tmp/cdingram_db'])
				subprocess.call(['mkdir', '/tmp/cdingram_db'])
				try:
					dbK = db3.btopen(DA_FILE, "w")
				except:
					print("DB doesn't exist, creating a new one.")
					dbK = db3.btopen(DA_FILE, "c") 

				# try:
				# 	dbV = db3.btopen(DA_FILE, "w")
				# except:
				# 	print("DB doesn't exist, creating a new one.")
				# 	dbV = db3.btopen(DA_FILE, "c") 
				dbV1 = {}

				dbV = indexfileCreatePopDB.CreatePop(dbK, dbV1)

		elif opt == '2':
			if db == False and dbK == False:
				print("Database not yet initialized")
			elif arg == "indexfile":
				key = input("Please enter a key: ")#.lower()
				start = dt.datetime.now()
				key = key.encode(encoding = 'UTF-8')
				if dbK.has_key(key) == True:
					value = dbK[key]
					#write to file
					key = key.decode('UTF-8')
					value = value.decode('UTF-8')
					f = open("answers3", 'a')
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

			else:
				key = input("Please enter a key: ")#.lower()
				start = dt.datetime.now()
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
			if db == False and dbK == False:
				print("Database not yet initialized")

			elif arg == "indexfile":
				key = input("Please enter a value: ")#.lower()
				start = dt.datetime.now()
				key = key.encode(encoding = 'UTF-8')
				try:
					value = dbV[key]
				except:
					print("There is no key associated with that value\n")

				records = 0
				key = key.decode('UTF-8')
				for each in value:
					val = each.decode('UTF-8')
					print(val)
					records += 1
					#write to file
					f = open("answers3", 'a')
					f.write(str(val) + '\n')
					f.write(str(key) + '\n')
					f.write(" \n")
					f.close()

				end = dt.datetime.now()
				print("Time: " + str((end - start).total_seconds()) + "s")
				print("Number of Records: " + str(records)) 
			

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

			if db == False and dbK == False:
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
					if k < in1 or k > in2:
						continue
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

					records = 0
					for k,v in output.items():
						records += 1
						#print("Key: " , k , ", Value: " , v)
						#write to file
						f = open("answers", 'a')
						f.write(str(k) + '\n')
						f.write(str(v) + '\n')
						f.write(" \n")
						f.close()
					print("Query recorded")

					end = dt.datetime.now()				
					print("Time: " + str((end - start).total_seconds()) + "s")
					print("Number of Records: " + str(records))

				#hash range search
				elif arg == 'hash':
					print("Hash range search")
					start = dt.datetime.now()
					
					a,b = db.last()
					k,v = db.first()
					
					while True:
						
						if k == a and v == b:
							if (in1 <= k) and (in2 >= k):
								k = k.decode('UTF-8')
								v = v.decode('UTF-8')
								output[k] = v
								break
							else:
								break						

						if (in1 <= k) and (in2 >= k):
							k = k.decode('UTF-8')
							v = v.decode('UTF-8')
							output[k] = v
							k,v = db.next()
						else:
							k,v = db.next()
						
						
					records = 0
					for k,v in output.items():
						records += 1
						#print("Key: ", k , ", Value: ", v)
						#write to file
						f = open("answers2", 'a')
						f.write(str(k) + '\n')
						f.write(str(v) + '\n')
						f.write(" \n")
						f.close()
					print("Query recorded")						
				
					end = dt.datetime.now()					
					print("Time: " + str((end - start).total_seconds()) + "s")
					print("Number of Records: " + str(records))

				elif arg == 'indexfile':
					print("indexFilerange search")
					start = dt.datetime.now()				
					k,v = dbK.set_location(in1)
					if k < in1 or k > in2:
						continue
					k = k.decode('UTF-8')
					v = v.decode('UTF-8')
					output[k] = v
					while True:
						k,v = dbK.next()
						if k > in2:
							break
						else:
							k = k.decode('UTF-8')
							v = v.decode('UTF-8')
							output[k] = v

					records = 0
					for k,v in output.items():
						records += 1
						#print("Key: " , k , ", Value: " , v)
						#write to file
						f = open("answers3", 'a')
						f.write(str(k) + '\n')
						f.write(str(v) + '\n')
						f.write(" \n")
						f.close()
					print("Query recorded")

					end = dt.datetime.now()				
					print("Time: " + str((end - start).total_seconds()) + "s")
					print("Number of Records: " + str(records))


		elif opt == '5':
			try:
				if arg == 'indexfile':
					dbK.close()
				else:
					db.close()
			except:
				print("Database could not be closed or doesn't exist")
			db = False
			dbK = False
			dbV = False
			try:
				subprocess.call(['rm', '-r', '-f', DA_FILE, '/tmp/cdingram_db'])
				print("Database file deleted if necessary")
			except:
				print("No database to delete")
			

		elif opt == '6':
			try:
				if arg == 'indexfile':
					dbK.close()
				else:
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
