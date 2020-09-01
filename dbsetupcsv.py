
# Python code to demonstrate table creation and
# insertions with SQL

# importing module
import sqlite3
import xlrd
import os
import csv
import csv_to_sqlite

#These give files with text data types, which I must address
c3a = os.getcwd()+r'\QUV_SUB_C3A.txt'
c2 = os.getcwd()+r'\QUV_SUB_C2.txt'
hospital_info = os.getcwd()+r'\QUV_SUB_HOSPITAL_INFO.txt'
db = os.getcwd()+r'\2019FLAHCAcsv.db'
Initial_Construct = """CREATE TABLE IF NOT EXISTS results2019(
                                    hospitalahcanumber integer PRIMARY KEY,
                                    MedicareCharges integer,
                                    MedicareRevenues integer,
                                    MedicAIDCharges integer,
                                    MedicAIDRevenues integer,
                                    OtherGovCharges integer,
                                    OtherGovRevenues integer,
                                    CharityBadDebtCharges integer,
                                    CharityBadDebtRevenues integer,
                                    NonMagCareCommCharges integer,
                                    NonMagCareCommRevenues integer,
                                    MgdCareCommCharges integer,
                                    MgdCareCommRevenues integer,
                                    EmployeeDiscounts integer,
                                    OtherDeductions integer,
                                    MgdCareCommINPATIENTCharges integer,
                                    MgdCareCommINPATIENTRevenue integer,
                                    MgdCareCommOUTPATIENTCharges integer,
                                    MgdCareCommOUTPATIENTRevenue integer,
                                    TotalCharges integer,
                                    TotalRevenue integer,
                                    FOREIGN KEY (hospitalahcanumber)
                                        REFERENCES QUV_SUB_HOSPITAL_INFO
                                        (hospital_ahca_number)
                                )"""


print("C3A is at  :",c3a)
print("C2 is at  :",c2)
print("The Hospital infomation is at  :", hospital_info)
print("db is at  :",db)

conn = sqlite3.connect(db)
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS QUV_SUB_C3A")
cursor.execute("DROP TABLE IF EXISTS QUV_SUB_C2")
cursor.execute("DROP TABLE IF EXISTS QUV_SUB_HOSPITAL_INFO")
cursor.execute("DROP TABLE IF EXISTS results2019")
cursor.execute(Initial_Construct)

print("Tables dropped... ")
# all the usual options are supported
options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="utf8")
input_files = [c3a,c2,hospital_info] # pass in a list of CSV files
csv_to_sqlite.write_csv(input_files, "2019FLAHCAcsv.db", options)

#Create Table for the informaiton that we generate

print ()
print ("All Done! Bye, for now.")
print ()

#print ("I just impor"ted " %2B columns %2B " columns and " %2B rows %2B " rows to SQLite!")
