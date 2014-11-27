# Berkeley DB
# Chris Li

# Creating and populating a database for btree.
import bsddb3 as bsddb
import random
import subprocess
import datetime as dt

#DA_FILE = "/tmp/my_db/291_db.db"
DB_SIZE = 100000
DB_SEED = 10000000

def getRandom():
    return random.randint(0,63)

def getRandomChar():
    return chr(97+random.randint(0,25))

def CreatePop(db, DB_FILE):
    print("Creating Database")
    start = dt.datetime.now()

    index = 0
    # generate key-value pairs.
    while index <= DB_SIZE:
        keyRange = 64 + getRandom()
        key = ""
        for i in range(keyRange):
            key = key +str(getRandomChar())

        key = key.encode(encoding = 'UTF-8')

        if db.has_key(key) == True:
            continue

        valueRange = 64 + getRandom()
        value = ""
        for i in range(valueRange):
            value = value + str(getRandomChar())

        value = value.encode(encoding = 'UTF-8')

        index += 1
        # view key-value pairs.
        # print("value:", value)
        # print("")

        # inserting the key-value pairs into the database.
        db[key] = value


    key = "Key".encode(encoding = 'UTF-8')
    value = "Value".encode(encoding = 'UTF-8')

    db[key] = value
    key = "MONEY".encode(encoding = 'UTF-8')
    value = "Value".encode(encoding = 'UTF-8')

    db[key] = value
    end = dt.datetime.now()
    print("Database has been created.\nTime = " + str((end - start).total_seconds()) + "s")

    # close the database.
    # try:
    #     db.close()
    # except Exception as e:
    #     print(e)
    return
    
