import sqlite3
import os
import sys

def MedicareCharges(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.TOTAL_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==5 or r[1]==10:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def MedicareRevenues(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.NET_PATIENT_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==5 or r[1]==10:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def MedicAIDCharges(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.TOTAL_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==6 or r[1]==11:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def MedicAIDRevenues(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.NET_PATIENT_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==6 or r[1]==11:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def OtherGovCharges(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.TOTAL_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==7:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def OtherGovRevenues(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.NET_PATIENT_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==7:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def CharityBadDebtCharges(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.TOTAL_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        #print(r)
        #print(type(r[0]))
        if r[1]==1 or r[1]==2 or r[1]==3 or r[1]==4:
            if r[0]!='':
                sum= sum + r[0]
                #print("Sum is :",sum)
    return sum

def CharityBadDebtRevenues(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.NET_PATIENT_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==1 or r[1]==2 or r[1]==3 or r[1]==4:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def NonMagCareCommCharges(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.TOTAL_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        #print(r)
        #print(type(r[0]))
        if r[1]==14 or r[1]==8:
            if r[0]!='':
                sum= sum + r[0]
                #print("Sum is :",sum)
    return sum

def NonMagCareCommRevenues(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.NET_PATIENT_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==14 or r[1]==8:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def MgdCareCommCharges(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.TOTAL_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        #print(r)
        #print(type(r[0]))
        if r[1]==12 or r[1]==13:
            if r[0]!='':
                sum= sum + r[0]
                #print("Sum is :",sum)
    return sum

def MgdCareCommRevenues(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.NET_PATIENT_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==12 or r[1]==13:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def EmployeeDiscounts(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.NET_PATIENT_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==16:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def OtherDeductions(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.NET_PATIENT_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==15 or r[1]==17 or r[1]==18 :
            if r[0]!='':
                sum= sum + r[0]
    return sum
