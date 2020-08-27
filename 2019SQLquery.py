import sqlite3
import os
import sys
import FLAHCAModule
import FLAHCAC2Module

def Which_Hospital(cursor):
    cursor.execute("""SELECT DISTINCT QUV_SUB_C3A.FILE_NBR FROM QUV_SUB_C3A""")
    result = cursor.fetchall()

    hospitallist = []
    for r in result:
        hospitallist.append(r[0])
        #print(r[0])
    #print(hospitallist)

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

def Charges_Validation(Total_Charges,C2_Total_Charges):
    if Total_Charges != C2_Total_Charges:
        print("Charges from C3A do not match those from C2")
    else:
        print("Charges from C3A and C2 match!! All good")

def Revenue_Validation(Total_Revenue,C2_Total_Revenue,Employee_Discounts,Other_Deductions,C2_Other_Op_Revenue):
    if Total_Revenue != (C2_Total_Revenue - Employee_Discounts - Other_Deductions - C2_Other_Op_Revenue):
        print("C3A Total Revenue :", Total_Revenue)
        print("c2 C2_Total_Revenue is :", C2_Total_Revenue)
        print("EE Discounts :", Employee_Discounts)
        print("Other deductions :", Other_Deductions)
        print("C2_Other_Op_Revenue", C2_Other_Op_Revenue)
        print("C2 Adjusted Revenue  :", (C2_Total_Revenue - Employee_Discounts - Other_Deductions - C2_Other_Op_Revenue))
        print("Total Revenue from C3A do not match those from C2")
    else:
        print("Revenue from C3A and C2 match!! All good")


def main(argv):
    db = os.getcwd()+r'\2019FLAHCAcsv.db'
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    print("This is from where the database is sourced:  ",db)

    hospital_ahca_number = Which_Hospital(cursor) #input("Enter IP Address: ")


    Medicare_Charges = FLAHCAModule.MedicareCharges(hospital_ahca_number,cursor)
    Medicare_Revenues = FLAHCAModule.MedicareRevenues(hospital_ahca_number,cursor)
    MedicAID_Charges = FLAHCAModule.MedicAIDCharges(hospital_ahca_number,cursor)
    MedicAID_Revenues = FLAHCAModule.MedicAIDRevenues(hospital_ahca_number,cursor)
    OtherGov_Charges = FLAHCAModule.OtherGovCharges(hospital_ahca_number,cursor)
    OtherGov_Revenues = FLAHCAModule.OtherGovRevenues(hospital_ahca_number,cursor)

    CharityBadDebt_Charges = FLAHCAModule.CharityBadDebtCharges(hospital_ahca_number,cursor)
    CharityBadDebt_Revenues = FLAHCAModule.CharityBadDebtRevenues(hospital_ahca_number,cursor)
    NonMagCareComm_Charges = FLAHCAModule.NonMagCareCommCharges(hospital_ahca_number,cursor)
    NonMagCareComm_Revenues = FLAHCAModule.NonMagCareCommRevenues(hospital_ahca_number,cursor)
    #CSN_Charges = FLAHCAModule.CSNCharges(hospital_ahca_number,cursor)
    #CSN_Revenues = FLAHCAModule.CSNRevenues(hospital_ahca_number,cursor)
    MgdCareComm_Charges = FLAHCAModule.MgdCareCommCharges(hospital_ahca_number,cursor)
    MgdCareComm_Revenues = FLAHCAModule.MgdCareCommRevenues(hospital_ahca_number,cursor)
    Employee_Discounts = FLAHCAModule.EmployeeDiscounts(hospital_ahca_number,cursor)
    Other_Deductions = FLAHCAModule.OtherDeductions(hospital_ahca_number,cursor)

    Total_Charges = Medicare_Charges + MedicAID_Charges + OtherGov_Charges + CharityBadDebt_Charges + NonMagCareComm_Charges + MgdCareComm_Charges
    Total_Revenue = Medicare_Revenues + MedicAID_Revenues + OtherGov_Revenues + CharityBadDebt_Revenues + NonMagCareComm_Revenues + MgdCareComm_Revenues
    print()
    print("ALL OF THESE BELOW ARE FROM C3A")
    print("_______________________________")
    print("Medicare Charges are   :", Medicare_Charges)
    print("Medicare Revenue is   :", Medicare_Revenues)
    print()
    print("Medicaid Charges are   :", MedicAID_Charges)
    print("Medicaid Revenues is   :", MedicAID_Revenues)
    print()
    print("Other Gov Charges are   :", OtherGov_Charges)
    print("Other Gov Revenue is   :", OtherGov_Revenues)
    print()
    print("Charity and Bad Charges are   :", CharityBadDebt_Charges)
    print("Charity and Bad Revenue is   :", CharityBadDebt_Revenues)
    print()
    print("Non-Managed Care Commercial Charges are   :", NonMagCareComm_Charges)
    print("Non-Managed Care Commercial Revenue is   :", NonMagCareComm_Revenues)
    print()
    print("Managed Care Commercial Charges are   :", MgdCareComm_Charges)
    print("Managed Care Commercial Revenue is   :", MgdCareComm_Revenues)
    print()
    print("Employee Discounts are   :", Employee_Discounts)
    print("Other Deductions are   :", Other_Deductions)
    print()
    print("Total Charges are :", Total_Charges)
    print("Total Revenue is :", Total_Revenue)
# Generation of numbers from c2
    C2_Total_Charges = FLAHCAC2Module.C2TotalCharges(hospital_ahca_number, cursor)
    C2_Total_Revenue = FLAHCAC2Module.C2TotalRevenue(hospital_ahca_number, cursor)
    C2_Other_Op_Revenue = FLAHCAC2Module.C2OtherOpRevenue(hospital_ahca_number, cursor)
    C2_Total_Op_Expense = FLAHCAC2Module.C2TotalOperatingExpense(hospital_ahca_number, cursor)
    Expense_ratio = round(C2_Total_Op_Expense/C2_Total_Charges,4) #Runding to four places
    print()
    print("ALL OF THESE BELOW ARE FROM C2")
    print("______________________________")
    print("C2 Total Charges are :", C2_Total_Charges)
    print("C2 Total Revenue is :", C2_Total_Revenue)
    print("C2 Other Operating Revenue is :", C2_Other_Op_Revenue)
    print("C2 Total Operating Expense is :", C2_Total_Op_Expense)
    print("Expense as a percent of charges is:", Expense_ratio)
#Does C3A totals match c2?#

    print()
    Charges_Validation(Total_Charges,C2_Total_Charges)
    Revenue_Validation(Total_Revenue,C2_Total_Revenue,Employee_Discounts,Other_Deductions,C2_Other_Op_Revenue)


if __name__ == "__main__":
  main(sys.argv)
