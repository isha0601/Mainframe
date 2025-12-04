
# # import streamlit as st
# # import pandas as pd
# # import requests
# # import plotly.express as px

# # API = "http://127.0.0.1:5000"

# # st.title("Employee Management System (DB2)")

# # # --- Session State for Refresh ---
# # if 'refresh' not in st.session_state:
# #     st.session_state.refresh = False

# # def refresh_data():
# #     st.session_state.refresh = True

# # # --- Merge Button ---
# # if st.button("Merge EMPLOYEE_FILE1 + EMPLOYEE_FILE2"):
# #     r = requests.post(f"{API}/merge_employees")
# #     st.success(r.json().get("message", "Merge complete"))
# #     refresh_data()

# # st.divider()

# # # --- Fetch Employees ---
# # res = requests.get(f"{API}/employees")
# # if res.status_code == 200:
# #     employees = pd.DataFrame(res.json())

# #     # Convert numeric columns
# #     employees['SALARY'] = pd.to_numeric(employees['SALARY'], errors='coerce')
# #     employees['BONUS'] = pd.to_numeric(employees['BONUS'], errors='coerce')

# #     # --- Metrics ---
# #     col1, col2, col3 = st.columns(3)
# #     col1.metric("Total Employees", len(employees))
# #     col2.metric("Average Salary", f"{employees['SALARY'].mean():,.2f}")
# #     col3.metric("Average Bonus", f"{employees['BONUS'].mean():,.2f}")

# #     st.divider()

# #     # --- Search & Filter ---
# #     search_name = st.text_input("Search by Name")
# #     dept_filter = st.multiselect("Filter by Department", options=employees['DEPARTMENT'].unique())
# #     salary_range = st.slider(
# #         "Salary Range",
# #         int(employees['SALARY'].min()),
# #         int(employees['SALARY'].max()),
# #         (int(employees['SALARY'].min()), int(employees['SALARY'].max()))
# #     )

# #     filtered = employees.copy()
# #     if search_name:
# #         filtered = filtered[filtered['NAME'].str.contains(search_name, case=False)]
# #     if dept_filter:
# #         filtered = filtered[filtered['DEPARTMENT'].isin(dept_filter)]
# #     filtered = filtered[(filtered['SALARY'] >= salary_range[0]) & (filtered['SALARY'] <= salary_range[1])]

# #     # --- Sorting ---
# #     sort_column = st.selectbox("Sort by", options=employees.columns, index=0)
# #     sort_order = st.radio("Order", ["Ascending", "Descending"])
# #     filtered = filtered.sort_values(by=sort_column, ascending=(sort_order == "Ascending"))

# #     st.dataframe(filtered)

# #     st.divider()

# #     # --- Charts ---
# #     st.subheader("Salary Distribution by Department")
# #     fig = px.box(filtered, x="DEPARTMENT", y="SALARY", color="DEPARTMENT")
# #     st.plotly_chart(fig, width='stretch'e)

# #     st.subheader("Bonus vs Salary Scatter")
# #     fig2 = px.scatter(filtered, x="SALARY", y="BONUS", color="DEPARTMENT", hover_data=["NAME"])
# #     st.plotly_chart(fig2, width='stretch'e)

# # else:
# #     st.error(res.json().get("error", "Failed to load employees"))

# # st.divider()

# # # --- Add Employee ---
# # st.subheader("Add Employee")
# # col1, col2 = st.columns(2)
# # with col1:
# #     emp_id = st.number_input("Employee ID", min_value=1, key="add_id")
# #     name = st.text_input("Name", key="add_name")
# # with col2:
# #     salary = st.number_input("Salary", min_value=0, key="add_salary")
# #     dept = st.text_input("Department", key="add_dept")
# #     bonus = st.number_input("Bonus", min_value=0, key="add_bonus")

# # if st.button("Add Employee"):
# #     r = requests.post(f"{API}/employees", json={
# #         "emp_id": emp_id,
# #         "name": name,
# #         "salary": salary,
# #         "department": dept,
# #         "bonus": bonus
# #     })
# #     if r.status_code == 200:
# #         st.success("Employee added!")
# #         refresh_data()
# #     else:
# #         st.error(r.json().get("error"))

# # # --- Update Employee ---
# # st.subheader("Update Employee")
# # update_id = st.number_input("Employee ID to Update", min_value=1, key="update")
# # new_name = st.text_input("New Name", key="update_name")
# # new_salary = st.number_input("New Salary", min_value=0, key="update_salary")
# # new_dept = st.text_input("New Department", key="update_dept")
# # new_bonus = st.number_input("New Bonus", min_value=0, key="update_bonus")

# # if st.button("Update Employee"):
# #     r = requests.put(f"{API}/employees/{update_id}", json={
# #         "name": new_name,
# #         "salary": new_salary,
# #         "department": new_dept,
# #         "bonus": new_bonus
# #     })
# #     if r.status_code == 200:
# #         st.success("Employee updated!")
# #         refresh_data()
# #     else:
# #         st.error(r.json().get("error"))

# # # --- Delete Employee ---
# # st.subheader("Delete Employee")
# # delete_id = st.number_input("Employee ID to Delete", min_value=1, key="delete")
# # if st.button("Delete Employee"):
# #     r = requests.delete(f"{API}/employees/{delete_id}")
# #     if r.status_code == 200:
# #         st.success("Employee deleted!")
# #         refresh_data()
# #     else:
# #         st.error(r.json().get("error"))

# # # --- Handle session state refresh ---
# # if st.session_state.refresh:
# #     st.session_state.refresh = False
# #     st.rerun()












# import streamlit as st
# import pandas as pd
# import requests
# import plotly.express as px

# API = "http://127.0.0.1:5000"
# st.set_page_config(page_title="Employee Management", layout="wide")

# # ---------- HEADER ----------
# st.markdown("""
#     <h1 style="text-align:center; color:#4A90E2;">
#         Employee Management System (DB2)
#     </h1>
# """, unsafe_allow_html=True)

# st.markdown("---")

# # ---------- SESSION ----------
# if "refresh" not in st.session_state:
#     st.session_state.refresh = False

# def refresh_data():
#     st.session_state.refresh = True


# # ---------- MERGE BUTTON ----------
# with st.container():
#     st.markdown("Merge Employee Files")
#     if st.button("Merge EMPLOYEE_FILE1 + EMPLOYEE_FILE2"):
#         r = requests.post(f"{API}/merge_employees")
#         st.success(r.json().get("message", "Merge Successful"))
#         refresh_data()

# st.markdown("---")

# # ---------- FETCH DATA ----------
# res = requests.get(f"{API}/employees")

# if res.status_code == 200:
#     employees = pd.DataFrame(res.json())

#     employees["SALARY"] = pd.to_numeric(employees["SALARY"], errors="coerce")
#     employees["BONUS"] = pd.to_numeric(employees["BONUS"], errors="coerce")

#     # ---------- KPI CARDS ----------
#     st.markdown("## Dashboard Overview")

#     col1, col2, col3 = st.columns(3)
#     col1.metric("👥 Total Employees", len(employees))
#     col2.metric("💰 Avg Salary", f"{employees['SALARY'].mean():,.2f}")
#     col3.metric("🎁 Avg Bonus", f"{employees['BONUS'].mean():,.2f}")

#     st.markdown("---")

#     # ---------- SEARCH & FILTER ----------
#     st.markdown("##  Search & Filters")

#     colA, colB, colC = st.columns([1.5, 1, 1])

#     with colA:
#         search_name = st.text_input("Search by Employee Name")

#     with colB:
#         dept_filter = st.multiselect(
#             "Filter by Department",
#             options=employees["DEPARTMENT"].unique()
#         )

#     with colC:
#         salary_range = st.slider(
#             "Salary Range",
#             int(employees["SALARY"].min()),
#             int(employees["SALARY"].max()),
#             (int(employees["SALARY"].min()), int(employees["SALARY"].max()))
#         )

#     filtered = employees.copy()

#     if search_name:
#         filtered = filtered[filtered["NAME"].str.contains(search_name, case=False)]

#     if dept_filter:
#         filtered = filtered[filtered["DEPARTMENT"].isin(dept_filter)]

#     filtered = filtered[
#         (filtered["SALARY"] >= salary_range[0]) &
#         (filtered["SALARY"] <= salary_range[1])
#     ]

#     # ---------- SORT ----------
#     st.markdown("###  Sorting Options")
#     colS1, colS2 = st.columns(2)

#     with colS1:
#         sort_column = st.selectbox("Sort by Column", options=employees.columns)

#     with colS2:
#         sort_order = st.radio("Sort Order", ["Ascending", "Descending"], horizontal=True)

#     filtered = filtered.sort_values(
#         sort_column,
#         ascending=(sort_order == "Ascending")
#     )

#     st.dataframe(filtered, width='stretch')

#     st.markdown("---")



#     st.markdown("## Data Visualizations")

#     # BAR CHART – Average Salary by Department
#     st.subheader(" Average Salary per Department")

#     dept_salary = filtered.groupby("DEPARTMENT")["SALARY"].mean().reset_index()

#     fig_bar = px.bar(
#         dept_salary,
#         x="DEPARTMENT",
#         y="SALARY",
#         text="SALARY",
#         title="Average Salary by Department",
#         color="DEPARTMENT"
#     )
#     fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
#     st.plotly_chart(fig_bar, config={"responsive": True})

#     st.markdown("---")

#     # BUBBLE CHART – Bonus-to-Salary Ratio
#     st.subheader(" Bonus-to-Salary Ratio Bubble Chart")

#     filtered["BONUS_RATIO"] = (filtered["BONUS"] / filtered["SALARY"]) * 100

#     fig_bubble = px.scatter(
#         filtered,
#         x="SALARY",
#         y="BONUS",
#         size="BONUS_RATIO",
#         color="DEPARTMENT",
#         hover_data=["NAME"],
#         title="Bubble Chart: Bonus-to-Salary Ratio"
#     )
#     st.plotly_chart(fig_bubble, config={"responsive": True})

#     st.markdown("---")

#     # 3️ HEATMAP – Salary Heatmap
#     st.subheader(" Salary Heatmap (Department vs Salary)")

#     fig_heat = px.density_heatmap(
#         filtered,
#         x="DEPARTMENT",
#         y="SALARY",
#         title="Salary Heatmap",
#         nbinsy=20,
#         color_continuous_scale="Viridis"
#     )
#     st.plotly_chart(fig_heat, config={"responsive": True})

#     st.markdown("---")

#     # 4️ PIE CHART – Department Distribution
#     st.subheader(" Department Distribution")

#     dept_counts = filtered["DEPARTMENT"].value_counts()

#     fig_pie = px.pie(
#         values=dept_counts.values,
#         names=dept_counts.index,
#         hole=0.4,
#         title="Employees per Department",
#         color_discrete_sequence=px.colors.qualitative.Bold
#     )
#     st.plotly_chart(fig_pie, config={"responsive": True})

# else:
#     st.error(res.json().get("error", "Failed to load employees"))


# # ---------------------------------------------------------------
# #                       CRUD OPERATIONS
# # ---------------------------------------------------------------

# st.markdown("---")
# st.markdown("##  Employee Operations")

# # ========== ADD EMPLOYEE ==========
# with st.expander(" Add Employee"):
#     col1, col2 = st.columns(2)

#     with col1:
#         emp_id = st.number_input("Employee ID", min_value=1, key="add_id")
#         name = st.text_input("Name", key="add_name")

#     with col2:
#         salary = st.number_input("Salary", min_value=0, key="add_salary")
#         dept = st.text_input("Department", key="add_dept")
#         bonus = st.number_input("Bonus", min_value=0, key="add_bonus")

#     if st.button("Add Employee"):
#         r = requests.post(f"{API}/employees", json={
#             "emp_id": emp_id,
#             "name": name,
#             "salary": salary,
#             "department": dept,
#             "bonus": bonus
#         })

#         if r.status_code == 200:
#             st.success("Employee Added Successfully!")
#             refresh_data()
#         else:
#             st.error(r.json().get("error"))

# # ========== UPDATE EMPLOYEE ==========
# with st.expander(" Update Employee"):
#     update_id = st.number_input("Employee ID to Update", min_value=1, key="update")
#     new_name = st.text_input("New Name", key="update_name")
#     new_salary = st.number_input("New Salary", min_value=0, key="update_salary")
#     new_dept = st.text_input("New Department", key="update_dept")
#     new_bonus = st.number_input("New Bonus", min_value=0, key="update_bonus")

#     if st.button("Update Employee"):
#         r = requests.put(
#             f"{API}/employees/{update_id}",
#             json={
#                 "name": new_name,
#                 "salary": new_salary,
#                 "department": new_dept,
#                 "bonus": new_bonus
#             }
#         )

#         if r.status_code == 200:
#             st.success("Employee Updated Successfully!")
#             refresh_data()
#         else:
#             st.error(r.json().get("error"))

# # ========== DELETE EMPLOYEE ==========
# with st.expander(" Delete Employee"):
#     delete_id = st.number_input("Employee ID to Delete", min_value=1, key="delete")

#     if st.button("Delete Employee"):
#         r = requests.delete(f"{API}/employees/{delete_id}")
#         if r.status_code == 200:
#             st.success("Employee Deleted Successfully!")
#             refresh_data()
#         else:
#             st.error(r.json().get("error"))

# # ---------- REFRESH ----------
# if st.session_state.refresh:
#     st.session_state.refresh = False
#     st.rerun()


















# 
# 
# 
# 
# 
# 
# 
# import streamlit as st
# import pandas as pd
# import requests
# import plotly.express as px
# 
# API = "http://127.0.0.1:5000"
# st.set_page_config(page_title="Employee Management", layout="wide", initial_sidebar_state="expanded")
# 
# ---------------- HEADER ----------------
# st.markdown("""
    # <h1 style="text-align:center; color:#4A90E2;">
        # Employee Management System (DB2)
    # </h1>
# """, unsafe_allow_html=True)
# st.markdown("---")
# 
# ---------------- SESSION ----------------
# if "refresh" not in st.session_state:
    # st.session_state.refresh = False
# 
# def refresh_data():
    # st.session_state.refresh = True
# 
# ---------------- SIDEBAR ----------------
# st.sidebar.header("Filters & Search")
# search_name = st.sidebar.text_input("Search Employee by Name")
# dept_filter = st.sidebar.multiselect("Filter by Department", options=[])
# salary_range = st.sidebar.slider("Salary Range of Employee", 0, 100000, (0, 100000))
# 
# ---------------- FETCH DATA ----------------
# res = requests.get(f"{API}/employees")
# if res.status_code == 200:
    # employees = pd.DataFrame(res.json())
    # employees["SALARY"] = pd.to_numeric(employees["SALARY"], errors="coerce")
    # employees["BONUS"] = pd.to_numeric(employees["BONUS"], errors="coerce")
# 
    # Update sidebar filter options dynamically
    # if not dept_filter:
        # dept_filter = []
# 
    # salary_range = st.sidebar.slider(
        # "Salary Range",
        # int(employees["SALARY"].min()),
        # int(employees["SALARY"].max()),
        # (int(employees["SALARY"].min()), int(employees["SALARY"].max()))
    # )
# 
    # ---------------- FILTER DATA ----------------
    # filtered = employees.copy()
    # if search_name:
        # filtered = filtered[filtered["NAME"].str.contains(search_name, case=False)]
    # if dept_filter:
        # filtered = filtered[filtered["DEPARTMENT"].isin(dept_filter)]
    # filtered = filtered[(filtered["SALARY"] >= salary_range[0]) & (filtered["SALARY"] <= salary_range[1])]
# 
    # ---------------- DASHBOARD ----------------
    # st.markdown("## 📊 Dashboard Overview")
    # col1, col2, col3 = st.columns(3)
    # col1.metric("👥 Total Employees", len(filtered))
    # col2.metric("💰 Avg Salary", f"{filtered['SALARY'].mean():,.2f}")
    # col3.metric("🎁 Avg Bonus", f"{filtered['BONUS'].mean():,.2f}")
# 
    # st.markdown("---")
# 
    # ---------------- TABS ----------------
    # tabs = st.tabs(["Employee Data", "Visualizations", "Merge Files", "Add Employee", "Update Employee", "Delete Employee"])
# 
    # ----- TAB 1: Employee Data -----
    # with tabs[0]:
        # st.subheader("Filtered Employee Records")
        # sort_column = st.selectbox("Sort by Column", options=employees.columns, key="sort_col")
        # sort_order = st.radio("Sort Order", ["Ascending", "Descending"], horizontal=True, key="sort_ord")
        # filtered = filtered.sort_values(sort_column, ascending=(sort_order == "Ascending"))
        # st.dataframe(filtered, use_container_width=True)
# 
    # ----- TAB 2: Visualizations -----
    # with tabs[1]:
        # st.subheader("Average Salary of Employee per Department")
        # dept_salary = filtered.groupby("DEPARTMENT")["SALARY"].mean().reset_index()
        # fig_bar = px.bar(dept_salary, x="DEPARTMENT", y="SALARY", text="SALARY", color="DEPARTMENT")
        # fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        # st.plotly_chart(fig_bar, use_container_width=True)
# 
        # st.subheader("Bonus-to-Salary Ratio Bubble Chart")
        # filtered["BONUS_RATIO"] = (filtered["BONUS"] / filtered["SALARY"]) * 100
        # fig_bubble = px.scatter(filtered, x="SALARY", y="BONUS", size="BONUS_RATIO", color="DEPARTMENT",
                                # hover_data=["NAME"], title="Bubble Chart: Bonus-to-Salary Ratio")
        # st.plotly_chart(fig_bubble, use_container_width=True)
# 
        # st.subheader("Salary Heatmap")
        # fig_heat = px.density_heatmap(filtered, x="DEPARTMENT", y="SALARY", nbinsy=20, color_continuous_scale="Viridis")
        # st.plotly_chart(fig_heat, use_container_width=True)
# 
        # st.subheader("Department Distribution")
        # dept_counts = filtered["DEPARTMENT"].value_counts()
        # fig_pie = px.pie(values=dept_counts.values, names=dept_counts.index, hole=0.4, color_discrete_sequence=px.colors.qualitative.Bold)
        # st.plotly_chart(fig_pie, use_container_width=True)
# 
    # ----- TAB 3: Merge Files -----
    # with tabs[2]:
        # st.subheader("Merge Employee Files")
        # if st.button("Merge EMPLOYEE_FILE1 + EMPLOYEE_FILE2"):
            # r = requests.post(f"{API}/merge_employees")
            # st.success(r.json().get("message", "Merge Successful"))
            # refresh_data()
# 
    # ----- TAB 4: Add Employee -----
    # with tabs[3]:
        # st.subheader("Add Employee")
        # col1, col2 = st.columns(2)
        # with col1:
            # emp_id = st.number_input("Employee ID", min_value=1, key="add_id")
            # name = st.text_input("Name", key="add_name")
        # with col2:
            # salary = st.number_input("Salary", min_value=0, key="add_salary")
            # dept = st.text_input("Department", key="add_dept")
            # bonus = st.number_input("Bonus", min_value=0, key="add_bonus")
# 
        # if st.button("Add Employee"):
            # r = requests.post(f"{API}/employees", json={
                # "emp_id": emp_id, "name": name, "salary": salary, "department": dept, "bonus": bonus
            # })
            # if r.status_code == 200:
                # st.success("Employee Added Successfully!")
                # refresh_data()
            # else:
                # st.error(r.json().get("error"))
# 
    # ----- TAB 5: Update Employee -----
    # with tabs[4]:
        # st.subheader("Update Employee")
        # update_id = st.number_input("Employee ID to Update", min_value=1, key="update")
        # new_name = st.text_input("New Name", key="update_name")
        # new_salary = st.number_input("New Salary", min_value=0, key="update_salary")
        # new_dept = st.text_input("New Department", key="update_dept")
        # new_bonus = st.number_input("New Bonus", min_value=0, key="update_bonus")
# 
        # if st.button("Update Employee"):
            # r = requests.put(f"{API}/employees/{update_id}", json={
                # "name": new_name, "salary": new_salary, "department": new_dept, "bonus": new_bonus
            # })
            # if r.status_code == 200:
                # st.success("Employee Updated Successfully!")
                # refresh_data()
            # else:
                # st.error(r.json().get("error"))
# 
    # ----- TAB 6: Delete Employee -----
    # with tabs[5]:
        # st.subheader("Delete Employee")
        # delete_id = st.number_input("Employee ID to Delete", min_value=1, key="delete")
        # if st.button("Delete Employee"):
            # r = requests.delete(f"{API}/employees/{delete_id}")
            # if r.status_code == 200:
                # st.success("Employee Deleted Successfully!")
                # refresh_data()
            # else:
                # st.error(r.json().get("error"))
# 
# else:
    # st.error(res.json().get("error", "Failed to load employees"))
# 
# ---------------- REFRESH ----------------
#if st.session_state.refresh:
    # st.session_state.refresh = False
    # st.experimental_rerun()
















import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API = "http://127.0.0.1:5000"
st.set_page_config(page_title="Admin Employee Portal", layout="wide", initial_sidebar_state="expanded")

# ---------------- HEADER ----------------
st.markdown("""
    <h1 style="text-align:center; color:#4A90E2;">
        Employee Portal 
    </h1>
""", unsafe_allow_html=True)
st.markdown("---")

# ---------------- SESSION ----------------
if "refresh" not in st.session_state:
    st.session_state.refresh = False

def refresh_data():
    st.session_state.refresh = True

# ---------------- FETCH DATA ----------------
res = requests.get(f"{API}/employees")
if res.status_code == 200:
    employees = pd.DataFrame(res.json())
    employees["SALARY"] = pd.to_numeric(employees["SALARY"], errors="coerce")
    employees["BONUS"] = pd.to_numeric(employees["BONUS"], errors="coerce")

    # ---------------- SIDEBAR ----------------
    st.sidebar.header("Filters & Search")

    search_name = st.sidebar.text_input("Search Employee by Name")

    # Fix: Populate department filter dynamically
    dept_filter = st.sidebar.multiselect(
        "Filter by Department",
        options=sorted(employees["DEPARTMENT"].unique())
    )

    salary_min = int(employees["SALARY"].min())
    salary_max = int(employees["SALARY"].max())
    salary_range = st.sidebar.slider("Salary Range", salary_min, salary_max, (salary_min, salary_max))

    # ---------------- FILTER DATA ----------------
    filtered = employees.copy()
    if search_name:
        filtered = filtered[filtered["NAME"].str.contains(search_name, case=False)]
    if dept_filter:
        filtered = filtered[filtered["DEPARTMENT"].isin(dept_filter)]
    filtered = filtered[(filtered["SALARY"] >= salary_range[0]) & (filtered["SALARY"] <= salary_range[1])]

    # ---------------- DASHBOARD ----------------
    st.markdown("## Dashboard Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric(" Total Employees", len(filtered))
    col2.metric(" Avg Salary", f"{filtered['SALARY'].mean():,.2f}")
    col3.metric(" Avg Bonus", f"{filtered['BONUS'].mean():,.2f}")

    st.markdown("---")

    # ---------------- TABS ----------------
    tabs = st.tabs(["Employee Data", "Visualizations", "Merge Files", "Add Employee", "Update Employee", "Delete Employee"])

    # ----- TAB 1: Employee Data -----
    with tabs[0]:
        st.subheader("Filtered Employee Records")
        sort_column = st.selectbox("Sort by Column", options=employees.columns, key="sort_col")
        sort_order = st.radio("Sort Order", ["Ascending", "Descending"], horizontal=True, key="sort_ord")
        filtered = filtered.sort_values(sort_column, ascending=(sort_order == "Ascending"))
        st.dataframe(filtered, use_container_width=True)

    # ----- TAB 2: Visualizations -----
    with tabs[1]:
        st.subheader("Average Salary per Department")
        dept_salary = filtered.groupby("DEPARTMENT")["SALARY"].mean().reset_index()
        fig_bar = px.bar(dept_salary, x="DEPARTMENT", y="SALARY", text="SALARY", color="DEPARTMENT")
        fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        st.plotly_chart(fig_bar, use_container_width=True)

        st.subheader("Bonus-to-Salary Ratio Bubble Chart")
        filtered["BONUS_RATIO"] = (filtered["BONUS"] / filtered["SALARY"]) * 100
        fig_bubble = px.scatter(filtered, x="SALARY", y="BONUS", size="BONUS_RATIO", color="DEPARTMENT",
                                hover_data=["NAME"], title="Bubble Chart: Bonus-to-Salary Ratio")
        st.plotly_chart(fig_bubble, use_container_width=True)

        st.subheader("Salary Heatmap")
        fig_heat = px.density_heatmap(filtered, x="DEPARTMENT", y="SALARY", nbinsy=20, color_continuous_scale="Viridis")
        st.plotly_chart(fig_heat, use_container_width=True)

        st.subheader("Department Distribution")
        dept_counts = filtered["DEPARTMENT"].value_counts()
        fig_pie = px.pie(values=dept_counts.values, names=dept_counts.index, hole=0.4, color_discrete_sequence=px.colors.qualitative.Bold)
        st.plotly_chart(fig_pie, use_container_width=True)

    # ----- TAB 3: Merge Files -----
    with tabs[2]:
        st.subheader("Merge Employee Files")
        if st.button("Merge EMPLOYEE_FILE1 + EMPLOYEE_FILE2"):
            r = requests.post(f"{API}/merge_employees")
            st.success(r.json().get("message", "Merge Successful"))
            refresh_data()

    # ----- TAB 4: Add Employee -----
    with tabs[3]:
        st.subheader("Add Employee")
        col1, col2 = st.columns(2)
        with col1:
            emp_id = st.number_input("Employee ID", min_value=1, key="add_id")
            name = st.text_input("Name", key="add_name")
        with col2:
            salary = st.number_input("Salary", min_value=0, key="add_salary")
            dept = st.text_input("Department", key="add_dept")
            bonus = st.number_input("Bonus", min_value=0, key="add_bonus")

        if st.button("Add Employee"):
            if emp_id in employees["EMP_ID"].values:
                st.warning(f"Employee ID {emp_id} already exists! Cannot add duplicate.")
            else:
                r = requests.post(f"{API}/employees", json={
                "emp_id": emp_id, "name": name, "salary": salary, "department": dept, "bonus": bonus
            })
                if r.status_code == 200:
                    st.success("Employee Added Successfully!")
                    refresh_data()
                else:
                    st.error(r.json().get("error"))

    # ----- TAB 5: Update Employee -----
    with tabs[4]:
        st.subheader("Update Employee")
        update_id = st.number_input("Employee ID to Update", min_value=1, key="update")
        new_name = st.text_input("New Name", key="update_name")
        new_salary = st.number_input("New Salary", min_value=0, key="update_salary")
        new_dept = st.text_input("New Department", key="update_dept")
        new_bonus = st.number_input("New Bonus", min_value=0, key="update_bonus")

        if st.button("Update Employee"):
             # Check if employee exists
            if update_id not in employees["EMP_ID"].values:
             st.warning(f"Employee ID {update_id} does not exist! Cannot update.")
            else:
                r = requests.put(f"{API}/employees/{update_id}", json={
                "name": new_name, "salary": new_salary, "department": new_dept, "bonus": new_bonus
            })
                if r.status_code == 200:
                    st.success("Employee Updated Successfully!")
                    refresh_data()
                else:
                    st.error(r.json().get("error"))

    # ----- TAB 6: Delete Employee -----
    with tabs[5]:
        st.subheader("Delete Employee")
        delete_id = st.number_input("Employee ID to Delete", min_value=1, key="delete")
        if st.button("Delete Employee"):
            r = requests.delete(f"{API}/employees/{delete_id}")
            if r.status_code == 200:
                st.success("Employee Deleted Successfully!")
                refresh_data()
            else:
                st.error(r.json().get("error"))

else:
    st.error("Failed to load employees from API")

# ---------------- REFRESH ----------------
if st.session_state.refresh:
    st.session_state.refresh = False
    st.rerun()
