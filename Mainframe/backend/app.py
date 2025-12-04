from flask import Flask, jsonify, request
from flask_cors import CORS
from db2_connect import runSelectQuery, runQuery, mergeEmployeeData

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Employee Management API is running"})

# --- READ ALL ---
@app.route("/employees", methods=["GET"])
def get_employees():
    success, data = runSelectQuery("SELECT * FROM EMPLOYEE_MATCHED ORDER BY EMP_ID")
    return jsonify(data) if success else (jsonify({"error": data}), 500)

# --- CREATE ---
# @app.route("/employees", methods=["POST"])
# def add_employee():
    # emp = request.json
    # q = f"""
        # INSERT INTO EMPLOYEE_MATCHED (EMP_ID, NAME, SALARY, DEPARTMENT, BONUS)
        # VALUES ('{emp['emp_id']}', '{emp['name']}', {emp['salary']}, '{emp['department']}', {emp['bonus']})
    # """
    # success, msg = runQuery(q)
    # return jsonify({"message": msg}) if success else (jsonify({"error": msg}), 500)

# --- CREATE ---
@app.route("/employees", methods=["POST"])
def add_employee():
    emp = request.json
    emp_id = emp["emp_id"]

    # 1️⃣ Check if Employee ID already exists
    check_q = f"SELECT COUNT(*) AS CNT FROM EMPLOYEE_MATCHED WHERE EMP_ID = '{emp_id}'"
    success, result = runSelectQuery(check_q)

    if success and len(result) > 0 and result[0]["CNT"] > 0:
        return jsonify({"error": f"Employee ID {emp_id} already exists!"}), 400

    # 2️⃣ Insert only if ID is NOT duplicate
    q = f"""
        INSERT INTO EMPLOYEE_MATCHED (EMP_ID, NAME, SALARY, DEPARTMENT, BONUS)
        VALUES ('{emp_id}', '{emp['name']}', {emp['salary']},
                '{emp['department']}', {emp['bonus']})
    """
    success, msg = runQuery(q)

    return jsonify({"message": msg}) if success else (jsonify({"error": msg}), 500)



# --- UPDATE ---
@app.route("/employees/<string:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    emp = request.json
    q = f"""
        UPDATE EMPLOYEE_MATCHED
        SET NAME='{emp['name']}', SALARY={emp['salary']}, 
            DEPARTMENT='{emp['department']}', BONUS={emp['bonus']}
        WHERE EMP_ID='{emp_id}'
    """
    success, msg = runQuery(q)
    return jsonify({"message": "Updated successfully"}) if success else (jsonify({"error": msg}), 500)

# --- DELETE ---
@app.route("/employees/<string:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    q = f"DELETE FROM EMPLOYEE_MATCHED WHERE EMP_ID='{emp_id}'"
    success, msg = runQuery(q)
    return jsonify({"message": "Deleted successfully"}) if success else (jsonify({"error": msg}), 500)

# --- MERGE FILE1 + FILE2 ---
@app.route("/merge_employees", methods=["POST"])
def merge_employees():
    success, msg = mergeEmployeeData()
    return jsonify({"message": msg}) if success else (jsonify({"error": msg}), 500)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=False)

