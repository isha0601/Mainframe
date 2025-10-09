from django.shortcuts import render
from django.http import JsonResponse
from . import DB2Query

def CREATE(request):
    # Employee-first: render employee create page
    return render(request, 'src/CREATE_employee.html')
def UPDATE(request):
    # Employee-first: render employee update page
    return render(request, 'src/UPDATE_employee.html')

# Employee pages
def EMP_CREATE(request):
    return render(request, 'src/CREATE_employee.html')

def EMP_UPDATE(request):
    return render(request, 'src/UPDATE_employee.html')

def get_data_by_uid(request):
    # Repurposed for employee: accept `uid` query param as EID for backward compatibility
    eid = request.GET.get('uid') or request.GET.get('eid')
    if not eid:
        return JsonResponse({"error": "EID is required"}, status=400)

    query = f"SELECT * FROM employee_data WHERE eid = '{eid}'"
    success, result = DB2Query.runSelectQuery(query)

    if success and result:
        # find payroll/payment info
        payroll = result[0].get('PAYROLL_NUM', '')
        payment_query = f"SELECT * FROM employee_register WHERE eid = '{result[0].get('EID')}' AND PAYROLL_NUM = '{payroll}'"
        payment_done_success, payment_done = DB2Query.runSelectQuery(payment_query)
        if payment_done_success and payment_done:
            send_data = {
                "payrollNum": result[0].get('PAYROLL_NUM'),
                "eid": result[0].get('EID'),
                "name": result[0].get('NAME'),
                "date": str(result[0].get('DATE')),
                "amount": float(result[0].get('AMOUNT', 0)),
                "paidAmount": float(payment_done[0].get('PAID_AMT', 0)),
                "remark": "Paid" if payment_done[0].get('PAID_AMT', 0) >= result[0].get('AMOUNT', 0) else "Pending",
            }
            return JsonResponse([send_data], safe=False)

    return JsonResponse([], safe=False)

def update_payment(request):
    # Repurposed for employee: accept `uid` as EID for backward compatibility
    eid = request.GET.get('uid') or request.GET.get('eid')
    payroll_num = request.GET.get('invoice_num') or request.GET.get('payroll_num')
    paid_amount = request.GET.get('paid_amount')

    if not eid or not payroll_num or not paid_amount:
        return JsonResponse({"error": "eid, payroll_num, and paid_amount are required"}, status=400)

    try:
        paid_amount = float(paid_amount)
    except ValueError:
        return JsonResponse({"error": "paid_amount must be a number"}, status=400)

    query = f"UPDATE employee_register SET PAID_AMT = {paid_amount} WHERE EID = '{eid}' AND PAYROLL_NUM = '{payroll_num}'"
    success, msg = DB2Query.runQuery(query)
    if success:
        return JsonResponse({"message": "Payment updated successfully"})
    else:
        return JsonResponse({"error": f"Failed to update payment: {msg}"}, status=500)
    
def load_data(request):
    # Load employee rows instead of patient rows
    query = "SELECT * FROM employee_data FETCH FIRST 100 ROWS ONLY"
    success, result = DB2Query.runSelectQuery(query)

    if success and result:
        formatted_result = []
        for row in result:
            paid_query = f"SELECT PAID_AMT FROM employee_register WHERE EID = '{row.get('EID')}' AND PAYROLL_NUM = '{row.get('PAYROLL_NUM')}'"
            paid_success, paid_result = DB2Query.runSelectQuery(paid_query)
            formatted_result.append({
                "payrollNum": row.get('PAYROLL_NUM'),
                "eid": row.get('EID'),
                "name": row.get('NAME'),
                "date": str(row.get('DATE')),
                "amount": float(row.get('AMOUNT', 0)),
                "paidAmount": float(paid_result[0]['PAID_AMT']) if paid_success and paid_result else 0.0,
                "remark":  "Paid" if (paid_result and paid_result[0].get('PAID_AMT', 0) >= row.get('AMOUNT', 0)) else "Pending",
            })
        return JsonResponse(formatted_result, safe=False)
    
    if success:
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({"error": "Failed to load data"}, status=500)


# ---------- Employee APIs (mirror patient APIs) ----------
def get_data_by_eid(request):
    """Get employee data by EID. Returns array like patient endpoint."""
    eid = request.GET.get('eid')
    if not eid:
        return JsonResponse({"error": "EID is required"}, status=400)

    # NOTE: Assuming employee tables are named `employee_data` and `employee_register`.
    query = f"SELECT * FROM employee_data WHERE eid = '{eid}'"
    success, result = DB2Query.runSelectQuery(query)

    if success and result:
        query = f"SELECT * FROM employee_register WHERE eid = '{result[0]['EID']}' AND PAYROLL_NUM = '{result[0].get('PAYROLL_NUM','')}'"
        payment_done_success, payment_done = DB2Query.runSelectQuery(query)
        if payment_done_success and payment_done:
            send_data = {
                "payrollNum": result[0].get('PAYROLL_NUM'),
                "eid": result[0].get('EID'),
                "name": result[0].get('NAME'),
                "date": str(result[0].get('DATE')),
                "amount": float(result[0].get('AMOUNT', 0)),
                "paidAmount": float(payment_done[0].get('PAID_AMT', 0)),
                "remark": "Paid" if payment_done[0].get('PAID_AMT', 0) >= result[0].get('AMOUNT', 0) else "Pending",
            }
            return JsonResponse([send_data], safe=False)

    return JsonResponse([], safe=False)


def update_emp_payment(request):
    eid = request.GET.get("eid")
    payroll_num = request.GET.get("payroll_num")
    paid_amount = request.GET.get("paid_amount")

    if not eid or not payroll_num or not paid_amount:
        return JsonResponse({"error": "eid, payroll_num, and paid_amount are required"}, status=400)

    try:
        paid_amount = float(paid_amount)
    except ValueError:
        return JsonResponse({"error": "paid_amount must be a number"}, status=400)

    query = f"UPDATE employee_register SET PAID_AMT = {paid_amount} WHERE EID = '{eid}' AND PAYROLL_NUM = '{payroll_num}'"
    success, msg = DB2Query.runQuery(query)
    if success:
        return JsonResponse({"message": "Payment updated successfully"})
    else:
        return JsonResponse({"error": f"Failed to update payment: {msg}"}, status=500)


def load_emp_data(request):
    query = "SELECT * FROM employee_data FETCH FIRST 100 ROWS ONLY"
    success, result = DB2Query.runSelectQuery(query)

    if success and result:
        formatted_result = []
        for row in result:
            paid_query = f"SELECT PAID_AMT FROM employee_register WHERE EID = '{row.get('EID')}' AND PAYROLL_NUM = '{row.get('PAYROLL_NUM')}'"
            paid_success, paid_result = DB2Query.runSelectQuery(paid_query)
            formatted_result.append({
                "payrollNum": row.get('PAYROLL_NUM'),
                "eid": row.get('EID'),
                "name": row.get('NAME'),
                "date": str(row.get('DATE')),
                "amount": float(paid_result[0]['AMOUNT']) if paid_success and paid_result else float(row.get('AMOUNT', 0)),
                "paidAmount": float(paid_result[0]['PAID_AMT']) if paid_success and paid_result else 0.0,
                "remark":  "Paid" if (paid_result and paid_result[0].get('PAID_AMT', 0) >= row.get('AMOUNT', 0)) else "Pending",
            })
        return JsonResponse(formatted_result, safe=False)
    
    if success:
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({"error": "Failed to load employee data"}, status=500)
