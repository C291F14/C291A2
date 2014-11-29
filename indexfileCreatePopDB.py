#Indexfile populate
import bsddb3 as bsddb
import random
import subprocess
import datetime as dt

DB_SIZE = 100000
DB_SEED = 10000000

def getRandom():
	return random.randint(0,63)

def getRandomChar():
	return chr(97+random.randint(0,25))

def CreatePop(dbK, dbV1):
	print("Creating Database")
	start = dt.datetime.now()
	random.seed(DB_SEED)

	index = 0
	# generate key-value pairs.
	while index < DB_SIZE:
		keyRange = 64 + getRandom()
		key = ""
		for i in range(keyRange):
			key = key +str(getRandomChar())

		key = key.encode(encoding = 'UTF-8')

		if dbK.has_key(key) == True:
			continue

		valueRange = 64 + getRandom()
		value = ""
		for i in range(valueRange):
			value = value + str(getRandomChar())

		value = value.encode(encoding = 'UTF-8')

		index += 1

		dbK[key] = value
		dbV1[key] = value

	
	dbV = {}

	for k, v in dbV1.items():
		dbV[v] = dbV.get(v, [])
		dbV[v].append(k)


	end = dt.datetime.now()
	print("Database has been created.\nTime = " + str((end - start).total_seconds()) + "s")

	return dbV
