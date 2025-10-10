dns_import_error = None
try:
    import ibm_db
    IBM_DB_AVAILABLE = True
except Exception as e:
    ibm_db = None
    IBM_DB_AVAILABLE = False
    dns_import_error = e

dsn_hostname = "localhost"
dsn_uid = "db2admin"
dsn_pwd = ""
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
            "ibm_db is not available in the Python environment. "
            "Install it with `python -m pip install ibm_db` and ensure the Microsoft Visual C++ Redistributable is present if on Windows. "
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
            "ibm_db is not available in the Python environment. "
            "Install it with `python -m pip install ibm_db` and ensure the Microsoft Visual C++ Redistributable is present if on Windows. "
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
