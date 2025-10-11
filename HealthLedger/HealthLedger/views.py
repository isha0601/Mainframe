from django.shortcuts import render
from django.http import JsonResponse
from . import DB2Query
from datetime import datetime

def DASH(request):
    return render(request, "src/DASH.html")

def get_stats(request):
    query = """
        SELECT 
            COUNT(*) AS TOTAL_RECORDS,
            COALESCE(SUM(SALARY), 0) AS TOTAL_SALARY,
            COALESCE(SUM(BONUS), 0) AS TOTAL_BONUS,
            COALESCE(AVG(SALARY), 0) AS AVG_SALARY
        FROM EMPLOYEE_MATCHED
    """
    ok, result = DB2Query.runSelectQuery(query)
    if not ok:
        return JsonResponse({"error": result}, status=500)

    row = result[0] if result else {}
    return JsonResponse({
        "total_records": int(row.get("TOTAL_RECORDS", 0)),
        "total_salary": float(row.get("TOTAL_SALARY", 0)),
        "total_bonus": float(row.get("TOTAL_BONUS", 0)),
        "avg_salary": float(row.get("AVG_SALARY", 0)),
    })


def get_matched(request):
    query = "SELECT * FROM EMPLOYEE_MATCHED ORDER BY EMP_ID"
    ok, result = DB2Query.runSelectQuery(query)
    if not ok:
        return JsonResponse({"error": result}, status=500)
    return JsonResponse(result, safe=False)


def get_recent_activity(request):
    data = [
        {"log_name": "Matched Records Refreshed", "log_desc": "EMPLOYEE_MATCHED table updated successfully."},
        {"log_name": "Stats Computed", "log_desc": "Salary and bonus aggregates calculated."},
        {"log_name": "User Access", "log_desc": "Admin viewed dashboard."},
    ]
    return JsonResponse({"activities": data})

    