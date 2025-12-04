

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
# import streamlit as st
# import pandas as pd
# import requests
# import plotly.express as px
# 
# API = "http://127.0.0.1:5000"
# 
# ---------------------------------------------------
                #   PAGE CONFIG
# ---------------------------------------------------
# st.set_page_config(
    # page_title="Employee Management System",
    # layout="wide",
# )
# 
# ---------------------------------------------------
                    #   HEADER
# ---------------------------------------------------
# st.markdown("""
    # <h1 style="text-align:center; color:#2E86C1; margin-bottom:0;">
        # Employee Management System (DB2)
    # </h1>
    # <p style="text-align:center; font-size:16px; color:gray; margin-top:5px;">
        # Manage, Analyze & Visualize Employee Records Efficiently
    # </p>
# """, unsafe_allow_html=True)
# 
# st.markdown("<hr>", unsafe_allow_html=True)
# 
# ---------------------------------------------------
                    # SESSION
# ---------------------------------------------------
# if "refresh" not in st.session_state:
    # st.session_state.refresh = False
# 
# def refresh():
    # st.session_state.refresh = True
# 
# 
# ---------------------------------------------------
            #    MERGE OPERATION
# ---------------------------------------------------
# with st.container():
    # st.subheader("🔄 Merge Employee Data Files")
    # st.write("Merge EMPLOYEE_FILE1 and EMPLOYEE_FILE2 into consolidated table.")
# 
    # if st.button("Merge Files", use_container_width=True):
        # r = requests.post(f"{API}/merge_employees")
        # st.success(r.json().get("message", "Merge Successful"))
        # refresh()
# 
# st.markdown("<hr>", unsafe_allow_html=True)
# 
# ---------------------------------------------------
            #    FETCH EMPLOYEES
# ---------------------------------------------------
# res = requests.get(f"{API}/employees")
# 
# if res.status_code != 200:
    # st.error("❌ Failed to load employee data")
    # st.stop()
# 
# employees = pd.DataFrame(res.json())
# 
# Convert numeric
# employees["SALARY"] = pd.to_numeric(employees["SALARY"], errors="coerce")
# employees["BONUS"] = pd.to_numeric(employees["BONUS"], errors="coerce")
# 
# if employees.empty:
    # st.warning("⚠ No employee records found.")
    # st.stop()
# 
# ---------------------------------------------------
                #  KPI DASHBOARD
# ---------------------------------------------------
# st.subheader("📊 Dashboard Overview")
# 
# col1, col2, col3 = st.columns(3)
# 
# col1.metric("👥 Total Employees", len(employees))
# col2.metric("💰 Average Salary", f"{employees['SALARY'].mean():,.2f}")
# col3.metric("🎁 Average Bonus", f"{employees['BONUS'].mean():,.2f}")
# 
# st.markdown("<hr>", unsafe_allow_html=True)
# 
# ---------------------------------------------------
            #   SEARCH + FILTER PANEL
# ---------------------------------------------------
# st.subheader("🔍 Search & Filter Employees")
# 
# f1, f2, f3 = st.columns([1.5, 1, 1])
# 
# with f1:
    # search_name = st.text_input("Search by Name", placeholder="Enter employee name...")
# 
# with f2:
    # dept_filter = st.multiselect(
        # "Department Filter",
        # options=employees["DEPARTMENT"].unique()
    # )
# 
# with f3:
    # salary_range = st.slider(
        # "Salary Range",
        # min_value=int(employees["SALARY"].min()),
        # max_value=int(employees["SALARY"].max()),
        # value=(int(employees["SALARY"].min()), int(employees["SALARY"].max()))
    # )
# 
# filtered = employees.copy()
# 
# Apply filters
# if search_name:
    # filtered = filtered[filtered["NAME"].str.contains(search_name, case=False)]
# 
# if dept_filter:
    # filtered = filtered[filtered["DEPARTMENT"].isin(dept_filter)]
# 
# filtered = filtered[
    # (filtered["SALARY"] >= salary_range[0]) &
    # (filtered["SALARY"] <= salary_range[1])
# ]
# 
# ---------------------------------------------------
                #    SORTING
# ---------------------------------------------------
# st.subheader("↕ Sorting Options")
# 
# s1, s2 = st.columns(2)
# 
# with s1:
    # sort_column = st.selectbox("Select Column", employees.columns)
# 
# with s2:
    # sort_order = st.radio("Order", ["Ascending", "Descending"], horizontal=True)
# 
# filtered = filtered.sort_values(
    # sort_column,
    # ascending=(sort_order == "Ascending")
# )
# 
# ---------------------------------------------------
            #    DISPLAY FILTERED DATA
# ---------------------------------------------------
# st.subheader("📄 Employee Data")
# st.dataframe(filtered, use_container_width=True, height=400)
# 
# st.markdown("<hr>", unsafe_allow_html=True)
# 
# ---------------------------------------------------
            #    DATA VISUALIZATION
# ---------------------------------------------------
# st.subheader("📈 Data Visualizations")
# 
# ---------------- BAR CHART ----------------
# st.markdown("### 📌 Average Salary by Department")
# 
# dept_salary = filtered.groupby("DEPARTMENT")["SALARY"].mean().reset_index()
# 
# fig_bar = px.bar(
    # dept_salary,
    # x="DEPARTMENT",
    # y="SALARY",
    # text="SALARY",
    # color="DEPARTMENT",
    # title="Average Salary by Department"
# )
# fig_bar.update_traces(texttemplate="%{text:.2f}", textposition="outside")
# st.plotly_chart(fig_bar, use_container_width=True)
# 
# ---------------- BUBBLE CHART ----------------
# st.markdown("### 🔵 Bonus-to-Salary Ratio")
# 
# filtered["BONUS_RATIO"] = (filtered["BONUS"] / filtered["SALARY"]) * 100
# 
# fig_bubble = px.scatter(
    # filtered,
    # x="SALARY",
    # y="BONUS",
    # size="BONUS_RATIO",
    # color="DEPARTMENT",
    # hover_data=["NAME"],
    # title="Bonus-to-Salary Ratio"
# )
# st.plotly_chart(fig_bubble, use_container_width=True)
# 
# ---------------- HEATMAP ----------------
# st.markdown("### 🔥 Salary Heatmap")
# 
# fig_heat = px.density_heatmap(
    # filtered,
    # x="DEPARTMENT",
    # y="SALARY",
    # nbinsy=20,
    # color_continuous_scale="Viridis",
    # title="Salary Heatmap"
# )
# st.plotly_chart(fig_heat, use_container_width=True)
# 
# ---------------- PIE CHART ----------------
# st.markdown("### 🥧 Department-wise Employee Distribution")
# 
# dept_counts = filtered["DEPARTMENT"].value_counts()
# 
# fig_pie = px.pie(
    # values=dept_counts.values,
    # names=dept_counts.index,
    # hole=0.4,
    # color_discrete_sequence=px.colors.qualitative.Bold,
    # title="Employees per Department"
# )
# st.plotly_chart(fig_pie, use_container_width=True)
# 
# ---------------------------------------------------
            #    AUTO REFRESH
# ---------------------------------------------------
# if st.session_state.refresh:
    # st.session_state.refresh = False
    # st.rerun()
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

# ---------------------------------------------------
                #   PAGE CONFIG
# ---------------------------------------------------
# st.set_page_config(
    # page_title="Employee Management System",
    # page_icon="💼",
    # layout="wide",
# )

# ---------------------------------------------------
            #   HEADER + DESCRIPTION
# ---------------------------------------------------
# st.markdown("""
    # <h1 style="text-align:center; color:#1A73E8; margin-bottom:0;">
        # 💼 Employee Management System (DB2)
    # </h1>
    # <p style="text-align:center; font-size:17px; color:gray;">
        # A professional system to manage, analyze & visualize employee records
    # </p>
# """, unsafe_allow_html=True)
# 
# st.markdown("")

# ---------------------------------------------------
            #   SESSION STATE
# ---------------------------------------------------
# if "refresh" not in st.session_state:
    # st.session_state.refresh = False
# 
# def refresh():
    # st.session_state.refresh = True

# ---------------------------------------------------
            #  FETCH EMPLOYEE DATA
# ---------------------------------------------------
# res = requests.get(f"{API}/employees")
# 
# if res.status_code != 200:
    # st.error("❌ Unable to connect to API")
    # st.stop()
# 
# employees = pd.DataFrame(res.json())
# employees["SALARY"] = pd.to_numeric(employees["SALARY"], errors="coerce")
# employees["BONUS"] = pd.to_numeric(employees["BONUS"], errors="coerce")
# 
# if employees.empty:
    # st.warning("⚠ No employee data found")
    # st.stop()
# 
# ---------------------------------------------------
            #    TABS /LAYOUT (4 TABS ONLY)
# ---------------------------------------------------
# tab1, tab2, tab3, tab4 = st.tabs(
    # ["🏠 Dashboard", "🔍 Search & Filters", "📄 Employee Table", "📈 Visualizations"]
# )
# 
# ===================================================
                #   TAB 1: DASHBOARD
# ===================================================
# with tab1:
    # st.markdown("### 📊 Overview Dashboard")
# 
    # col1, col2, col3 = st.columns(3)
    # col1.metric("👥 Total Employees", len(employees))
    # col2.metric("💰 Avg Salary", f"{employees['SALARY'].mean():,.2f}")
    # col3.metric("🎁 Avg Bonus", f"{employees['BONUS'].mean():,.2f}")
# 
    # st.markdown("### 🔎 Quick Department Summary")
# 
    # dept_summary = employees.groupby("DEPARTMENT").agg({
        # "EMP_ID": "count",
        # "SALARY": "mean",
        # "BONUS": "mean"
    # }).rename(columns={"EMP_ID": "EMP_COUNT"})
# 
    # st.dataframe(dept_summary, use_container_width=True)
# 
# ===================================================
            #  TAB 2: SEARCH & FILTERS
# ===================================================
# with tab2:
    # st.markdown("### 🔍 Advanced Search & Filters")
# 
    # c1, c2, c3 = st.columns([1.5, 1, 1])
# 
    # with c1:
        # search_name = st.text_input("Search by Employee Name")
# 
    # with c2:
        # dept_filter = st.multiselect(
            # "Filter by Department",
            # options=employees["DEPARTMENT"].unique()
        # )
# 
    # with c3:
        # salary_range = st.slider(
            # "Salary Range",
            # min_value=int(employees["SALARY"].min()),
            # max_value=int(employees["SALARY"].max()),
            # value=(int(employees["SALARY"].min()), int(employees["SALARY"].max()))
        # )
# 
    # filtered = employees.copy()
# 
    # if search_name:
        # filtered = filtered[filtered["NAME"].str.contains(search_name, case=False)]
# 
    # if dept_filter:
        # filtered = filtered[filtered["DEPARTMENT"].isin(dept_filter)]
# 
    # filtered = filtered[
        # (filtered["SALARY"] >= salary_range[0]) &
        # (filtered["SALARY"] <= salary_range[1])
    # ]
# 
    # st.success(f"🔎 {len(filtered)} Employees Found")
    # st.dataframe(filtered, use_container_width=True)
# 
# ===================================================
            #  TAB 3: DATA TABLE
# ===================================================
# with tab3:
    # st.markdown("### 📄 Full Employee Database")
# 
    # colA, colB = st.columns(2)
# 
    # with colA:
        # sort_column = st.selectbox("Sort By", employees.columns)
# 
    # with colB:
        # sort_order = st.radio("Order", ["Ascending", "Descending"], horizontal=True)
# 
    # sorted_df = employees.sort_values(
        # sort_column,
        # ascending=(sort_order == "Ascending")
    # )
# 
    # st.dataframe(sorted_df, use_container_width=True, height=500)
# 
# ===================================================
            #  TAB 4: VISUALIZATIONS
# ===================================================
# with tab4:
# 
    # st.markdown("### 📊 Visual Insights")
# 
    # BAR CHART
    # st.markdown("#### 📌 Average Salary by Department")
    # dept_salary = employees.groupby("DEPARTMENT")["SALARY"].mean().reset_index()
    # st.plotly_chart(
        # px.bar(dept_salary, x="DEPARTMENT", y="SALARY", text="SALARY",
            #    title="Avg Salary by Department"),
        # use_container_width=True
    # )
# 
    # PIE CHART
    # st.markdown("#### 🥧 Employees per Department")
    # dept_counts = employees["DEPARTMENT"].value_counts()
    # st.plotly_chart(
        # px.pie(values=dept_counts.values, names=dept_counts.index, hole=0.4),
        # use_container_width=True
    # )
# 
    # BUBBLE CHART
    # st.markdown("#### 🔵 Bonus vs Salary Ratio")
    # employees["BONUS_RATIO"] = (employees["BONUS"] / employees["SALARY"]) * 100
    # st.plotly_chart(
        # px.scatter(employees, x="SALARY", y="BONUS",
                #    size="BONUS_RATIO", color="DEPARTMENT",
                #    hover_data=["NAME"], title="Bonus/Salary Ratio"),
        # use_container_width=True
    # )
# 
    # HEATMAP
    # st.markdown("#### 🔥 Salary Heatmap")
    # st.plotly_chart(
        # px.density_heatmap(employees, x="DEPARTMENT", y="SALARY"),
        # use_container_width=True
    # )
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 


















import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API = "http://127.0.0.1:5000"
st.set_page_config(page_title="Admin Employee Portal", layout="wide")

# ---------- HEADER ----------
st.markdown("""
    <h1 style="text-align:center; color:#4A90E2;">
        Employee Portal 
    </h1>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- SESSION ----------
if "refresh" not in st.session_state:
    st.session_state.refresh = False

def refresh_data():
    st.session_state.refresh = True
# 

# ---------- MERGE BUTTON ----------
with st.container():
    st.markdown("Merge Employee Files")
    if st.button("Merge EMPLOYEE_FILE1 + EMPLOYEE_FILE2"):
        r = requests.post(f"{API}/merge_employees")
        st.success(r.json().get("message", "Merge Successful"))
        refresh_data()

st.markdown("---")

# ---------- FETCH DATA ----------
res = requests.get(f"{API}/employees")

if res.status_code == 200:
    employees = pd.DataFrame(res.json())

    employees["SALARY"] = pd.to_numeric(employees["SALARY"], errors="coerce")
    employees["BONUS"] = pd.to_numeric(employees["BONUS"], errors="coerce")

    # ---------- KPI CARDS ----------
    st.markdown("## Dashboard Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("👥 Total Employees", len(employees))
    col2.metric("💰 Avg Salary", f"{employees['SALARY'].mean():,.2f}")
    col3.metric("🎁 Avg Bonus", f"{employees['BONUS'].mean():,.2f}")

    st.markdown("---")

    # ---------- SEARCH & FILTER ----------
    st.markdown("##  Search & Filters")

    colA, colB, colC = st.columns([1.5, 1, 1])

    with colA:
        search_name = st.text_input("Search by Employee Name")

    with colB:
        dept_filter = st.multiselect(
            "Filter by Department",
            options=employees["DEPARTMENT"].unique()
        )

    with colC:
        salary_range = st.slider(
            "Salary Range",
            int(employees["SALARY"].min()),
            int(employees["SALARY"].max()),
            (int(employees["SALARY"].min()), int(employees["SALARY"].max()))
        )

    filtered = employees.copy()

    if search_name:
        filtered = filtered[filtered["NAME"].str.contains(search_name, case=False)]

    if dept_filter:
        filtered = filtered[filtered["DEPARTMENT"].isin(dept_filter)]

    filtered = filtered[
        (filtered["SALARY"] >= salary_range[0]) &
        (filtered["SALARY"] <= salary_range[1])
    ]

    # ---------- SORT ----------
    st.markdown("###  Sorting Options")
    colS1, colS2 = st.columns(2)

    with colS1:
        sort_column = st.selectbox("Sort by Column", options=employees.columns)

    with colS2:
        sort_order = st.radio("Sort Order", ["Ascending", "Descending"], horizontal=True)

    filtered = filtered.sort_values(
        sort_column,
        ascending=(sort_order == "Ascending")
    )

    st.dataframe(filtered, width='stretch')

    st.markdown("---")



    st.markdown("## Data Visualizations")

    # BAR CHART – Average Salary by Department
    st.subheader(" Average Salary per Department")

    dept_salary = filtered.groupby("DEPARTMENT")["SALARY"].mean().reset_index()

    fig_bar = px.bar(
        dept_salary,
        x="DEPARTMENT",
        y="SALARY",
        text="SALARY",
        title="Average Salary by Department",
        color="DEPARTMENT"
    )
    fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    st.plotly_chart(fig_bar, config={"responsive": True})

    st.markdown("---")

    # BUBBLE CHART – Bonus-to-Salary Ratio
    st.subheader(" Bonus-to-Salary Ratio Bubble Chart")

    filtered["BONUS_RATIO"] = (filtered["BONUS"] / filtered["SALARY"]) * 100

    fig_bubble = px.scatter(
        filtered,
        x="SALARY",
        y="BONUS",
        size="BONUS_RATIO",
        color="DEPARTMENT",
        hover_data=["NAME"],
        title="Bubble Chart: Bonus-to-Salary Ratio"
    )
    st.plotly_chart(fig_bubble, config={"responsive": True})

    st.markdown("---")

    # 3️ HEATMAP – Salary Heatmap
    st.subheader(" Salary Heatmap (Department vs Salary)")

    fig_heat = px.density_heatmap(
        filtered,
        x="DEPARTMENT",
        y="SALARY",
        title="Salary Heatmap",
        nbinsy=20,
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig_heat, config={"responsive": True})

    st.markdown("---")

    # 4️ PIE CHART – Department Distribution
    st.subheader(" Department Distribution")

    dept_counts = filtered["DEPARTMENT"].value_counts()

    fig_pie = px.pie(
        values=dept_counts.values,
        names=dept_counts.index,
        hole=0.4,
        title="Employees per Department",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    st.plotly_chart(fig_pie, config={"responsive": True})

else:
    st.error(res.json().get("error", "Failed to load employees"))

# ---------- REFRESH ----------
if st.session_state.refresh:
    st.session_state.refresh = False
    st.rerun()
























































































































