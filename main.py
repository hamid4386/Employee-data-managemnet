import sqlite3
import streamlit as st
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('employees.db')
c = conn.cursor()

# Create a table to store employee data
c.execute('''CREATE TABLE IF NOT EXISTS employees
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, salary REAL, department TEXT, role TEXT)''')

# Function to add employee data to the database
def add_employee(name, age, salary, department, role):
    try:
        with conn:
            c.execute("INSERT INTO employees (name, age, salary, department, role) VALUES (?, ?, ?, ?, ?)", (name, age, salary, department, role))
    except sqlite3.IntegrityError as e:
        st.error(f"Error: {e}")

# Function to search for employees
def search_employees(query, search_by):
    try:
        with conn:
            if search_by == "id":
                try:
                    query = int(query)
                except ValueError:
                    st.error("Please enter a valid integer for ID.")
                    return []
                c.execute("SELECT * FROM employees WHERE id = ?", (query,))
            elif search_by == "name":
                c.execute("SELECT * FROM employees WHERE name LIKE ?", ('%' + query + '%',))
            elif search_by == "department":
                c.execute("SELECT * FROM employees WHERE department LIKE ?", ('%' + query + '%',))
            elif search_by == "role":
                c.execute("SELECT * FROM employees WHERE role LIKE ?", ('%' + query + '%',))
            return c.fetchall()
    except sqlite3.OperationalError as e:
        st.error(f"Error: {e}")
        return []

# Function to sort employees by age or salary
def sort_employees(sort_by):
    try:
        with conn:
            if sort_by == "age":
                c.execute("SELECT * FROM employees ORDER BY age")
            elif sort_by == "salary":
                c.execute("SELECT * FROM employees ORDER BY salary")
            return c.fetchall()
    except sqlite3.OperationalError as e:
        st.error(f"Error: {e}")
        return []

# Streamlit user interface
def main():
    st.set_page_config(page_title="Employee Management System", layout="wide")
    st.title("Employee Management System")

    # Sidebar for navigation
    options = st.sidebar.radio("Select an option", ["Add Employee", "Search Employees", "Sort Employees"])

    if options == "Add Employee":
        st.subheader("Add Employee")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=18, step=1)
        salary = st.number_input("Salary (Rs)", min_value=0.0, step=1.0)
        department = st.text_input("Department")
        role = st.text_input("Role")

        if st.button("Add"):
            add_employee(name, age, salary, department, role)
            st.success("Employee added successfully!")

    elif options == "Search Employees":
        st.subheader("Search Employees")
        search_by = st.selectbox("Search By", ["id", "name", "department", "role"])
        query = st.text_input(f"Enter {search_by}")
        filter_by = st.multiselect("Filter By", ["Name", "Age", "Salary", "Department", "Role"])

        if st.button("Search"):
            results = search_employees(query, search_by)
            if results:
                st.subheader("Search Results")
                # Create a pandas DataFrame from the results
                df = pd.DataFrame(results, columns=["ID", "Name", "Age", "Salary", "Department", "Role"])

                # Apply filters
                if filter_by:
                    for field in filter_by:
                        if field == "Name":
                            df = df[df["Name"].str.contains(query, case=False)]
                        elif field == "Age":
                            df = df[df["Age"].astype(str).str.contains(query)]
                        elif field == "Salary":
                            df = df[df["Salary"].astype(str).str.contains(query)]
                        elif field == "Department":
                            df = df[df["Department"].str.contains(query, case=False)]
                        elif field == "Role":
                            df = df[df["Role"].str.contains(query, case=False)]

                # Pagination
                total_rows = len(df)
                rows_per_page = 10
                last_page = total_rows // rows_per_page + (total_rows % rows_per_page != 0)
                page_number = st.number_input("Page Number", min_value=1, max_value=last_page, value=1, step=1)
                start_index = (page_number - 1) * rows_per_page
                end_index = start_index + rows_per_page

                # Display the paginated DataFrame
                st.write(df.iloc[start_index:end_index])
            else:
                st.warning("No employees found.")

    elif options == "Sort Employees":
        st.subheader("Sort Employees")
        sort_by = st.selectbox("Sort By", ["age", "salary"])
        filter_by = st.multiselect("Filter By", ["Name", "Age", "Salary", "Department", "Role"])

        if st.button("Sort"):
            results = sort_employees(sort_by)
            if results:
                st.subheader(f"Employees sorted by {sort_by}")
                # Create a pandas DataFrame from the results
                df = pd.DataFrame(results, columns=["ID", "Name", "Age", "Salary", "Department", "Role"])

                # Apply filters
                if filter_by:
                    for field in filter_by:
                        if field == "Name":
                            df = df[df["Name"].str.contains("", case=False)]
                        elif field == "Age":
                            df = df[df["Age"].astype(str).str.contains("")]
                        elif field == "Salary":
                            df = df[df["Salary"].astype(str).str.contains("")]
                        elif field == "Department":
                            df = df[df["Department"].str.contains("", case=False)]
                        elif field == "Role":
                            df = df[df["Role"].str.contains("", case=False)]

                # Pagination
                total_rows = len(df)
                rows_per_page = 10
                last_page = total_rows // rows_per_page + (total_rows % rows_per_page != 0)
                page_number = st.number_input("Page Number", min_value=1, max_value=last_page, value=1, step=1)
                start_index = (page_number - 1) * rows_per_page
                end_index = start_index + rows_per_page

                # Display the paginated DataFrame
                st.write(df.iloc[start_index:end_index])
            else:
                st.warning("No employees found.")

if __name__ == "__main__":
    main()