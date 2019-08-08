import mysql.connector
from mysql.connector import errorcode
import csv

def createDB(cursor, dbName):
    '''
    This function to create database
    '''
    try:
        cursor.execute(
            "CREATE DATABASE  IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(dbName))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def useAlumDB(cursor, dbName):
    '''
    This function to specify which database to use, database will be created if it not exist.
    :param cursor:
    :param dbName: database to use
    '''
    try:
        cursor.execute("USE {}".format(dbName))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(dbName))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            createDB(cursor)
            print("Database {} created successfully.".format(dbName))
        else:
            print(err)
            exit(1)

def executeScriptsFromFile(cursor, filename):
    '''
    This function to execute SQL files
    :param cursor:
    :param filename: file to run
    '''
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except IOError as  msg:
            print ("Command skipped: ", msg)

def copy_Table(cursor, fromTable, toTable ):
    '''
    This function to copy content from one table to another
    :param cursor:
    :param fromTable: table to be copied
    :param toTable: table to be inserted
    :return:
    '''
    cursor.execute(f"INSERT INTO {toTable} SELECT * FROM {fromTable}")
    cursor.execute("COMMIT")

def readLinks(cursor, fromtable):
    '''
    This function to read out links from 'linkedin_profile' table
    :param cursor:
    '''
    cursor.execute(
        f"SELECT pID, url FROM {fromtable}"
    )

def assignPID(cursor, newNameFile, newAlumfile, auto_increment):
    '''
    This function to verify whether names received from Mills already in database or not, if not, assign an
    unique pID
    :param newNameFile: a csv file that contains new names as (firstname, lastname)
    :param newAlumfile: a csv fiel that will store new alums as (pID, dirstname, lastname)
    :param auto_increment: the current max pID in person database, used to assign pID to new alum
    :return:
    '''
    with open(newNameFile) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        names = list(reader)
        print(names)

    pIDs = []
    first = []
    last = []
    for data in names:
        first_name = data[0]
        last_name = data[1]

        try:
            cursor.execute("SELECT pID FROM alumDB_18.person WHERE first_name=%s AND last_name=%s", (first_name, last_name))
            pID = cursor.fetchall()[0][0]
        except:
            auto_increment += 1
            pID = auto_increment

        pIDs.append(pID)

        first.append(first_name)
        last.append(last_name)


    with open(newAlumfile, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(
            zip(pIDs, first, last))

