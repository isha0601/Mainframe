# import streamlit as st
# import requests
# import pandas as pd
# import matplotlib.pyplot as plt

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
#     employees = pd.DataFrame(res.json())
    
#     # Ensure proper column names
#     employees.columns = [col.upper() for col in employees.columns]
    
#     if not employees.empty:
#         # Fix SALARY and BONUS if concatenated or as strings
#         employees['SALARY'] = employees['SALARY'].astype(str).str.extract(r'(\d+\.?\d*)')[0]
#         employees['BONUS'] = employees['BONUS'].astype(str).str.extract(r'(\d+\.?\d*)')[0]
#         employees['SALARY'] = pd.to_numeric(employees['SALARY'], errors='coerce')
#         employees['BONUS'] = pd.to_numeric(employees['BONUS'], errors='coerce')
#         employees = employees.dropna(subset=['SALARY', 'BONUS'])
        
#         # Metrics
#         col1, col2, col3 = st.columns(3)
#         col1.metric("Total Employees", len(employees))
#         col2.metric("Average Salary", f"{employees['SALARY'].mean():,.2f}")
#         col3.metric("Average Bonus", f"{employees['BONUS'].mean():,.2f}")
        
#         # Sorting
#         sort_by = st.selectbox("Sort By", options=employees.columns, index=0)
#         ascending = st.checkbox("Ascending", value=True)
#         st.dataframe(employees.sort_values(by=sort_by, ascending=ascending))
        
#         # Graphs
#         st.subheader("📊 Salary & Bonus Distribution")
#         fig, ax = plt.subplots()
#         employees[['SALARY', 'BONUS']].plot(kind='bar', ax=ax)
#         st.pyplot(fig)
#     else:
#         st.info("No employees found.")
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















import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API = "http://127.0.0.1:5000"

st.title("💼 Employee Management System (DB2)")

# --- Session State for Refresh ---
if 'refresh' not in st.session_state:
    st.session_state.refresh = False

def refresh_data():
    st.session_state.refresh = True

# --- Merge Button ---
if st.button("🔄 Merge EMPLOYEE_FILE1 + EMPLOYEE_FILE2"):
    r = requests.post(f"{API}/merge_employees")
    st.success(r.json().get("message", "Merge complete"))
    refresh_data()

st.divider()

# --- Fetch Employees ---
res = requests.get(f"{API}/employees")
if res.status_code == 200:
    employees = pd.DataFrame(res.json())

    # Convert numeric columns
    employees['SALARY'] = pd.to_numeric(employees['SALARY'], errors='coerce')
    employees['BONUS'] = pd.to_numeric(employees['BONUS'], errors='coerce')

    # --- Metrics ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Employees", len(employees))
    col2.metric("Average Salary", f"{employees['SALARY'].mean():,.2f}")
    col3.metric("Average Bonus", f"{employees['BONUS'].mean():,.2f}")

    st.divider()

    # --- Search & Filter ---
    search_name = st.text_input("Search by Name")
    dept_filter = st.multiselect("Filter by Department", options=employees['DEPARTMENT'].unique())
    salary_range = st.slider(
        "Salary Range",
        int(employees['SALARY'].min()),
        int(employees['SALARY'].max()),
        (int(employees['SALARY'].min()), int(employees['SALARY'].max()))
    )

    filtered = employees.copy()
    if search_name:
        filtered = filtered[filtered['NAME'].str.contains(search_name, case=False)]
    if dept_filter:
        filtered = filtered[filtered['DEPARTMENT'].isin(dept_filter)]
    filtered = filtered[(filtered['SALARY'] >= salary_range[0]) & (filtered['SALARY'] <= salary_range[1])]

    # --- Sorting ---
    sort_column = st.selectbox("Sort by", options=employees.columns, index=0)
    sort_order = st.radio("Order", ["Ascending", "Descending"])
    filtered = filtered.sort_values(by=sort_column, ascending=(sort_order == "Ascending"))

    st.dataframe(filtered)

    st.divider()

    # --- Charts ---
    st.subheader("📊 Salary Distribution by Department")
    fig = px.box(filtered, x="DEPARTMENT", y="SALARY", color="DEPARTMENT")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📊 Bonus vs Salary Scatter")
    fig2 = px.scatter(filtered, x="SALARY", y="BONUS", color="DEPARTMENT", hover_data=["NAME"])
    st.plotly_chart(fig2, use_container_width=True)

else:
    st.error(res.json().get("error", "Failed to load employees"))

st.divider()

# --- Add Employee ---
st.subheader("➕ Add Employee")
col1, col2 = st.columns(2)
with col1:
    emp_id = st.number_input("Employee ID", min_value=1, key="add_id")
    name = st.text_input("Name", key="add_name")
with col2:
    salary = st.number_input("Salary", min_value=0, key="add_salary")
    dept = st.text_input("Department", key="add_dept")
    bonus = st.number_input("Bonus", min_value=0, key="add_bonus")

if st.button("Add Employee"):
    r = requests.post(f"{API}/employees", json={
        "emp_id": emp_id,
        "name": name,
        "salary": salary,
        "department": dept,
        "bonus": bonus
    })
    if r.status_code == 200:
        st.success("✅ Employee added!")
        refresh_data()
    else:
        st.error(r.json().get("error"))

# --- Update Employee ---
st.subheader("✏️ Update Employee")
update_id = st.number_input("Employee ID to Update", min_value=1, key="update")
new_name = st.text_input("New Name", key="update_name")
new_salary = st.number_input("New Salary", min_value=0, key="update_salary")
new_dept = st.text_input("New Department", key="update_dept")
new_bonus = st.number_input("New Bonus", min_value=0, key="update_bonus")

if st.button("Update Employee"):
    r = requests.put(f"{API}/employees/{update_id}", json={
        "name": new_name,
        "salary": new_salary,
        "department": new_dept,
        "bonus": new_bonus
    })
    if r.status_code == 200:
        st.success("✅ Employee updated!")
        refresh_data()
    else:
        st.error(r.json().get("error"))

# --- Delete Employee ---
st.subheader("🗑️ Delete Employee")
delete_id = st.number_input("Employee ID to Delete", min_value=1, key="delete")
if st.button("Delete Employee"):
    r = requests.delete(f"{API}/employees/{delete_id}")
    if r.status_code == 200:
        st.success("✅ Employee deleted!")
        refresh_data()
    else:
        st.error(r.json().get("error"))

# --- Handle session state refresh ---
if st.session_state.refresh:
    st.session_state.refresh = False
    st.rerun()





