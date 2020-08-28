# Python code to demonstrate table creation and
# insertions with SQL
##

# importing module
import sqlite3
import xlrd
import os


book = xlrd.open_workbook(os.getcwd()+'\QUV_SUB_C3A Query.xlsx')
sheet = book.sheet_by_name('c3a')
#sheet.col(1)

print("Sheet is  :",sheet)
# connecting to the database
connection = sqlite3.connect("2019FLAHCA.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
clear_table = "DROP TABLE IF EXISTS quv_sub_c3a"
make_table = """CREATE TABLE IF NOT EXISTS quv_sub_c3a (
row FLOAT PRIMARY KEY,
file_number FLOAT,
line_number VARCHAR(2),
inpatient_revenue TEXT,
outpatient_revenue TEXT,
total_revenue TEXT);"""

# execute the statement
crsr.execute(clear_table)
crsr.execute(make_table)

# SQL command to insert the data in the table
#sql_command = """INSERT INTO quv_sub_c3a (file_number, line_number, inpatient_revenue,
#outpatient_revenue, total_revenue) VALUES(?,?,?,?,?)"""
sql_command = """INSERT INTO quv_sub_c3a VALUES(?,?,?,?,?,?)"""

counter = 0

for r in range(1, sheet.nrows):

    #print("First  :",type(sheet.cell(r,1).value))
    print(r)
    print(type(sheet.cell(r,0).value))

    print(sheet.cell(r,0).value)
    row                   = sheet.cell(r,0).value
    file_number           = sheet.cell(r,1).value
    line_number           = sheet.cell(r,3).value
    #print(line_number)
    inpatient_revenue     = sheet.cell(r,4).value
    outpatient_revenue    = sheet.cell(r,5).value
    total_revenue         = sheet.cell(r,6).value

		# Assign values from each row
    values = (row, file_number, line_number, inpatient_revenue,
    outpatient_revenue, total_revenue)
    print(values)
    print("row = ", row)
    print("Second   :",type(sheet.cell(r,0).value))

		# Execute sql Query
    crsr.execute(sql_command, values)
    print("Third   :",type(sheet.cell(r,0).value))
    counter += 1
    # I have to figure out how many rows in the excel worksheet before I
    # run this.  I treid to read "empty cell" to break and ould not make it
    #wor
    if counter == 1933:
        break


# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()

# close the connection
connection.close()

print ()
print ("All Done! Bye, for now.")
print ()
columns = str(sheet.ncols)
rows = str(sheet.nrows)
#print ("I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to SQLite!")
print(rows)

"""
 storage.append(comment.author)
            c.execute("INSERT INTO users (id, Username, subreddit, comment) VALUES(?,?,?,?)", (str(comment.id), str(comment.author), str(comment.subreddit), str(comment.body)))
            conn.commit()  """
