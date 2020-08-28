

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

def IPOP_Validation(MgdCareComm_Charges, MgdCareComm_Revenues, MgdCareComm_INPATIENT_Charges, MgdCareComm_OUTPATIENT_Charges, MgdCareComm_INPATIENT_Revenue, MgdCareComm_OUTPATIENT_Revenue):
    if MgdCareComm_Charges != MgdCareComm_INPATIENT_Charges + MgdCareComm_OUTPATIENT_Charges:
        print("BAD BAD STUFF: Manage Care Commercial Total Charges from C3A do not match the Sum of INPATIENT and OUTPATIENT Managed Care Commercial Charges")
    else:
        print("Manage Care Commercial Total Charges from C3A DO MATCH the Sum of INPATIENT and OUTPATIENT Managed Care Commercial Charges.  All good")
    if MgdCareComm_Revenues != MgdCareComm_INPATIENT_Revenue + MgdCareComm_OUTPATIENT_Revenue:
        print("BAD BAD STUFF: Manage Care Commercial Total Revenue from C3A do not match the Sum of INPATIENT and OUTPATIENT Managed Care Commercial Revenue")
    else:
        print("Manage Care Commercial Total Revenue from C3A DO MATCH the Sum of INPATIENT and OUTPATIENT Managed Care Commercial Revenue.  All good")
