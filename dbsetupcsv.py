
# Python code to demonstrate table creation and
# insertions with SQL

# importing module
import sqlite3
import xlrd
import os
import csv
import csv_to_sqlite

c3a = os.getcwd()+r'\QUV_SUB_C3A.txt'
c2 = os.getcwd()+r'\QUV_SUB_C2.txt'
db = os.getcwd()+r'\2019FLAHCAcsv.db'

print("C3A is at  :",c3a)
print("C2 is at  :",c2)
print("db is at  :",db)

conn = sqlite3.connect(db)
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS QUV_SUB_C3A")
cursor.execute("DROP TABLE IF EXISTS QUV_SUB_C2")


print("Table dropped... ")
# all the usual options are supported
options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="utf8")
input_files = [c3a,c2] # pass in a list of CSV files
csv_to_sqlite.write_csv(input_files, "2019FLAHCAcsv.db", options)



"""
with open(book, newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(', '.join(row))

"""
print ()
print ("All Done! Bye, for now.")
print ()

#print ("I just impor"ted " %2B columns %2B " columns and " %2B rows %2B " rows to SQLite!")
