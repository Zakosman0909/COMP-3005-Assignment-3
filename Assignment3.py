import psycopg2

# Global connection parameters for the PostgreSQL database
global_conn_params = {
    "dbname": "",
    "user": "",
    "password": "",
    "host": "",
    "port": ""
}

def get_database_connection():
    # Establishes and returns a connection to the database using global parameters.
    return psycopg2.connect(**global_conn_params)

def getAllStudents():
    # Fetches all student records from the database and prints them.
    conn = get_database_connection()  # Establish a new database connection
    try:
        with conn.cursor() as cur:  # Open a cursor to perform database operations
            cur.execute("SELECT * FROM public.students;")  # Execute a query to retrieve all students
            records = cur.fetchall()  # Fetch all rows of the query result
            for record in records:  # Iterate over and print each student record
                print(record)
    finally:
        conn.close()  # Ensure the connection is closed after operation

def addStudent(first_name, last_name, email, enrollment_date):
    # Inserts a new student record into the database.
    conn = get_database_connection()  # Establish a new database connection
    try:
        with conn.cursor() as cur:  # Open a cursor to perform database operations
            # Execute an INSERT statement to add a new student record with provided details
            cur.execute("INSERT INTO public.students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                        (first_name, last_name, email, enrollment_date))
            conn.commit()  # Commit the transaction to make changes persistent in the database
            print(f"Added student: {first_name} {last_name}")
    finally:
        conn.close()  # Ensure the connection is closed after operation

def updateStudentEmail(student_id, new_email):
    # Updates the email address for a student specified by the student ID.
    conn = get_database_connection()  # Establish a new database connection
    try:
        with conn.cursor() as cur:  # Open a cursor to perform database operations
            # Execute an UPDATE statement to change the email of a specific student
            cur.execute("UPDATE public.students SET email = %s WHERE student_id = %s;",
                        (new_email, student_id))
            conn.commit()  # Commit the transaction to apply the changes
            print(f"Updated student ID {student_id} with new email: {new_email}")
    finally:
        conn.close()  # Ensure the connection is closed after operation

def deleteStudent(student_id):
    # Deletes a student record from the database identified by the student ID.
    conn = get_database_connection()  # Establish a new database connection
    try:
        with conn.cursor() as cur:  # Open a cursor to perform database operations
            # Execute a DELETE statement to remove a student record by ID
            cur.execute("DELETE FROM public.students WHERE student_id = %s;", (student_id,))
            conn.commit()  # Commit the transaction to finalize the deletion
            print(f"Deleted student ID {student_id}")
    finally:
        conn.close()  # Ensure the connection is closed after operation

if __name__ == "__main__":
    # Collect database connection parameters from the user
    global_conn_params["dbname"] = input("Enter the database name: ")
    global_conn_params["user"] = input("Enter the database user: ")
    global_conn_params["password"] = input("Enter the database password: ")
    global_conn_params["host"] = input("Enter the database host (default 'localhost'): ") or "localhost"
    global_conn_params["port"] = input("Enter the database port (default '5432'): ") or "5432"

    while True:  # Main loop to continuously accept user commands
        # Display available actions to the user
        print("\nAvailable Actions:")
        print("1. List all students")
        print("2. Add a new student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Choose an action (1-5): ")  # Prompt user for action choice

        # Execute the corresponding function based on the user's choice
        if choice == '1':
            getAllStudents()
        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == '3':
            student_id = input("Enter student ID to update email: ")
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            deleteStudent(student_id)
        elif choice == '5':
            print("Exiting...")  # Exit the program
            break
        else:
            print("Invalid choice, please choose again.")  # Handle invalid input

