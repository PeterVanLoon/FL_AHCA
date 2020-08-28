import sqlite3
import os
import sys

def IPCharges(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.INPATIENT_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==12 or r[1]==13:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def IPRevenue(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.NET_INPATIENT_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==12 or r[1]==13:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def OPCharges(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.OUTPATIENT_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==12 or r[1]==13:
            if r[0]!='':
                sum= sum + r[0]
    return sum

def OPRevenue(hospital_ahca_number,cursor):
    sum = 0
    cursor.execute("""SELECT QUV_SUB_C3A.NET_OUTPATIENT_REVENUE, QUV_SUB_C3A.LINE_NUMBER FROM QUV_SUB_C3A WHERE QUV_SUB_C3A.[FILE_NBR]={}""".format(hospital_ahca_number,))
    result = cursor.fetchall()
    for r in result:
        if r[1]==12 or r[1]==13:
            if r[0]!='':
                sum= sum + r[0]
    return sum
