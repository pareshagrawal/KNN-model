import mysql.connector as c
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWD = os.getenv('DB_PASSWD')

mydb = c.connect(host="localhost",user=DB_USER,passwd=DB_PASSWD,database="demo")
myCursor = mydb.cursor()

# TO CREATE A NEW DATABASE 'DEMO'
#
# mydb = c.connect(host="localhost",user="root",passwd="@1234567")
# myCursor = mydb.cursor()
#
# query = "create database demo"
# myCursor.execute(query)
#
# print("created database successfully")

def insert():
    sid = int(input("Enter Student id = "))
    name = input("Enter Student Name = ")
    branch = input("Enter the Student branch = ")

    query = "insert into Student(Sid,name,branch) values({},'{}','{}')".format(sid,name,branch)
    myCursor.execute(query)
    mydb.commit()

    if myCursor.rowcount > 0:
        print("inserted successfully")

def update():
    setColumn = input("Enter the set column name = ")
    setValue = input("Enter the set value = ")
    whereColumn = input("Enter the where column name = ")
    whereValue = input("Enter the where value = ")

    if setColumn == 'sid' or setColumn == 'Sid':
        setValue = int(setValue)
    if whereColumn == 'sid' or whereColumn == 'Sid':
        whereValue = int(whereValue)

    query = "update Student set {}='{}' where {}='{}'".format(setColumn,setValue,whereColumn,whereValue)
    myCursor.execute(query)
    mydb.commit()

    if myCursor.rowcount > 0:
        print("updated successfully")

def delete():
    whereColumn = input("Enter the where column name = ")
    whereValue = input("Enter the where value = ")

    if whereColumn == 'sid' or whereColumn == 'Sid':
        whereValue = int(whereValue)

    query = "delete from Student where {}='{}'".format(whereColumn, whereValue)
    myCursor.execute(query)
    mydb.commit()

    if myCursor.rowcount > 0:
        print("deleted successfully")


# TO CONVERT MYSQL DATA INTO DATAFRAMES AND THAT DATAFRAMES INTO DICTIONARY
#
# import pandas as pd
#
# mydb = c.connect(host="localhost",user="root",passwd="@1234567",database="demo")
#
# myCursor = mydb.cursor()
#
# query = "select * from student"
# myCursor.execute(query)
#
# df = pd.DataFrame(myCursor)
#
# print(df.to_dict())
# print(df.to_dict('list'))
# print(df.to_dict('records'))
