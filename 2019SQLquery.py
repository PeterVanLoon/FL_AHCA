import sqlite3
import os
import sys
import FLAHCAModule

def Which_Hospital(cursor):
    cursor.execute("""SELECT DISTINCT QUV_SUB_C3A.FILE_NBR FROM QUV_SUB_C3A""")
    result = cursor.fetchall()

    hospitallist = []
    for r in result:
        hospitallist.append(r[0])
        #print(r[0])
    print(hospitallist)

    while True:
        try:
            hospital_ahca_number = int(input("Please enter the Hospital's Florida AHCA number:"))
            if hospital_ahca_number in hospitallist:
                print("That is a valid AHCA number")
                break
            else:
                print("NOT A VALID AHCA NUMBER - Please enter a number that is vaild")
        except:
            continue
    return hospital_ahca_number

def main(argv):
    db = os.getcwd()+r'\2019FLAHCAcsv.db'
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    print(db)
    hospital_ahca_number = Which_Hospital(cursor) #input("Enter IP Address: ")
    Medicare_Charges = FLAHCAModule.MedicareCharges(hospital_ahca_number,cursor)
    Medicare_Revenues = FLAHCAModule.MedicareRevenues(hospital_ahca_number,cursor)
    print("Medicare Charges are   :", Medicare_Charges)
    print("Medicare Revenues are   :", Medicare_Revenues)

if __name__ == "__main__":
  main(sys.argv)
