import random
import DB2Query

# --------------------------------
# Random Indian Names
# --------------------------------
first_names = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Ananya", "Diya", "Isha", "Aisha",
    "Rohan", "Kabir", "Aryan", "Anika", "Saanvi", "Krishna", "Lakshya", "Meera", "Riya", "Shreya",
    "Tanvi", "Vishal", "Neha", "Amit", "Sneha", "Kavya", "Raj", "Pooja", "Ansh", "Siddharth",
    "Ishaan", "Naina", "Devansh", "Tanish", "Priya", "Arnav", "Reyansh", "Kriti", "Harsh", "Aarohi",
    "Yash", "Mihir", "Anvi", "Shivansh", "Ritika", "Pranav", "Sanya", "Karan", "Ira", "Manya"
]

last_names = [
    "Sharma", "Patel", "Singh", "Gupta", "Mehta", "Kumar", "Reddy", "Iyer", "Chopra", "Kapoor",
    "Desai", "Jain", "Nair", "Malhotra", "Bhat", "Joshi", "Aggarwal", "Rao", "Verma", "Choudhary",
    "Pandey", "Agarwal", "Ghosh", "Shah", "Trivedi", "Mukherjee", "Saxena", "Prasad", "Naidu", "Khan",
    "Tiwari", "Dutta", "Bansal", "Singhania", "Menon", "Rathore", "Bhardwaj", "Chatterjee", "Ranganathan", "Nambiar",
    "Yadav", "Sinha", "Bhattacharya", "Kohli", "Rajput", "Ramakrishnan", "Chakraborty", "Saxena", "Shinde", "Garg"
]

departments = ["HR", "Finance", "IT", "Marketing", "Sales", "Operations", "Support"]

# --------------------------------
# Generate & Insert Data
# --------------------------------
for i in range(1, 501):
    emp_id = f"EMP{i:03d}"
    name = random.choice(first_names) + " " + random.choice(last_names)
    salary = round(random.uniform(25000, 120000), 2)
    department = random.choice(departments)
    bonus = round(random.uniform(2000, 15000), 2)

    # --- Insert into EMPLOYEE_FILE1 ---
    sql_file1 = f"""
        INSERT INTO EMPLOYEE_FILE1 (EMP_ID, NAME, SALARY)
        VALUES ('{emp_id}', '{name}', {salary})
    """
    a, b = DB2Query.runQuery(sql_file1)
    if not a:
        print(f"❌ ERROR inserting into EMPLOYEE_FILE1 for {emp_id}: {b}")
        break

    # --- Insert into EMPLOYEE_FILE2 ---
    sql_file2 = f"""
        INSERT INTO EMPLOYEE_FILE2 (ID2, DEPARTMENT, BONUS)
        VALUES ('{emp_id}', '{department}', {bonus})
    """
    a, b = DB2Query.runQuery(sql_file2)
    if not a:
        print(f"❌ ERROR inserting into EMPLOYEE_FILE2 for {emp_id}: {b}")
        break

    # --- Insert into EMPLOYEE_MATCHED ---
    sql_matched = f"""
        INSERT INTO EMPLOYEE_MATCHED (EMP_ID, NAME, SALARY, DEPARTMENT, BONUS)
        VALUES ('{emp_id}', '{name}', {salary}, '{department}', {bonus})
    """
    a, b = DB2Query.runQuery(sql_matched)
    if not a:
        print(f"❌ ERROR inserting into EMPLOYEE_MATCHED for {emp_id}: {b}")
        break

    print(f"✅ Inserted record {i}: {name} ({department})")

print("🎯 Data generation and insertion completed successfully!")
