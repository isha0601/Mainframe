import os

# ✅ Add DB2 CLI driver path (update if Python version changes)
os.add_dll_directory(r"C:\Users\VICTUS\AppData\Local\Programs\Python\Python311\Lib\site-packages\clidriver\bin")

dns_import_error = None
try:
    import ibm_db
    IBM_DB_AVAILABLE = True
except Exception as e:
    ibm_db = None
    IBM_DB_AVAILABLE = False
    dns_import_error = e


# 🔹 DB2 connection details
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


def runQuery(query):
    if not IBM_DB_AVAILABLE:
        msg = (
            "ibm_db is not available. "
            "Install it with `python -m pip install ibm_db` and ensure the Microsoft Visual C++ Redistributable is installed. "
            f"Import error: {dns_import_error}"
        )
        return False, msg

    try:
        conn = ibm_db.connect(dsn, "", "")
        ibm_db.autocommit(conn, ibm_db.SQL_AUTOCOMMIT_ON)
        ibm_db.exec_immediate(conn, "SET CURRENT SCHEMA = VICTUS")
        stmt = ibm_db.exec_immediate(conn, query)
        ibm_db.close(conn)
        return True, stmt
    except Exception as e:
        return False, str(e)


def runSelectQuery(query):
    """Executes SELECT query and returns list of dictionaries"""
    if not IBM_DB_AVAILABLE:
        msg = (
            "ibm_db is not available. "
            "Install it with `python -m pip install ibm_db` and ensure the Microsoft Visual C++ Redistributable is installed. "
            f"Import error: {dns_import_error}"
        )
        return False, msg

    try:
        conn = ibm_db.connect(dsn, "", "")
        ibm_db.autocommit(conn, ibm_db.SQL_AUTOCOMMIT_ON)
        ibm_db.exec_immediate(conn, "SET CURRENT SCHEMA = VICTUS")
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


def runInsertQuery(query):
    """Executes INSERT/UPDATE/DELETE queries"""
    try:
        conn = ibm_db.connect(dsn, "", "")
        ibm_db.autocommit(conn, ibm_db.SQL_AUTOCOMMIT_ON)
        stmt = ibm_db.exec_immediate(conn, query)
        ibm_db.close(conn)
        return True, "✅ Insert/Update successful!"
    except Exception as e:
        return False, f"❌ Insert/Update failed: {e}"


# 🧠 Connection test
def test_connection():
    print("🔍 Testing DB2 connection...")
    success, result = runQuery("SELECT CURRENT DATE FROM SYSIBM.SYSDUMMY1")
    if success:
        print("✅ Connection successful!")
    else:
        print(f"❌ Connection failed: {result}")


# Run test
if __name__ == "__main__":
    test_connection()
