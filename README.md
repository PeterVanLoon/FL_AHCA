# FL_AHCA
Manipulating Florida AHCA data
The Florida Agency for Health Care Administration(FL AHCA) generates a lot of information and data.

This is an effort to pull data from FL AHCA financial information into a SQLite database using Python, and then using that data to develop financial analyses of individual hospitals..
The data from AHCA is in an Access database.  For 2019, the file name is "2019QuadrantDataDissemination.mdb".  Three tables from this file are used; QUV_SUB_C2, QUV_SUB_C3A, and QUV_SUB_HOSPITAL_INFO.
QUV_SUB_C2: Contains high level information on charges, deductions and the hospital's profit and loss.  The information sourced from here is Total Charges, Total Revenue, Operating Expense and Margin. 
QUV_SUB_C3A: This file contains detailed information by product line, i.e. Medicare, Medicaid, Other Government, Charity and Bad Debt, Non Managed Care Commercial and Managed Care Commercial information.  It breaks down InPatient and Outpatient charges and revenues, which is germane to the Managed Care Commercial informaiton.
QUV_SUB_HOSPITAL_INFO: This includes the Hospital information, specfically the hospital name.

For all three of these tables, the KEY is FILE_NBR, which is the FL AHCA hospital number.  For the most hospitals, but not all, the FL AHCA hospital number is the Medicare Number of the hospital.  

FILE PREPARATION
Each of these three tables needs to be exported as an individual CSV file to a common folder with the file names QUV_SUB_C2.txt, QUV_SUB_C3A.txt, and QUV_SUB_HOSPITAL_INFO.txt.
With these three text files staged, a succession of Python files are used to generate a new database.  The Access database is not accessed directly because I could not get the pyodbc module to work.  

GENERATE A DATABASE
Run "dbsetupcsv.py".  This will generate a SQLite database which will be used to develop and/or query informaiton to be used to generate analyses.  
