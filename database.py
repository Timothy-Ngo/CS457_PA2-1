"""Kimberly Meza Martinez
PA2: Basic Data Manipulation
CS457
10/31/22"""

import sys
import os
import string
import os.path  # os for creating directories
from shutil import rmtree  # for removing tree paths


def createDb(valueInput):  # pass input, navigate to directory, if db doesnt exist create it, if it does send error
    parentDirectory = os.getcwd()  # set current working directory to parent directory
    newDirectoryDb = valueInput
    # creates path for new directory
    path = os.path.join(parentDirectory, newDirectoryDb)
    try:  # error handling if path already exists
        os.mkdir(path)
        print('Database', newDirectoryDb, 'created.')

    except OSError:  # catch error and print if db already exists
        print('!Failed to create database', newDirectoryDb, 'because it already exists.')


def createTbl(data, valueInput):  # if tbl doesnt exist, create it, if it does send error message
    newFileTbl = valueInput

    try:
        f = open(newFileTbl, 'x')  # creates file for exclusive creation
        f.write(data)
        f.close()
        print('Table', newFileTbl, 'created.')

    except OSError:
        print('!Failed to create table', newFileTbl, 'because it already exists.')


def dropDb(valueInput):  # pass input,
    parentDirectory = os.getcwd()  # set current working directory to parent directory
    dbToDrop = valueInput
    # creates path for new directory
    path = os.path.join(parentDirectory, dbToDrop)
    try:
        rmtree(path)  # removes directory
        print('Database', dbToDrop, 'deleted.')
    except OSError:  # if cannot remove path its bc it doesnt exist
        print('!Failed to delete', dbToDrop, 'because it does not exist.')


def dropTbl(valueInput):  # if it exists within directory then delete, if it doesnt then send error
    fileToDrop = valueInput
    try:
        # removes a file, do i need to add '.txt' at the end
        os.remove(fileToDrop)
        print('Table', fileToDrop, 'deleted.')

    except OSError:
        print('!Failed to delete', fileToDrop, 'because it does not exist.')


def useDb(workingDirectory, valueInput):
    # creates path for new directory
    path = os.path.join(workingDirectory, valueInput)
    os.chdir(path)  # change to directory
    print('Using database', valueInput, '.')


def selectTbl(valueInput):  # display contents of tbl(aka file)
    tblToView = valueInput
    tblExists = os.path.exists(tblToView)
    if(tblExists == True):
        fileTbl = open(tblToView, 'r')  # open file for reading
        tblContent = fileTbl.read()  # gets strings in file to save to variable
        print(tblContent)  # prints variable contents
        fileTbl.close()  # close file
    else:
        print('!Failed to query table', tblToView, 'becaue it does not exist.')


def selectCategory(table, data):        #selecting multiple stuff to view COME BACK to function
    tblToView = table
    string = data
    firstCetegory = string[0]
    secondCetegory = string[1]
    whereCategory = string[5]

    tblExists = os.path.exists(tblToView)
    if(tblExists == True):
        fileTbl = open(tblToView, 'r')  # open file for reading
        tblContent = fileTbl.read()  # gets strings in file to save to variable
        print(tblContent)  # prints variable contents
        fileTbl.close()  # close file
    else:
        print('!Failed to query table', tblToView, 'becaue it does not exist.')


def alterTbl(valueInput, newValues):  # edit table adds to end of file
    tblToAlter = valueInput  # set value input to tblToAlter which is file
    addToTblValues = newValues  # set new values to addToTblValues
    fileTbl = open(tblToAlter, 'a')
    fileTbl.write(" | ")
    fileTbl.write("".join(addToTblValues))
    fileTbl.close()
    print('Table', tblToAlter, 'modified.')


def insertIntoTbl(table, newValues):  # insert into table
    tblToInsert = table
    addToTblValues = newValues  # set new values to addToTblValues
    fileTbl = open(tblToInsert, 'a')        #might need to add new line in bewteen the nextl line and this one
    fileTbl.write('\n')
    fileTbl.write("".join(addToTblValues))
    fileTbl.close()
    print('1 new record inserted.')

def updateTable(table, string):      #update table
    tblToUpdate = table
    data = string

    setValue = data[2]      #newval is first 
    whereValue = data[6]      #where val

    setCategory = data[0]      #first category
    whereCategory = data[4]     #second category

    nameName = 'name'
    priceName = 'price'
    
    if(setCategory == nameName and whereCategory == nameName):
        print('here')
        with open(tblToUpdate) as f:
            fileData = f.read().replace(whereValue, setValue)       #replaces values where is old val, set is new val
        with open(tblToUpdate, 'w') as f:
            f.write(fileData)
        
    elif(setCategory == priceName and whereCategory == nameName):
        with open(tblToUpdate, 'r') as file:       #open file to read
            with open('temp.txt', 'w') as newFile:      #open file to write
                for line in file:       #loop through file to write only lines that do not contain the mathing word
                    if whereValue in line:
                        line[2] = setValue
                        newFile.write(line)

def deleteFrom(table, string):
    tblToDeleteFrom = table
    data = string
    categoryName = data[1]
    searchFor = data[3]
    nameName = 'name'
    priceName = 'price'
    if(categoryName == nameName):
        with open(tblToDeleteFrom, 'r') as file:       #open file to read
            with open('temp.txt', 'w') as newFile:      #open file to write
                for line in file:       #loop through file to write only lines that do not contain the mathing word
                    if searchFor not in line.strip('\n'):
                        newFile.write(line)

        os.replace('temp.txt', tblToDeleteFrom)     #replace files
    elif(categoryName == priceName):
        with open(tblToDeleteFrom, 'r') as file:       #open file to read
            with open('temp.txt', 'w') as newFile:      #open file to write
                for line in file:       #loop through file to write only lines that do not contain the mathing word
                    if line > searchFor:
                        line.strip('\n')
                        newFile.write(line)


def main():
    baseDirectory = os.getcwd()  # define main cwd to use as base
    dbTestFile = sys.argv[1]  # save testfile name into variable
    f = open(dbTestFile, 'r')  # open file for reading
    commandLines = f.readlines()  # read lines into strings
    num = 0
    for line in commandLines:  # loop through each line
        # line alterings
        currentWorkingLine = line  # saves line into varriable of single line
        #currentWorkingLine = currentWorkingLine.replace('\n', '')      #need to account for end lin eventually!!!!
        currentWorkingLine = currentWorkingLine.replace(';', '')        #removes semicolon at end of each testline
        currentWorkingLine = currentWorkingLine.replace('(', ' ')       #replaces () characters with spaces to split by next
        currentWorkingLine = currentWorkingLine.replace(')', ' ')
        arrayLines = currentWorkingLine.split()  # split lines by spaces
        
        # checkNames
        createName = 'CREATE'
        dropName = 'DROP'
        dbName = 'DATABASE'
        tbName = 'TABLE'
        useName = 'USE'
        selectName = 'SELECT'
        starName = '*'
        selectLowName = 'select'
        alterName = 'ALTER'
        exitName = '.EXIT'
        exitLowName = '.exit'
        commentName = '--'
        name = ''
        insertName = 'insert'
        updateName = 'update'
        deleteName = 'delete'
        newLineName = '\n'
        # if statements to call functions
        if(arrayLines[0] == createName and arrayLines[1] == dbName):  # create db
            name = arrayLines[2]
            createDb(name)

        elif(arrayLines[0] == createName and arrayLines[1] == tbName):  #create table
            name = arrayLines[2]
            # editing data info to put into file
            data = " ".join(arrayLines[3:])
            finalData = data.replace(',', ' |')
            createTbl(finalData, name)

        elif(arrayLines[0] == dropName and arrayLines[1] == dbName):  # drop db
            name = arrayLines[2]
            dropDb(name)

        elif(arrayLines[0] == dropName and arrayLines[1] == tbName):  # drop tbl
            name = arrayLines[2]
            dropTbl(name)

        elif(arrayLines[0] == useName):  # use db
            name = arrayLines[1]
            useDb(baseDirectory, name)

        elif((arrayLines[0] == selectName and arrayLines[1] == starName) or (arrayLines[0] == selectLowName and arrayLines[1] == starName)):  # select
            name = arrayLines[3]
            selectTbl(name)

        elif(arrayLines[0] == selectName):      #selecting multiple
            data = " ".join(arrayLines[1:])
            data = data.replace(',', '')       #replaces , w nothing
            name = data[3]
            selectCategory(name, data)#need to do 

        elif(arrayLines[0] == alterName and arrayLines[1] == tbName):  # alter tbl
            name = arrayLines[2]
            # editing data info to put into file
            data = " ".join(arrayLines[4:])
            alterTbl(name, data)

        elif(arrayLines[0] == insertName):  # insert into tbl
            name = arrayLines[2]
            data = " ".join(arrayLines[4:])  # combines data to send into function
            data = data.replace(',', ' |')       #replaces , w " |"
            finalData = data.replace("'", "")      #replaces apostrophe w nothing
            insertIntoTbl(name, finalData)

        elif(arrayLines[0] == updateName):      #update table
            name = arrayLines[1]        #table name
            data = " ".join(arrayLines[3:])   #join = and rest to pass into function
            finalData = data.replace("'", "")
            updateTable(name, finalData)
            num += 1
            print(num, 'records modified.')

        elif(arrayLines[0] == deleteName):
            name = arrayLines[2]        #table name
            data = " ".join(arrayLines[3:])   #join = and rest to pass into function
            finalData = data.replace("'", "")
            deleteFrom(name, finalData)

        elif(arrayLines[0] == exitName or arrayLines[0] == exitLowName):  # exit
            print('All done.')
            quit()

        elif(commandLines == commentName):
            print("Error: unknown command or invalid arguements")

    f.close()


if __name__ == "__main__":
    main()