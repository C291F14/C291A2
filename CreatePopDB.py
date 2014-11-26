# Berkeley DB
# Chris Li

# Creating and populating a database for btree.
import bsddb3 as bsddb
import random
import time
import subprocess

DA_FILE = "/tmp/my_db/sample_db"
DB_SIZE = 100000
DB_SEED = 10000000

def getRandom():
    return random.randint(0,63)

def getRandomChar():
    return chr(97+random.randint(0,25))

def btreeCreatePop():
    subprocess.call(['rm', '-r', '-f', DA_FILE, '/tmp/my_db'])
    subprocess.call(['mkdir', '/tmp/my_db'])

    # open database if it exist, else create a new one.
    try:
        db = bsddb.btopen(DA_FILE, "w")
    except:
        print("DB doesn't exist, creating a new one.\n")
        db = bsddb.btopen(DA_FILE, "c")
        random.seed(DB_SEED)

    # generate key-value pairs.
    for index in range(DB_SIZE):
        keyRange = 64 + getRandom()
        key = ""
        for i in range(keyRange):
            key = key +str(getRandomChar())

        valueRange = 64 + getRandom()
        value = ""
        for i in range(valueRange):
            value = value + str(getRandomChar())

        # view key-value pairs.
        print("key:", key)
        print("value:", value)
        print("")

        # encoding the keys and values.
        key = key.encode(encoding = 'UTF-8')
        value = value.encode(encoding = 'UTF-8')

        # inserting the key-value pairs into the database.
        db[key] = value

    print("Database has been created.\n")

    # close the database.
    try:
        db.close()
    except Exception as e:
        print(e)
    return