import sqlite3
import os
import sys
import FLAHCAC3AModule
import FLAHCAC2Module
import FLAHCAC3AIPOPModule
import FLAHCAValidations
#import dbsetupcsv



def main(argv):
    db = os.getcwd()+r'\2019FLAHCAcsv.db'
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    print("This is from where the database is sourced:  ",db)

    # This is from where I get the FL AHCA number and check its validity
    hospital_ahca_number = FLAHCAValidations.Which_Hospital(cursor)


    Medicare_Charges =\
        FLAHCAC3AModule.MedicareCharges(hospital_ahca_number,cursor)
    Medicare_Revenues =\
        FLAHCAC3AModule.MedicareRevenues(hospital_ahca_number,cursor)
    MedicAID_Charges = \
        FLAHCAC3AModule.MedicAIDCharges(hospital_ahca_number,cursor)
    MedicAID_Revenues = \
        FLAHCAC3AModule.MedicAIDRevenues(hospital_ahca_number,cursor)
    OtherGov_Charges = \
        FLAHCAC3AModule.OtherGovCharges(hospital_ahca_number,cursor)
    OtherGov_Revenues = \
        FLAHCAC3AModule.OtherGovRevenues(hospital_ahca_number,cursor)

    CharityBadDebt_Charges = \
        FLAHCAC3AModule.CharityBadDebtCharges(hospital_ahca_number,cursor)
    CharityBadDebt_Revenues = \
        FLAHCAC3AModule.CharityBadDebtRevenues(hospital_ahca_number,cursor)
    NonMagCareComm_Charges =  \
        FLAHCAC3AModule.NonMagCareCommCharges(hospital_ahca_number,cursor)
    NonMagCareComm_Revenues = \
        FLAHCAC3AModule.NonMagCareCommRevenues(hospital_ahca_number,cursor)
    #CSN_Charges = FLAHCAModule.CSNCharges(hospital_ahca_number,cursor)
    #CSN_Revenues = FLAHCAModule.CSNRevenues(hospital_ahca_number,cursor)
    MgdCareComm_Charges = \
        FLAHCAC3AModule.MgdCareCommCharges(hospital_ahca_number,cursor)
    MgdCareComm_Revenues = \
        FLAHCAC3AModule.MgdCareCommRevenues(hospital_ahca_number,cursor)
    Employee_Discounts = \
        FLAHCAC3AModule.EmployeeDiscounts(hospital_ahca_number,cursor)
    Other_Deductions = \
        FLAHCAC3AModule.OtherDeductions(hospital_ahca_number,cursor)

    Total_Charges = Medicare_Charges + MedicAID_Charges + OtherGov_Charges \
        + CharityBadDebt_Charges + NonMagCareComm_Charges + MgdCareComm_Charges
    Total_Revenue = Medicare_Revenues + MedicAID_Revenues + OtherGov_Revenues \
        + CharityBadDebt_Revenues + NonMagCareComm_Revenues \
        + MgdCareComm_Revenues


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
    C2_Total_Charges = \
        FLAHCAC2Module.C2TotalCharges(hospital_ahca_number, cursor)
    C2_Total_Revenue = \
        FLAHCAC2Module.C2TotalRevenue(hospital_ahca_number, cursor)
    C2_Other_Op_Revenue = \
        FLAHCAC2Module.C2OtherOpRevenue(hospital_ahca_number, cursor)
    C2_Total_Op_Expense = \
        FLAHCAC2Module.C2TotalOperatingExpense(hospital_ahca_number, cursor)
    Expense_ratio = round(C2_Total_Op_Expense/C2_Total_Charges,4) #Runding to four places
    print()
    print("ALL OF THESE BELOW ARE FROM C2")
    print("______________________________")
    print("C2 Total Charges are :", C2_Total_Charges)
    print("C2 Total Revenue is :", C2_Total_Revenue)
    print("C2 Other Operating Revenue is :", C2_Other_Op_Revenue)
    print("C2 Total Operating Expense is :", C2_Total_Op_Expense)
    print("Expense as a percent of charges is:", Expense_ratio)

# Generation of IP and OP numbers for Commercial PPO and FLAHCAModule
    MgdCareComm_INPATIENT_Charges = \
        FLAHCAC3AIPOPModule.IPCharges(hospital_ahca_number,cursor)
    MgdCareComm_INPATIENT_Revenue = \
        FLAHCAC3AIPOPModule.IPRevenue(hospital_ahca_number,cursor)
    MgdCareComm_OUTPATIENT_Charges = \
        FLAHCAC3AIPOPModule.OPCharges(hospital_ahca_number,cursor)
    MgdCareComm_OUTPATIENT_Revenue = \
        FLAHCAC3AIPOPModule.OPRevenue(hospital_ahca_number,cursor)


    print()
    print("ALL OF THESE BELOW ARE FROM C3A")
    print("_______________________________")
    print("Managed Care Commercial INPATIENT Charges are   :", \
        MgdCareComm_INPATIENT_Charges, type(MgdCareComm_INPATIENT_Charges))
    print("Managed Care Commercial INPATIENT Revenue is   :", \
        MgdCareComm_INPATIENT_Revenue)
    print("Managed Care Commercial OUTPATIENT Charges are   :", \
        MgdCareComm_OUTPATIENT_Charges)
    print("Managed Care Commercial OUTPATIENT Revenue is   :", \
        MgdCareComm_OUTPATIENT_Revenue)

#Does C3A totals match c2?#

    print()
    print("VALIDATION SECTION")
    print("_______________________________")
    FLAHCAValidations.Charges_Validation(Total_Charges,C2_Total_Charges)
    FLAHCAValidations.Revenue_Validation(Total_Revenue,C2_Total_Revenue,\
        Employee_Discounts,Other_Deductions,C2_Other_Op_Revenue)
    FLAHCAValidations.IPOP_Validation(MgdCareComm_Charges, \
        MgdCareComm_Revenues,MgdCareComm_INPATIENT_Charges, \
        MgdCareComm_OUTPATIENT_Charges,MgdCareComm_INPATIENT_Revenue, \
        MgdCareComm_OUTPATIENT_Revenue)

#Create a table for the informaiton we source above
    print(hospital_ahca_number, type(hospital_ahca_number))
    print(Medicare_Charges, type(Medicare_Charges))
    print(Medicare_Revenues, type(Medicare_Revenues))


    cursor.execute("""INSERT INTO results2019 (hospitalahcanumber,
    MedicareCharges,MedicareRevenues,MedicAIDCharges,
    MedicAIDRevenues,OtherGovCharges,OtherGovRevenues,CharityBadDebtCharges,
    CharityBadDebtRevenues,NonMagCareCommCharges,NonMagCareCommRevenues,
    MgdCareCommCharges,MgdCareCommRevenues,EmployeeDiscounts,OtherDeductions,
    MgdCareCommINPATIENTCharges,MgdCareCommINPATIENTRevenue,
    MgdCareCommOUTPATIENTCharges,MgdCareCommOUTPATIENTRevenue,
    TotalCharges,TotalRevenue)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
    (hospital_ahca_number,Medicare_Charges,Medicare_Revenues,MedicAID_Charges,
    MedicAID_Revenues,OtherGov_Charges, OtherGov_Revenues,
    CharityBadDebt_Charges, CharityBadDebt_Revenues, NonMagCareComm_Charges,
    NonMagCareComm_Revenues, MgdCareComm_Charges, MgdCareComm_Revenues,
    Employee_Discounts,Other_Deductions,MgdCareComm_INPATIENT_Charges,
    MgdCareComm_INPATIENT_Revenue, MgdCareComm_OUTPATIENT_Charges,
    MgdCareComm_OUTPATIENT_Revenue, Total_Charges,Total_Revenue))
    conn.commit()
    cursor.close()


if __name__ == "__main__":
  main(sys.argv)
