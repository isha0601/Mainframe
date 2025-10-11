

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from . import DB2Query
from django.views.decorators.csrf import csrf_exempt
import json

# ---------------- Dashboard ----------------
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

# ---------------- Employee APIs ----------------
def add_new_data(request):
    emp_id = request.GET.get("emp_id")
    name = request.GET.get("name")
    salary = request.GET.get("salary") or 0
    department = request.GET.get("department")
    bonus = request.GET.get("bonus") or 0

    if not emp_id or not name or not department:
        return JsonResponse({"status": False, "error": "Missing required fields."})

    query = f"""
        INSERT INTO EMPLOYEE_MATCHED (EMP_ID, NAME, SALARY, DEPARTMENT, BONUS)
        VALUES ('{emp_id}', '{name}', {salary}, '{department}', {bonus})
    """
    ok, result = DB2Query.runInsertQuery(query)
    if not ok:
        return JsonResponse({"status": False, "error": result})
    return JsonResponse({"status": True})

def get_employee(request):
    emp_id = request.GET.get("emp_id")
    query = f"SELECT * FROM EMPLOYEE_MATCHED WHERE EMP_ID='{emp_id}'"
    ok, result = DB2Query.runSelectQuery(query)
    if not ok or not result:
        return JsonResponse({"status": False, "error": "Employee not found"})
    return JsonResponse({"status": True, "employee": result[0]})

@csrf_exempt
def update_employee(request):
    if request.method != "POST":
        return JsonResponse({"status": False, "error": "Invalid request method"})
    try:
        data = json.loads(request.body)
        emp_id = data.get("emp_id")
        name = data.get("name")
        salary = data.get("salary") or 0
        department = data.get("department")
        bonus = data.get("bonus") or 0

        query = f"""
            UPDATE EMPLOYEE_MATCHED
            SET NAME='{name}', SALARY={salary}, DEPARTMENT='{department}', BONUS={bonus}
            WHERE EMP_ID='{emp_id}'
        """
        ok, result = DB2Query.runInsertQuery(query)
        if not ok:
            return JsonResponse({"status": False, "error": result})
        return JsonResponse({"status": True})
    except Exception as e:
        return JsonResponse({"status": False, "error": str(e)})

@csrf_exempt
def delete_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        emp_id = data.get('emp_id')
        try:
            query = f"DELETE FROM EMPLOYEE_MATCHED WHERE EMP_ID='{emp_id}'"
            ok, result = DB2Query.runInsertQuery(query)
            if not ok:
                return JsonResponse({'status': False, 'error': result})
            return JsonResponse({'status': True})
        except Exception as e:
            return JsonResponse({'status': False, 'error': str(e)})

# ---------------- Employee Pages ----------------
def view_all_employees(request):
    query = "SELECT * FROM EMPLOYEE_MATCHED ORDER BY EMP_ID"
    ok, employees = DB2Query.runSelectQuery(query)
    if not ok:
        employees = []

    total_salary = sum(emp.get('SALARY',0) for emp in employees)
    total_bonus = sum(emp.get('BONUS',0) for emp in employees)

    context = {
        'employees': employees,
        'total_employees': len(employees),
        'total_salary': total_salary,
        'total_bonus': total_bonus
    }
    return render(request, 'VIEW_ALL.html', context)

def create_employee(request):
    return render(request, 'CREATE.html')

def update_employee_page(request, emp_id):
    query = f"SELECT * FROM EMPLOYEE_MATCHED WHERE EMP_ID='{emp_id}'"
    ok, result = DB2Query.runSelectQuery(query)
    if not ok or not result:
        return render(request, 'UPDATE.html', {'error': 'Employee not found'})
    employee = result[0]
    return render(request, 'UPDATE.html', {'employee': employee})
