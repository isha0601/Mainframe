import os

# Fix DLL import issue for ibm_db on Windows
os.add_dll_directory(r"C:\Users\VICTUS\AppData\Local\Programs\Python\Python311\Lib\site-packages\clidriver\bin")

# Try importing ibm_db safely
dns_import_error = None
try:
    import ibm_db
    IBM_DB_AVAILABLE = True
except Exception as e:
    ibm_db = None
    IBM_DB_AVAILABLE = False
    dns_import_error = e

# --- DB2 Connection Config ---
dsn_hostname = "localhost"
dsn_uid = "db2admin"
dsn_pwd = "isha0601"
dsn_database = "MAINFRM"
dsn_port = "25000"
dsn_protocol = "TCPIP"

dsn = (
    f"DATABASE={dsn_database};"
    f"HOSTNAME={dsn_hostname};"
    f"PORT={dsn_port};"
    f"PROTOCOL={dsn_protocol};"
    f"UID={dsn_uid};"
    f"PWD={dsn_pwd};"
)

# --- Helper Functions ---
def runQuery(query):
    """Execute a general SQL query (INSERT, UPDATE, DELETE, etc.)"""
    if not IBM_DB_AVAILABLE:
        return False, f"ibm_db not available: {dns_import_error}"
    try:
        conn = ibm_db.connect(dsn, "", "")
        ibm_db.autocommit(conn, ibm_db.SQL_AUTOCOMMIT_ON)
        stmt = ibm_db.exec_immediate(conn, query)
        ibm_db.close(conn)
        return True, " Query executed successfully!"
    except Exception as e:
        return False, str(e)


def runSelectQuery(query):
    """Executes a SELECT query and returns list of dicts"""
    if not IBM_DB_AVAILABLE:
        return False, f"ibm_db not available: {dns_import_error}"
    try:
        conn = ibm_db.connect(dsn, "", "")
        ibm_db.autocommit(conn, ibm_db.SQL_AUTOCOMMIT_ON)
        stmt = ibm_db.exec_immediate(conn, query)
        result = []
        row = ibm_db.fetch_assoc(stmt)
        while row:
            result.append(row)
            row = ibm_db.fetch_assoc(stmt)
        ibm_db.close(conn)
        return True, result
    except Exception as e:
        return False, str(e)







def mergeEmployeeData():
    try:
        conn = ibm_db.connect(dsn, "", "")
        merge_sql = """
            INSERT INTO EMPLOYEE_MATCHED (EMP_ID, NAME, SALARY, DEPARTMENT, BONUS)
            SELECT f1.ID1, f1.NAME, f1.SALARY, f2.DEPARTMENT, f2.BONUS
            FROM EMPLOYEE_FILE1 f1
            JOIN EMPLOYEE_FILE2 f2 ON f1.ID1 = f2.ID2
        """
        ibm_db.exec_immediate(conn, merge_sql)
        ibm_db.close(conn)
        return True, " Merge completed"
    except Exception as e:
        return False, str(e)













