# Employee Management System

The application solves the following problems:

Centralized Employee Data Management: Instead of relying on spreadsheets or manual record-keeping, this application provides a centralized solution for storing and managing employee data, reducing the risk of data inconsistencies or loss.
Efficient Data Retrieval: With the search and filtering functionality, you can quickly find employees based on their ID, name, department, or role, saving time and effort compared to manually sifting through large datasets.
Data Organization: By allowing you to sort employees by age or salary, and navigate through the results using pagination, the application helps you organize and present employee data in a more structured and manageable way.

## Description
The Employee Management System is a user-friendly application built with Python and Streamlit that allows you to efficiently manage employee records. With its intuitive interface, you can add new employees, search for existing ones based on various criteria, sort the data by age or salary, and navigate through the results using pagination. This application can be particularly useful for small to medium-sized businesses or organizations that need to maintain and organize employee information.


# features
**Add Employee:** Easily add new employees by providing their name, age, salary, department, and role.
**Search Employees:** Search for employees based on their ID, name, department, or role. You can also apply multiple filters to narrow down the results.
**Sort Employees:** Sort the employee data by age or salary in ascending order.
**Pagination**: Navigate through the search or sort results using pagination, with a maximum of 10 rows displayed per page.
**Error Handling:** The application includes error handling mechanisms to catch and display relevant errors, such as invalid input or database errors.
**Clean User Interface:** The application provides a clean and user-friendly interface powered by Streamlit, making it easy to navigate and use.



## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command:
   `pip install streamlit pandas`
3. Ensure you have SQLite3 installed on your system, as the application uses an SQLite database to store employee data.
   `pip install db-sqlite3`


## Usage

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the following command to start the Streamlit application:
   `streamlit run main.py`
3. The application will open in your default web browser.
4. Use the sidebar to navigate between different options: "Add Employee", "Search Employees", and "Sort Employees".
5. Follow the on-screen instructions to interact with the application and manage employee data. 


# Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.



# License
This project is licensed under the MIT License.

### Acknowledgments
This application was built using the following libraries:
`Streamlit`: Python library for building interactive web applications.
`Pandas`: Python library for data manipulation and analysis.
`SQLite3`: Python's built-in SQLite database library.
