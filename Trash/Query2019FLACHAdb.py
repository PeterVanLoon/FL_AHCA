import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * WHERE type='table' ORDER BY name")

    rows = cur.fetchall()

    for row in rows:
        print(row)

if __name__ == '__main__':
    db_file = r"C:\Users\Peter\OneDrive\3_AHCA\2019FLAHCA.db"
    conn = create_connection(db_file)
    select_all_tasks(conn)

print()
print("Moving")
print()
