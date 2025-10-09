try:
    import ibm_db  # type: ignore
    IBM_DB_AVAILABLE = True
except Exception:
    ibm_db = None
    IBM_DB_AVAILABLE = False


dsn_hostname = "localhost"
dsn_uid = "db2admin"
dsn_pwd = "2425455"
dsn_database = "HOSPITAL"
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
    """Execute a non-SELECT query against DB2.

    Returns (True, stmt) on success or (False, error_message) on failure.
    If `ibm_db` isn't available, returns a descriptive error instead of raising.
    """
    if not IBM_DB_AVAILABLE:
        return False, "ibm_db is not available in the environment"

    try:
        conn = ibm_db.connect(dsn, "", "")
        ibm_db.autocommit(conn, ibm_db.SQL_AUTOCOMMIT_ON)
        ibm_db.exec_immediate(conn, "SET CURRENT SCHEMA = NEJET")
        stmt = ibm_db.exec_immediate(conn, query)
        ibm_db.close(conn)
        return True, stmt
    except Exception as e:
        return False, str(e)


def runSelectQuery(query):
    """Executes SELECT query and returns list of dictionaries"""
    if not IBM_DB_AVAILABLE:
        return False, "ibm_db is not available in the environment"

    try:
        conn = ibm_db.connect(dsn, "", "")
        ibm_db.autocommit(conn, ibm_db.SQL_AUTOCOMMIT_ON)
        ibm_db.exec_immediate(conn, "SET CURRENT SCHEMA = NEJET")
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