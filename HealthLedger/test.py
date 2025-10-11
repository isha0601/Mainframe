import os
os.add_dll_directory(r"C:\Users\VICTUS\AppData\Local\Programs\Python\Python311\Lib\site-packages\clidriver\bin")
import ibm_db

dsn = (
    "DATABASE=MAINFRM;"
    "HOSTNAME=localhost;"
    "PORT=25000;"
    "PROTOCOL=TCPIP;"
    "UID=db2admin;"
    "PWD=isha0601;"
)

try:
    conn = ibm_db.connect(dsn, "", "")
    print("✅ Connected successfully to DB2!")
    stmt = ibm_db.exec_immediate(conn, "SELECT * FROM EMPLOYEE_MATCHED FETCH FIRST 5 ROWS ONLY")
    row = ibm_db.fetch_assoc(stmt)
    while row:
        print(row)
        row = ibm_db.fetch_assoc(stmt)
    ibm_db.close(conn)
except Exception as e:
    print("❌ Connection or query failed:", e)
