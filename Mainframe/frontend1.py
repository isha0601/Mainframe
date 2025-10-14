# import streamlit as st
# import requests

# API = "http://127.0.0.1:5000"

# st.title("💼 Employee Management System (DB2)")

# # --- Merge Button ---
# if st.button("🔄 Merge EMPLOYEE_FILE1 + EMPLOYEE_FILE2"):
#     r = requests.post(f"{API}/merge_employees")
#     st.success(r.json().get("message", "Merge complete"))

# st.divider()

# # --- Show Employees ---
# st.subheader("📋 Employee Records")
# res = requests.get(f"{API}/employees")
# if res.status_code == 200:
#     employees = res.json()
#     st.dataframe(employees)
# else:
#     st.error(res.json().get("error", "Failed to load"))

# st.divider()

# # --- Add Employee ---
# st.subheader("➕ Add Employee")
# col1, col2 = st.columns(2)
# with col1:
#     emp_id = st.number_input("Employee ID", min_value=1)
#     name = st.text_input("Name")
# with col2:
#     salary = st.number_input("Salary", min_value=0)
#     dept = st.text_input("Department")
#     bonus = st.number_input("Bonus", min_value=0)

# if st.button("Add Employee"):
#     r = requests.post(f"{API}/employees", json={
#         "emp_id": emp_id,
#         "name": name,
#         "salary": salary,
#         "department": dept,
#         "bonus": bonus
#     })
#     if r.status_code == 200:
#         st.success("✅ Employee added!")
#         st.rerun()
#     else:
#         st.error(r.json().get("error"))

# # --- Update Employee ---
# st.subheader("✏️ Update Employee")
# update_id = st.number_input("Enter Employee ID to Update", min_value=1, key="update")
# new_name = st.text_input("New Name")
# new_salary = st.number_input("New Salary", min_value=0, key="new_salary")
# new_dept = st.text_input("New Department")
# new_bonus = st.number_input("New Bonus", min_value=0, key="new_bonus")

# if st.button("Update"):
#     r = requests.put(f"{API}/employees/{update_id}", json={
#         "name": new_name,
#         "salary": new_salary,
#         "department": new_dept,
#         "bonus": new_bonus
#     })
#     if r.status_code == 200:
#         st.success("✅ Updated successfully!")
#         st.rerun()
#     else:
#         st.error(r.json().get("error"))

# # --- Delete Employee ---
# st.subheader("🗑️ Delete Employee")
# delete_id = st.number_input("Employee ID to Delete", min_value=1, key="delete")
# if st.button("Delete"):
#     r = requests.delete(f"{API}/employees/{delete_id}")
#     if r.status_code == 200:
#         st.success("Deleted successfully!")
#         st.rerun()
#     else:
#         st.error(r.json().get("error"))










