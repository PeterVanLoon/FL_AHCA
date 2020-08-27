import sqlite3
import os
import sys

def C2TotalCharges(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C2.AMOUNT, QUV_SUB_C2.LINE_NUMBER FROM QUV_SUB_C2 WHERE QUV_SUB_C2.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==3:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def C2TotalRevenue(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C2.AMOUNT, QUV_SUB_C2.LINE_NUMBER FROM QUV_SUB_C2 WHERE QUV_SUB_C2.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==7:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def C2OtherOpRevenue(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C2.AMOUNT, QUV_SUB_C2.LINE_NUMBER FROM QUV_SUB_C2 WHERE QUV_SUB_C2.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==6:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def C2TotalOperatingExpense(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C2.AMOUNT, QUV_SUB_C2.LINE_NUMBER FROM QUV_SUB_C2 WHERE QUV_SUB_C2.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==12:
            if r[0]!='':
                sum= sum + r[0]
    return sum
